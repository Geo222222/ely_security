import ipaddress
import tempfile
import unittest
from pathlib import Path

import ely_live_guard as g

class LiveGuardTest(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        cfg=g.Config(
            bind="127.0.0.1", port=0,
            db=Path(self.tmp.name)/"guard.db",
            eve=Path(self.tmp.name)/"eve.json",
            zeek=Path(self.tmp.name)/"zeek",
            nets=[ipaddress.ip_network("192.168.50.0/24")],
            known={"192.168.50.1":"Gateway"},
            stale=30,
        )
        self.store=g.Store(cfg)

    def tearDown(self):
        self.tmp.cleanup()

    def test_suricata_alert_and_asset(self):
        raw={
            "timestamp":"2026-09-21T13:00:00-05:00",
            "event_type":"alert",
            "src_ip":"192.168.50.10","src_port":50000,
            "dest_ip":"1.1.1.1","dest_port":443,
            "proto":"TCP",
            "alert":{"signature":"Synthetic alert","severity":1}
        }
        event=g.suri(raw,"eve.json")
        self.assertEqual(event["severity"],"high")
        self.store.add(event)
        s=self.store.summary()
        self.assertEqual(s["high_24h"],1)
        self.assertEqual(s["internal_assets"],1)
        self.assertEqual(s["external_endpoints"],1)
        self.assertEqual(s["new_assets_24h"],1)

    def test_zeek_flow(self):
        raw={
            "ts":g.now(),
            "id.orig_h":"192.168.50.10","id.orig_p":51000,
            "id.resp_h":"93.184.216.34","id.resp_p":443,
            "proto":"tcp","service":"ssl"
        }
        event=g.zeek(raw,"conn.log")
        self.store.add(event)
        rows=self.store.connections(15)
        self.assertEqual(len(rows),1)
        self.assertTrue(rows[0]["src_internal"])
        self.assertFalse(rows[0]["dst_internal"])

if __name__=="__main__":
    unittest.main()
