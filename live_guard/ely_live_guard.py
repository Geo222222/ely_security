#!/usr/bin/env python3
"""Ely Live Guard v0: dependency-free local Suricata/Zeek cockpit."""
from __future__ import annotations
import argparse, ipaddress, json, os, signal, sqlite3, threading, time, urllib.parse
from dataclasses import dataclass
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

VERSION="0.1.0"
DEFAULT_NETS=["10.0.0.0/8","172.16.0.0/12","192.168.0.0/16"]

def now(): return time.time()
def ts(v):
    if isinstance(v,(int,float)): return float(v)
    if not v: return now()
    s=str(v)
    try:
        if s.endswith("Z"): s=s[:-1]+"+00:00"
        return datetime.fromisoformat(s).timestamp()
    except Exception:
        try: return float(s)
        except Exception: return now()
def iso(v): return datetime.fromtimestamp(v,tz=timezone.utc).astimezone().isoformat(timespec="seconds")

@dataclass
class Config:
    bind:str; port:int; db:Path; eve:Path; zeek:Path; nets:list; known:dict; stale:int
    @classmethod
    def load(cls,p):
        d=json.loads(Path(p).read_text()) if p and Path(p).exists() else {}
        dash=d.get("dashboard",{})
        cidrs=os.getenv("ELY_TRUSTED_CIDRS")
        vals=[x.strip() for x in cidrs.split(",") if x.strip()] if cidrs else d.get("trusted_cidrs",DEFAULT_NETS)
        nets=[]
        for x in vals:
            try: nets.append(ipaddress.ip_network(x,strict=False))
            except ValueError: pass
        return cls(
            os.getenv("ELY_BIND",dash.get("bind","127.0.0.1")),
            int(os.getenv("ELY_PORT",dash.get("port",8787))),
            Path(os.getenv("ELY_DB",d.get("db_path","./data/live_guard.db"))),
            Path(os.getenv("ELY_SURICATA_EVE",d.get("suricata_eve","/var/log/suricata/eve.json"))),
            Path(os.getenv("ELY_ZEEK_DIR",d.get("zeek_dir","/opt/zeek/logs/current"))),
            nets or [ipaddress.ip_network(x) for x in DEFAULT_NETS],
            {str(k):str(v) for k,v in d.get("known_assets",{}).items()},
            int(d.get("source_stale_seconds",30))
        )

