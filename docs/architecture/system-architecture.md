# System Architecture

**Status:** Accepted for V1 implementation  
**Version:** 1.0

[← Product Vision](../product/vision.md) · [Next: Domain Model →](domain-model.md)

## Architectural style

Ely Security is a local-first, event-driven security control plane over replaceable observation/execution primitives.

V1 uses a modular Go Core rather than a microservice fleet. Separate deployables exist only for privilege, hardware placement, runtime, or failure-domain reasons.

## Runtime topology

```text
NETWORK / ENDPOINTS
       │
       ▼
Zeek / Suricata / Arkime? / osquery / gateway sources
       │
       ▼
Ely Collectors (Go)
       │
       ├── raw Evidence
       ▼
Normalization
       │
       ▼
NATS JetStream
       │
 ┌─────┼─────────────┬─────────────────┐
 ▼     ▼             ▼                 ▼
Graph  Detection   Investigation    OpenSearch
Proj.  Correlation / Automation     projection
 │       │
 └── PostgreSQL authoritative state ──┐
                                     │
                               Ely Core APIs
                                     │
                         ┌───────────┴──────────┐
                         ▼                      ▼
                    Command Center          Elyandra
                         │                      │ typed
                         └──────────┬───────────┘ tools
                                    ▼
                               Play Engine
                                    ▼
                               Policy Engine
                                    ▼
                            Execution Gateway
                                    ▼
                     isolated Worker / Kali VM
                                    ▼
                         Results + Evidence/Audit
```

## Technology boundaries

### Ely Core — Go
Contains domain modules:
- identity;
- graph;
- evidence metadata;
- detection/correlation;
- investigations;
- Plays;
- policy;
- automation;
- execution gateway;
- auth/RBAC;
- audit/API.

### PostgreSQL
Authoritative operational state and temporal Security Graph.

### NATS JetStream
At-least-once internal durable event transport.

### Evidence BlobStore
Local content-addressed filesystem in V1; object backend interface for later.

### OpenSearch
Optional rebuildable search/hunt projection.

### Elyandra — TypeScript
Separate reasoning process using bounded Ely APIs.

### Command Center — Next.js/TypeScript
Operator experience. Sigma.js/Graphology render Universe projections.

## Observation plane

Default native provider stack:
- Zeek — passive protocol/network observations;
- Suricata — IDS/NSM and optional capture;
- Arkime — optional indexed session/PCAP;
- Ely Node Agent + osquery — endpoint;
- firewall/router/DNS/DHCP/syslog;
- optional wireless sensor/controller.

Security Onion and Malcolm are reference/optional provider profiles, not the default product substrate.

## Evidence plane

Raw source evidence/artifacts are persisted or referenced with hashes/provenance. Canonical normalization never discards the source lineage.

## Knowledge plane

Asset/Identity Resolver + temporal Security Graph.

Epistemic classes:
`OBSERVATION → DERIVED FACT → HYPOTHESIS → DETERMINATION`.

## Detection/investigation plane

Provider alerts feed deterministic Ely detection/correlation. Alerts are not Findings. Findings lead to evidence-backed Investigations.

## Reasoning plane

Elyandra:
- queries graph/evidence;
- proposes hypotheses/Plays;
- requests policy-governed operations.

It has no database, root, policy-signing, or execution-grant credentials.

## Orchestration/enforcement

Play Engine executes typed state machines.

Policy Engine deterministically returns:
`PERMIT | DENY | REQUIRE_APPROVAL`.

Execution Gateway issues short-lived, exact-target grants to isolated Worker Agents.

## API/transport

- HTTPS REST/OpenAPI — product/operator;
- gRPC/Protobuf + mTLS — nodes/workers/internal RPC;
- NATS — durable eventing;
- SSE — default UI realtime.

## Failure behavior

- Elyandra unavailable → collection/detection/policy/automation continue.
- OpenSearch unavailable → search degraded; truth remains available.
- NATS unavailable → collectors spool bounded local backlog and surface degradation.
- PostgreSQL unavailable → authority/state mutations pause; collectors spool; state-changing execution fails closed.
- Policy unavailable → state-changing execution denied.
- Worker unavailable → Operation pauses/fails-needs-verification.
- schema drift → quarantine + source DEGRADED.
- disk pressure → protected evidence/state preserved; low-priority packet capture rotates/stops before core corruption.
- clock skew → source and ingest timestamps retained; skew surfaced.

## Deployment evolution

### V1 Small Site
Core Node + sensor/gateway + endpoints + isolated assessment VM.

### Multi-site
Local site collection/policy continues; federation aggregates metadata/management.

### Multi-workspace
Strict workspace isolation, RBAC/federation, per-site retention. No V1 code assumes singleton workspace/site/node.

## Cross-document contracts

- Constitution governs invariants.
- Technology Stack governs defaults.
- Storage/Retention defines ownership.
- Telemetry Ingestion defines event flow.
- Policy/Execution define authority.
- Deployment defines physical boundaries.
- Testing/Validation defines proof.

[← Product Vision](../product/vision.md) · [Next: Domain Model →](domain-model.md)
