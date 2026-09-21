# Technology Stack

**Status:** Accepted for V1 architecture  
**Version:** 1.0

## Core principle

Technology choices serve Ely-owned contracts. They are implementation defaults, not product identity.

## Backend/control plane

### Go
Used for:
- Ely Core;
- Telemetry Gateway;
- Policy Engine;
- Play/Automation runtime;
- Execution Gateway;
- collectors;
- node/worker agents.

Why:
- strong concurrency and networking;
- static binaries;
- predictable deployment;
- mature gRPC/NATS/PostgreSQL ecosystem;
- smaller attack/operational surface than a large dynamic runtime for authority services.

## Agent/operator process

### TypeScript
Elyandra remains a separate TypeScript process because its OpenCode-derived foundation and AI-tool ecosystem live there.

Boundary: typed API only; no direct authority/state ownership.

## Frontend

### Next.js + React + TypeScript
Product shell and command center.

### Design system
Ely-owned tokens/components.

Accessible primitives may use Radix UI selectively (MIT), but Ely's visual identity and component contracts remain owned.

### Universe graph
Sigma.js + Graphology is the initial browser rendering stack because Sigma uses WebGL and targets graphs with thousands of nodes/edges. It remains a rendering implementation behind an Ely `UniverseRenderer` adapter.

No canonical graph state lives in the browser.

## Authoritative database

### PostgreSQL
Authoritative operational state, temporal graph, audit metadata, policies, investigations, asset identity.

## Event bus

### NATS JetStream
Durable internal delivery/backpressure.

## Search

### OpenSearch
Optional high-volume search/hunt projection. Apache-2.0 and rebuildable.

## Packet/session

### Zeek
Passive protocol/network observation.

### Suricata
IDS/NSM and optional packet capture.

### Arkime
Optional indexed session/PCAP provider.

## Endpoint

### Ely Node Agent + osquery
Ely owns enrollment/transport/control; osquery supplies low-level OS query capability.

## Protocols

- HTTPS REST/OpenAPI: product API;
- gRPC/Protobuf + mTLS: nodes/internal high-integrity RPC;
- NATS: event transport;
- SSE: default realtime UI;
- WebSocket only for genuinely bidirectional interactive surfaces.

## Packaging

- OCI containers for Core service composition where useful;
- system packages/static binaries for node agents;
- dedicated VM for assessment worker;
- Docker Compose-equivalent small-site profile first;
- Kubernetes is not a V1 dependency.

## Dependency posture

| Technology | Role | Replaceability |
|---|---|---|
| Go | authority services | costly but not domain-defining |
| PostgreSQL | system of record | schema is Ely-owned |
| NATS | bus | event abstraction |
| OpenSearch | projection | fully rebuildable |
| Next.js | web framework | API/UI contracts owned |
| Sigma.js | graph renderer | renderer adapter |
| Zeek | sensor | adapter |
| Suricata | sensor | adapter |
| Arkime | evidence provider | provider interface |
| osquery | endpoint primitive | provider interface |

## Sources relevant to license/fit

- PostgreSQL License: https://www.postgresql.org/about/licence/
- OpenSearch Apache 2.0: https://docs.opensearch.org/platform/
- NATS Apache 2.0: https://github.com/nats-io/nats-server/blob/main/LICENSE
- Next.js MIT: https://github.com/vercel/next.js/blob/canary/license.md
- Radix MIT: https://github.com/radix-ui/primitives/blob/main/LICENSE
- Sigma.js MIT / WebGL graph focus: https://github.com/jacomyal/sigma.js