class Store:
    def __init__(self,cfg):
        self.cfg=cfg; cfg.db.parent.mkdir(parents=True,exist_ok=True)
        self.lock=threading.RLock(); self.db=sqlite3.connect(cfg.db,check_same_thread=False); self.db.row_factory=sqlite3.Row
        self.db.execute("PRAGMA journal_mode=WAL"); self.db.executescript("""
        CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY,ts REAL,source TEXT,event_type TEXT,severity TEXT,src_ip TEXT,src_port INTEGER,dst_ip TEXT,dst_port INTEGER,protocol TEXT,summary TEXT,raw_json TEXT);
        CREATE INDEX IF NOT EXISTS e_ts ON events(ts DESC);
        CREATE TABLE IF NOT EXISTS assets(ip TEXT PRIMARY KEY,label TEXT,internal INTEGER,first_seen REAL,last_seen REAL,event_count INTEGER DEFAULT 0,alert_count INTEGER DEFAULT 0,last_protocol TEXT,known INTEGER DEFAULT 0);
        CREATE TABLE IF NOT EXISTS source_health(source TEXT PRIMARY KEY,last_seen REAL,last_error TEXT,path TEXT);
        """); self.db.commit()
    def internal(self,ip):
        try:
            a=ipaddress.ip_address(ip); return any(a in n for n in self.cfg.nets)
        except Exception: return False
    def health_touch(self,source,path,error=None):
        with self.lock,self.db:
            self.db.execute("""INSERT INTO source_health VALUES(?,?,?,?) ON CONFLICT(source) DO UPDATE SET last_seen=excluded.last_seen,last_error=excluded.last_error,path=excluded.path""",(source,now(),error,path))
    def asset(self,ip,t,proto,alert=False):
        if not ip:
            return False
        try: ipaddress.ip_address(ip)
        except ValueError: return False
        old=self.db.execute("SELECT 1 FROM assets WHERE ip=?",(ip,)).fetchone()
        label=self.cfg.known.get(ip); internal=int(self.internal(ip))
        self.db.execute("""INSERT INTO assets VALUES(?,?,?,?,?,1,?,?,?) ON CONFLICT(ip) DO UPDATE SET label=COALESCE(excluded.label,assets.label),internal=excluded.internal,last_seen=MAX(assets.last_seen,excluded.last_seen),event_count=assets.event_count+1,alert_count=assets.alert_count+excluded.alert_count,last_protocol=COALESCE(excluded.last_protocol,assets.last_protocol),known=MAX(assets.known,excluded.known)""",(ip,label,internal,t,t,1 if alert else 0,proto,1 if label else 0))
        return old is None and bool(internal)
    def add(self,e):
        raw=json.dumps(e.get("raw",{}),separators=(",",":"),ensure_ascii=False)[:65536]
        with self.lock,self.db:
            new1=self.asset(e.get("src_ip"),e["ts"],e.get("protocol"),e["severity"] in ("high","critical"))
            new2=self.asset(e.get("dst_ip"),e["ts"],e.get("protocol"),e["severity"] in ("high","critical"))
            self.db.execute("INSERT INTO events(ts,source,event_type,severity,src_ip,src_port,dst_ip,dst_port,protocol,summary,raw_json) VALUES(?,?,?,?,?,?,?,?,?,?,?)",(e["ts"],e["source"],e["event_type"],e["severity"],e.get("src_ip"),e.get("src_port"),e.get("dst_ip"),e.get("dst_port"),e.get("protocol"),e.get("summary",""),raw))
            for ip,n in ((e.get("src_ip"),new1),(e.get("dst_ip"),new2)):
                if ip and n: self.db.execute("INSERT INTO events(ts,source,event_type,severity,src_ip,summary,raw_json) VALUES(?,?,?,?,?,?,?)",(e["ts"],"ely","new_asset","attention",ip,"New internal asset observed: "+ip,"{}"))
    def summary(self):
        t=now(); q=self.db.execute
        with self.lock:
            return {"version":VERSION,"events_15m":q("SELECT COUNT(*) c FROM events WHERE ts>=?",(t-900,)).fetchone()["c"],"high_24h":q("SELECT COUNT(*) c FROM events WHERE ts>=? AND severity IN ('critical','high')",(t-86400,)).fetchone()["c"],"new_assets_24h":q("SELECT COUNT(*) c FROM events WHERE ts>=? AND event_type='new_asset'",(t-86400,)).fetchone()["c"],"internal_assets":q("SELECT COUNT(*) c FROM assets WHERE internal=1").fetchone()["c"],"external_endpoints":q("SELECT COUNT(*) c FROM assets WHERE internal=0").fetchone()["c"]}
    def rows(self,sql,args=()):
        with self.lock: return [dict(x) for x in self.db.execute(sql,args).fetchall()]
    def events(self,n=80): return self.rows("SELECT * FROM events ORDER BY ts DESC LIMIT ?",(max(1,min(n,300)),))
    def assets(self): return self.rows("SELECT * FROM assets ORDER BY internal DESC,last_seen DESC LIMIT 500")
    def connections(self,mins=15):
        rows=self.rows("""SELECT src_ip,dst_ip,COALESCE(protocol,'') protocol,COUNT(*) events,MAX(ts) last_seen,SUM(CASE WHEN severity IN ('critical','high','medium') THEN 1 ELSE 0 END) alerts FROM events WHERE ts>=? AND src_ip IS NOT NULL AND dst_ip IS NOT NULL GROUP BY src_ip,dst_ip,protocol ORDER BY last_seen DESC LIMIT 150""",(now()-mins*60,))
        for x in rows: x["src_internal"]=self.internal(x["src_ip"]); x["dst_internal"]=self.internal(x["dst_ip"])
        return rows
    def health(self):
        rows=self.rows("SELECT * FROM source_health ORDER BY source"); t=now()
        for x in rows:
            x["age_seconds"]=round(t-x["last_seen"],1); x["state"]="degraded" if x["last_error"] else ("healthy" if x["age_seconds"]<=self.cfg.stale else "stale")
        seen={x["source"] for x in rows}
        if "suricata" not in seen: rows.append({"source":"suricata","path":str(self.cfg.eve),"state":"waiting","age_seconds":None,"last_error":None})
        return rows

