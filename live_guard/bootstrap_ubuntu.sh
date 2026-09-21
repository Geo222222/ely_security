#!/usr/bin/env bash
set -euo pipefail
IFACE=""
TRUSTED=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --interface) IFACE="$2"; shift 2;;
    --trusted-cidr) TRUSTED="$2"; shift 2;;
    *) echo "Unknown argument: $1" >&2; exit 2;;
  esac
done
if [[ $EUID -ne 0 ]]; then echo "Run with sudo/root." >&2; exit 1; fi
IFACE="${IFACE:-$(ip route show default 2>/dev/null | awk '/default/ {print $5; exit}')}"
if [[ -z "$IFACE" ]]; then echo "Could not determine capture interface; pass --interface." >&2; exit 1; fi
HOST_IP="$(ip -4 addr show dev "$IFACE" | awk '/inet / {print $2; exit}' | cut -d/ -f1)"
TRUSTED="${TRUSTED:-${HOST_IP:-127.0.0.1}/32}"
echo "Capture interface: $IFACE"
echo "Trusted scope: $TRUSTED"
. /etc/os-release
apt-get update
apt-get install -y software-properties-common jq python3 ca-certificates curl
if [[ "${ID:-}" == "ubuntu" ]] && command -v add-apt-repository >/dev/null 2>&1; then
  add-apt-repository -y ppa:oisf/suricata-stable
  apt-get update
fi
apt-get install -y suricata
suricata-update
suricata -T -c /etc/suricata/suricata.yaml
systemctl disable --now suricata.service >/dev/null 2>&1 || true
install -d -m 0755 /opt/ely-live-guard /var/lib/ely-live-guard
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
install -m 0755 "$SCRIPT_DIR/ely_live_guard.py" /opt/ely-live-guard/ely_live_guard.py
cat >/etc/ely-live-guard.json <<JSON
{
  "dashboard": {"bind": "127.0.0.1", "port": 8787},
  "db_path": "/var/lib/ely-live-guard/live_guard.db",
  "suricata_eve": "/var/log/suricata/eve.json",
  "zeek_dir": "/opt/zeek/logs/current",
  "trusted_cidrs": ["$TRUSTED"],
  "known_assets": {},
  "source_stale_seconds": 30
}
JSON
cat >/etc/systemd/system/ely-suricata.service <<UNIT
[Unit]
Description=Ely Live Guard Suricata Sensor
After=network-online.target
Wants=network-online.target
[Service]
Type=simple
ExecStart=/usr/bin/suricata -c /etc/suricata/suricata.yaml -i $IFACE --pidfile /run/ely-suricata.pid
Restart=on-failure
RestartSec=3
[Install]
WantedBy=multi-user.target
UNIT
SURI_USER="root"
SURI_GROUP="root"
if id suricata >/dev/null 2>&1; then SURI_USER="suricata"; SURI_GROUP="suricata"; chown -R suricata:suricata /var/lib/ely-live-guard; fi
cat >/etc/systemd/system/ely-live-guard.service <<UNIT
[Unit]
Description=Ely Live Guard v0 Dashboard
After=ely-suricata.service
Wants=ely-suricata.service
[Service]
Type=simple
User=$SURI_USER
Group=$SURI_GROUP
WorkingDirectory=/var/lib/ely-live-guard
ExecStart=/usr/bin/python3 /opt/ely-live-guard/ely_live_guard.py --config /etc/ely-live-guard.json
Restart=on-failure
RestartSec=2
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=strict
ReadWritePaths=/var/lib/ely-live-guard
ReadOnlyPaths=/var/log/suricata /opt/zeek/logs
[Install]
WantedBy=multi-user.target
UNIT
systemctl daemon-reload
systemctl enable --now ely-suricata ely-live-guard
sleep 2
echo
echo "Ely Live Guard installed."
echo "Dashboard: http://127.0.0.1:8787"
echo "Config: /etc/ely-live-guard.json"
echo "Verify: systemctl status ely-suricata ely-live-guard --no-pager"
echo "EVE: tail -f /var/log/suricata/eve.json"
