# Project Audit — Security Onion

**Decision:** Learn from + optional integration. Do not make a runtime foundation.  
**Sovereignty target:** S3 through adapter/alternate stack.  
**Evidence date:** 2026-09-21.

## Verified facts

Security Onion 2.4 documents:
- network visibility through Suricata and Zeek/Suricata metadata;
- full packet capture through Suricata or Stenographer depending on deployment;
- endpoint visibility through Elastic Agent/osquery;
- Elasticsearch-backed storage/search;
- manager, sensor, search, receiver, and combined deployment roles;
- ELv2 for Elastic and Security Onion components;
- Pro-only features including the Security Onion Connect API beginning in 2.4.120.

Security Onion's standalone deployment guidance starts at a relatively heavy footprint (24 GB RAM minimum in current 2.4 documentation), reinforcing that it is not the smallest possible substrate for Ely's initial local appliance.

## Architecture worth learning

1. Separate sensors from management/search.
2. Keep packet capture close to sensors.
3. Buffer ingestion between collection and indexing.
4. Support standalone and distributed roles.
5. Present alert → hunt → packet → case workflows.
6. Treat grid health/configuration as an operational surface.

## What Ely will not inherit

- Security Onion Console as Ely UX.
- Elasticsearch documents as Ely canonical data.
- Connect API as a required integration.
- Salt/configuration topology as Ely lifecycle architecture.
- Security Onion user/case model.
- Security Onion ELv2 code in Ely core without an intentional licensing decision.

## Integration strategy

Security Onion can be supported as a provider profile.

Adapter inputs may include exported logs/events, supported search interfaces, files, or explicitly licensed APIs. Ely's adapter contract cannot require a Pro feature.

The adapter emits Ely canonical:
- Observation;
- Alert;
- Flow/SessionReference;
- EvidenceReference;
- SourceHealth.

## Exit plan

Ely remains functional with:
`Zeek + Suricata + Arkime/direct PCAP + osquery + OpenSearch/PostgreSQL`
without Security Onion.

## Sources

- https://docs.securityonion.net/en/2.4/license.html
- https://docs.securityonion.net/en/2.4/pro.html
- https://docs.securityonion.net/en/2.4/introduction.html
- https://docs.securityonion.net/en/2.4/architecture.html
- https://docs.securityonion.net/en/2.4/hardware.html
- https://blog.securityonion.net/2021/03/

## Remaining empirical work

Prototype the least-coupled supported export/search path from a current Security Onion installation and measure integration cost. This does not block Ely core architecture.
