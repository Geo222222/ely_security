# Ely Live Guard v0

Immediate local visibility while full Ely is being built.

## What runs today

- Suricata IDS/NSM with ET Open rules.
- Ely Live Guard local dashboard and SQLite history.
- Optional Zeek JSON enrichment.
- Windows host audit/safe firewall+Defender baseline.
- No automated blocking or active scanning.

Dashboard defaults to http://127.0.0.1:8787 and is not exposed to the LAN.

## Ubuntu sensor install

    git checkout implementation/live-guard-v0
    sudo ./live_guard/bootstrap_ubuntu.sh

For a sensor on a private LAN you own/administer:

    sudo ./live_guard/bootstrap_ubuntu.sh --interface enp1s0 --trusted-cidr 192.168.50.0/24

Do not mark campground/public upstream address space as trusted.

Verify:

    sudo systemctl status ely-suricata ely-live-guard --no-pager
    sudo tail -f /var/log/suricata/eve.json
    curl http://127.0.0.1:8787/healthz

## Placement matters

Whole-home visibility requires the sensor at the gateway/bridge, a TAP, or switch mirror/SPAN port. Running it only on a workstation primarily observes that workstation.

## Windows workstation

Audit only:

    .\live_guard\windows_host_guard.ps1

Apply the narrow safe baseline:

    .\live_guard\windows_host_guard.ps1 -ApplySafe

This enables Windows Firewall with default inbound blocking and requests Microsoft Defender real-time protection. It does not open ports or change remote-access settings.

## Optional Zeek

Live Guard reads JSON conn.log, dns.log, notice.log, ssl.log and tls.log from the configured Zeek directory. Enable Zeek JSON logging with policy/tuning/json-logs and restart Live Guard.

## Why no auto-block yet

Live Guard is OBSERVE-first. Device identity is still IP-level bootstrap identity, and false containment is worse than an alert. Full Ely will put defensive actions behind Identity Resolution, Plays, Policy, approvals, verification and audit.

## Downloadable tested bundle

The chat also contains ely-live-guard-v0.zip with the locally smoke-tested standalone package.