def suri(o,_):
    kind=str(o.get("event_type","event")); a=o.get("alert") or {}
    sev="info"
    if kind=="alert":
        s=int(a.get("severity",3) or 3); sev="high" if s<=1 else ("medium" if s==2 else "low")
    elif kind in ("anomaly","drop"): sev="medium"
    summary=str(a.get("signature") or kind)
    if kind=="dns": summary="DNS "+str((o.get("dns") or {}).get("rrname") or (o.get("dns") or {}).get("query") or "")
    if kind=="tls": summary="TLS "+str((o.get("tls") or {}).get("sni") or "")
    if kind=="http":
        h=o.get("http") or {}; summary=("HTTP "+str(h.get("http_method",""))+" "+str(h.get("hostname",""))+str(h.get("url",""))).strip()
    return {"ts":ts(o.get("timestamp")),"source":"suricata","event_type":kind,"severity":sev,"src_ip":o.get("src_ip"),"src_port":o.get("src_port"),"dst_ip":o.get("dest_ip"),"dst_port":o.get("dest_port"),"protocol":str(o.get("app_proto") or o.get("proto") or ""),"summary":summary[:400],"raw":o}

def zeek(o,name):
    kind=name.split(".")[0]; src=o.get("id.orig_h"); dst=o.get("id.resp_h"); proto=o.get("service") or o.get("proto") or ""
    summary=str(o.get("msg") or o.get("query") or ("Connection "+str(proto) if kind=="conn" else kind))
    return {"ts":ts(o.get("ts")),"source":"zeek","event_type":"zeek_"+kind,"severity":"medium" if kind=="notice" else "info","src_ip":src,"src_port":o.get("id.orig_p"),"dst_ip":dst,"dst_port":o.get("id.resp_p"),"protocol":str(proto),"summary":summary[:400],"raw":o}

class Tail(threading.Thread):
    daemon=True
    def __init__(self,path,parser,source,store,from_start=False):
        super().__init__(); self.path=path; self.parser=parser; self.source=source; self.store=store; self.from_start=from_start; self.off=0; self.ino=None; self.stop=threading.Event(); self.first=True
    def run(self):
        while not self.stop.is_set():
            try:
                if not self.path.exists(): time.sleep(1); continue
                st=self.path.stat()
                if self.ino!=getattr(st,"st_ino",None) or st.st_size<self.off:
                    self.ino=getattr(st,"st_ino",None); self.off=0 if self.from_start or not self.first else st.st_size; self.first=False
                with self.path.open("r",encoding="utf-8",errors="replace") as f:
                    f.seek(self.off)
                    while not self.stop.is_set():
                        line=f.readline()
                        if not line:
                            self.off=f.tell(); self.store.health_touch(self.source,str(self.path)); break
                        self.off=f.tell()
                        try:
                            e=self.parser(json.loads(line),self.path.name)
                            if e: self.store.add(e)
                            self.store.health_touch(self.source,str(self.path))
                        except json.JSONDecodeError: self.store.health_touch(self.source,str(self.path),"non-JSON log; enable JSON logging")
                        except Exception as ex: self.store.health_touch(self.source,str(self.path),"parse error: "+type(ex).__name__)
                time.sleep(.4)
            except Exception as ex:
                self.store.health_touch(self.source,str(self.path),"tail error: "+type(ex).__name__); time.sleep(1)

