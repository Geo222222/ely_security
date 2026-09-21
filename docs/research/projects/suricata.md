# Project Audit — Suricata

**Decision:** Primary IDS/detection engine and optional packet-capture provider for V1, running as a separate process.  
**License:** GPLv2; OISF also offers non-GPL commercial licensing.  
**Sovereignty strategy:** data/process boundary, no proprietary-core linking.

## Verified facts

Suricata is an IDS/IPS/network-security-monitoring engine. Its EVE output provides structured JSON including alerts, anomalies, flows, files, metadata, and protocol-specific records. The upstream repository is GPL-2.0.

OISF's GPL guidance states that redistribution of Suricata binaries must comply with GPLv2 or use an OISF redistribution license.

## Architecture decision

Ely integrates Suricata as an independent executable/container and consumes EVE/PCAP outputs through documented formats.

Ely core code will not link against Suricata libraries unless Ely deliberately accepts the applicable license consequences or obtains a suitable license.

## Ely-owned abstraction

Suricata adapter emits:
- AlertObservation;
- Flow;
- ProtocolObservation;
- FileObservation;
- CaptureReference;
- SensorHealth.

Suricata severity/signature metadata are evidence inputs, not Ely's final Finding severity or confidence.

## Why keep Suricata

Rebuilding a mature detection/signature engine is not strategic Ely IP. Ely's value is evidence correlation, state, reasoning, policy, and controlled response.

## Replacement path

The DetectionProvider contract allows other IDS engines. Rules and source identifiers remain provider-qualified.

## Sources

- https://github.com/OISF/suricata
- https://suricata.io/gpl-faqs/
- https://suricata.io/features/open-source/

## Remaining empirical work

Measure EVE volume, capture overhead, and optimal rule/profile defaults on the target appliance.
