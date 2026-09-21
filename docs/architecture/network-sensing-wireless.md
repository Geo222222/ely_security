# Network Sensing and Wireless Architecture

**Status:** Accepted  
**Version:** 1.0

## Fundamental constraint

Ely can only observe traffic visible at a sensing vantage point. No UI or AI can reconstruct packets a sensor never received.

Therefore network topology is part of the product architecture.

## Recommended site topology

```text
Untrusted Upstream / ISP / Campground Wi-Fi
                    │
                    ▼
            ELY-MANAGED GATEWAY
              /             \
        Trusted LAN        IoT/Camera Zone
            │                   │
      Dev/phones/etc.       cameras/devices
            │
      passive sensor tap
```

The preferred small-site deployment places a managed gateway/router between untrusted upstream connectivity and private networks. The sensor observes north-south traffic at that choke point.

## Visibility sources

### Gateway/switch
- DHCP leases;
- ARP/neighbor table;
- firewall events;
- DNS;
- NAT/session data;
- interface counters.

### Passive network sensor
- Zeek;
- Suricata;
- packet/session provider.

### Endpoint
- Ely Node Agent/osquery;
- process/socket correlation.

Combining these provides more reliable attribution than any source alone.

## East-west traffic

Switched LAN traffic may not traverse the gateway.

To observe east-west:
- switch SPAN/TAP to sensor;
- transparent bridge sensor;
- endpoint telemetry;
- managed switch flow/telemetry.

Product shows coverage gaps explicitly.

## Wireless

### Managed AP/controller visibility
Preferred first source:
- SSID/BSSID;
- associated clients;
- authentication events;
- signal/channel where available;
- roaming;
- security configuration.

### Monitor-mode sensor
Optional dedicated Linux wireless sensor with compatible chipset.

Responsibilities:
- passive 802.11 observations;
- AP/BSSID discovery;
- channel/security changes;
- client association observations where technically visible.

Monitor mode does not imply authorization for injection/deauthentication.

### Active wireless assessment
ASSESS-only, explicit SSID/BSSID/channel scope, dedicated worker/sensor, human approval for disruptive actions.

## Separate hotspots/networks

A separate camera hotspot or isolated network is a separate Network/Zone. The main LAN sensor cannot be assumed to see it.

Options:
- Ely collector on that gateway/hotspot;
- dedicated sensor;
- controller/API integration;
- treat it as partially observed and surface coverage state.

## Upstream boundary

The upstream network is `UNTRUSTED_EXTERNAL`, not an assessment target.

Ely may passively observe traffic to/from it and enrich external endpoints. Active scans beyond explicitly owned/administered scope are denied.

## Coverage model

Every Network has `CoverageState`:
- FULL;
- PARTIAL;
- ENDPOINT_ONLY;
- GATEWAY_ONLY;
- NONE;
- DEGRADED.

Coverage facts include active sensors and last event times.

Findings incorporate coverage limits when estimating confidence.

## Acceptance tests

- UI distinguishes unseen east-west risk from “no traffic”;
- separate hotspot does not appear fully monitored without a source;
- upstream addresses are not auto-added to AssessmentScope;
- monitor sensor loss changes coverage state;
- device relationships can combine gateway + Zeek + endpoint evidence.