HTML=r'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Ely Live Guard</title><style>
:root{color-scheme:dark;--bg:#080914;--p:#111329;--l:#252847;--t:#edf0ff;--m:#9298b9;--a:#9b6cff;--b:#5ea1ff;--r:#ff6075;--y:#ffc857;--g:#61d69a}*{box-sizing:border-box}body{margin:0;background:radial-gradient(circle at 80% -10%,#24163e,#080914 42%);font:14px system-ui;color:var(--t)}header{padding:16px 22px;border-bottom:1px solid var(--l);display:flex;gap:12px;align-items:center}.logo{font-weight:800;letter-spacing:.08em}.logo b{color:var(--a)}.pill{border:1px solid var(--l);border-radius:99px;padding:5px 9px;color:var(--m)}main{max-width:1500px;margin:auto;padding:18px}.grid{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}.card{background:#101225e8;border:1px solid var(--l);border-radius:14px;padding:13px;margin-bottom:12px}.k{color:var(--m);font-size:11px;text-transform:uppercase}.v{font-size:27px;font-weight:750;margin-top:5px}.cols{display:grid;grid-template-columns:1.4fr .6fr;gap:12px}h2{font-size:15px;margin:0 0 10px}table{width:100%;border-collapse:collapse}th,td{padding:8px;border-bottom:1px solid #22253f;text-align:left;white-space:nowrap;max-width:330px;overflow:hidden;text-overflow:ellipsis}th{font-size:11px;color:var(--m);text-transform:uppercase}.hi{color:var(--r);font-weight:700}.med,.att{color:var(--y)}.in{color:#bea9ff}.out{color:#8ec5ff}.dot{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:6px}.healthy{background:var(--g)}.stale,.waiting{background:var(--y)}.degraded{background:var(--r)}small{color:var(--m)}@media(max-width:900px){.grid{grid-template-columns:repeat(2,1fr)}.cols{grid-template-columns:1fr}}</style></head><body>
<header><div class="logo">ELY <b>LIVE GUARD</b></div><span class="pill">OBSERVE</span><span class="pill" id="clock"></span><span style="margin-left:auto;color:var(--m)">local-only v0</span></header><main>
<div class="grid" id="cards"></div><div class="cols"><div class="card"><h2>Live connections · 15m</h2><div style="overflow:auto"><table><thead><tr><th>From</th><th>To</th><th>Proto</th><th>Events</th><th>Alerts</th></tr></thead><tbody id="con"></tbody></table></div></div><div class="card"><h2>Sensor health</h2><div id="health"></div><br><small>Coverage is only what this sensor can actually see. Put it at your gateway/bridge/SPAN for whole-home visibility.</small></div></div>
<div class="card"><h2>Attention & evidence</h2><div style="overflow:auto"><table><thead><tr><th>Time</th><th>Severity</th><th>Source</th><th>Type</th><th>From</th><th>To</th><th>Summary</th></tr></thead><tbody id="ev"></tbody></table></div></div>
<div class="card"><h2>Observed endpoints</h2><div style="overflow:auto"><table><thead><tr><th>IP</th><th>Class</th><th>Known</th><th>Events</th><th>Alerts</th><th>Last proto</th></tr></thead><tbody id="as"></tbody></table></div></div>
</main><script>
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); const td=(v,c='')=>'<td class="'+c+'">'+esc(v??'')+'</td>'; async function j(u){return (await fetch(u,{cache:'no-store'})).json()}
async function go(){try{const [s,e,a,c,h]=await Promise.all([j('/api/summary'),j('/api/events'),j('/api/assets'),j('/api/connections'),j('/api/health')]); document.getElementById('clock').textContent=new Date().toLocaleTimeString(); const vals=[['High · 24h',s.high_24h],['New internal · 24h',s.new_assets_24h],['Internal',s.internal_assets],['External',s.external_endpoints],['Events · 15m',s.events_15m]]; document.getElementById('cards').innerHTML=vals.map(x=>'<div class="card"><div class="k">'+x[0]+'</div><div class="v">'+x[1]+'</div></div>').join(''); document.getElementById('health').innerHTML=h.map(x=>'<div style="padding:7px 0;border-bottom:1px solid #22253f"><span class="dot '+x.state+'"></span><b>'+esc(x.source)+'</b><span style="float:right;color:var(--m)">'+esc(x.state)+'</span><br><small>'+esc(x.path||'')+(x.last_error?'<br>'+esc(x.last_error):'')+'</small></div>').join(''); document.getElementById('ev').innerHTML=e.map(x=>'<tr>'+td(new Date(x.ts*1000).toLocaleTimeString())+td(x.severity,x.severity==='high'?'hi':(x.severity==='medium'?'med':(x.severity==='attention'?'att':'')))+td(x.source)+td(x.event_type)+td(x.src_ip)+td(x.dst_ip)+td(x.summary)+'</tr>').join(''); document.getElementById('as').innerHTML=a.map(x=>'<tr>'+td(x.ip,x.internal?'in':'out')+td(x.internal?'INTERNAL':'EXTERNAL')+td(x.known?(x.label||'yes'):'no')+td(x.event_count)+td(x.alert_count)+td(x.last_protocol)+'</tr>').join(''); document.getElementById('con').innerHTML=c.map(x=>'<tr>'+td(x.src_ip,x.src_internal?'in':'out')+td(x.dst_ip,x.dst_internal?'in':'out')+td(x.protocol)+td(x.events)+td(x.alerts,x.alerts?'med':'')+'</tr>').join('')}catch(e){console.error(e)}} go();setInterval(go,2000)
</script></body></html>'''

class H(BaseHTTPRequestHandler):
    store=None
    def log_message(self,*a): pass
    def sendj(self,x,n=200):
        b=json.dumps(x,separators=(",",":"),ensure_ascii=False).encode(); self.send_response(n); self.send_header("Content-Type","application/json"); self.send_header("Cache-Control","no-store"); self.send_header("Content-Length",str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        p=urllib.parse.urlparse(self.path); q=urllib.parse.parse_qs(p.query)
        if p.path=="/":
            b=HTML.encode(); self.send_response(200); self.send_header("Content-Type","text/html; charset=utf-8"); self.send_header("Content-Security-Policy","default-src 'self' 'unsafe-inline'; connect-src 'self'"); self.send_header("X-Frame-Options","DENY"); self.send_header("Cache-Control","no-store"); self.send_header("Content-Length",str(len(b))); self.end_headers(); self.wfile.write(b)
        elif p.path=="/api/summary": self.sendj(self.store.summary())
        elif p.path=="/api/events": self.sendj(self.store.events(int(q.get("limit",[80])[0])))
        elif p.path=="/api/assets": self.sendj(self.store.assets())
        elif p.path=="/api/connections": self.sendj(self.store.connections(int(q.get("minutes",[15])[0])))
        elif p.path=="/api/health": self.sendj(self.store.health())
        elif p.path=="/healthz": self.sendj({"status":"ok","version":VERSION})
        else: self.sendj({"error":"not_found"},404)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--config",default=os.getenv("ELY_CONFIG","./live_guard.json")); ap.add_argument("--from-start",action="store_true"); a=ap.parse_args()
    cfg=Config.load(a.config); store=Store(cfg); tails=[Tail(cfg.eve,suri,"suricata",store,a.from_start)]
    for n in ("conn.log","dns.log","notice.log","ssl.log","tls.log"):
        p=cfg.zeek/n
        if p.exists(): tails.append(Tail(p,zeek,"zeek",store,a.from_start))
    for t in tails: t.start()
    H.store=store; srv=ThreadingHTTPServer((cfg.bind,cfg.port),H)
    def stop(*_):
        for t in tails: t.stop.set()
        threading.Thread(target=srv.shutdown,daemon=True).start()
    signal.signal(signal.SIGINT,stop); signal.signal(signal.SIGTERM,stop)
    print("Ely Live Guard v%s → http://%s:%s"%(VERSION,cfg.bind,cfg.port)); print("Suricata:",cfg.eve); print("DB:",cfg.db)
    try: srv.serve_forever(.5)
    finally: srv.server_close()
if __name__=="__main__": main()
