# Dependency Register

**Status:** Architecture baseline  
**Date:** 2026-09-21

| Component | Capability | License/profile | Ely relationship | Core truth? | Exit |
|---|---|---|---|---|---|
| PostgreSQL | authoritative relational state | PostgreSQL License | depend | yes, via Ely schema | logical DB contract + migrations |
| NATS JetStream | durable event transport | Apache 2.0 | depend | no | event-bus interface |
| OpenSearch | high-volume search projection | Apache 2.0 | optional depend | no | rebuild projection from evidence/events |
| Zeek | passive network metadata | BSD | integrate | no | sensor adapter |
| Suricata | IDS/NSM | GPLv2 / commercial option | separate-process integrate | no | detection adapter |
| Arkime | session/PCAP indexing | Apache 2.0 | optional integrate | no | SessionProvider |
| osquery | endpoint query primitive | Apache-2.0 OR GPL-2.0-only | integrate | no | EndpointProvider |
| Fleet | osquery fleet reference/provider | mostly MIT, paid portions separate | learn/optional | no | Ely Node Agent |
| Malcolm | NTA composition/reference | Apache 2.0 | learn/selective reuse | no | n/a |
| Security Onion | integrated SOC/reference | ELv2 + upstream licenses | learn/optional integrate | no | native sensor stack |
| OpenCode | Elyandra foundation | MIT | evolve | no security authority | Ely agent contracts |
| CAI | cyber-agent research | mixed MIT + research-use | learn only | no | n/a |
| Stenographer | historical FPC reference | Apache 2.0, archived | learn only | no | Arkime/Suricata/future capture |
| Go toolchain/runtime | core services/workers | BSD-style | depend | n/a | language migration possible but costly |
| TypeScript/React/Next.js | command-center UI | ecosystem licenses | depend | no | web contract |

## Chosen core stack

### Authoritative state — PostgreSQL
Rationale:
- liberal license;
- mature transactional integrity;
- JSONB + relational schema;
- recursive CTEs and indexes sufficient for V1 temporal graph;
- one authoritative operational store avoids premature graph-database coupling.

### Event backbone — NATS JetStream
Rationale:
- Apache 2.0;
- single-binary operational model;
- durable streams/consumers;
- suitable for local-first through distributed deployments;
- lighter than Kafka-class infrastructure for V1.

### Search — OpenSearch, optional projection
Rationale:
- Apache 2.0;
- security/event search ecosystem;
- rebuildable from canonical events/evidence;
- never owns policy, identity, investigations, or graph truth.

### Languages
- **Go:** control-plane services, ingestion, policy, execution gateway, node/worker agents.
- **TypeScript:** Command Center and Elyandra/OpenCode-derived operator process.
- **Python:** isolated research/tool adapters only where ecosystem value justifies it; not a control-plane authority runtime.

## Rule

Adding a core dependency requires updating this register and passing Sovereignty Program review.
