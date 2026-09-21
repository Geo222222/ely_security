# Phase 1 Implementation Plan — Give Ely Eyes

**Status:** Ready for engineering after architecture PR acceptance  
**Architecture baseline:** 2026-09-21

## Objective

Implement the smallest vertical slice that proves Ely's architecture rather than merely standing up infrastructure.

Definition:

> Open Universe, see the real authorized network, select an asset/relationship, reach evidence, and ask Elyandra what changed with traceable support.

No DEFEND or ASSESS execution is enabled in this phase.

## Build order

### P1.1 — Repository/bootstrap

Create the accepted monorepo structure.

Tooling:
- Go workspace/modules;
- pnpm workspace for web/Elyandra;
- Protobuf generation;
- OpenAPI generation;
- migrations;
- lint/test/security CI;
- synthetic fixture policy;
- dependency/SBOM generation.

Acceptance:
- reproducible clean checkout build;
- no secret/evidence fixture violations;
- generated contracts checked for drift.

### P1.2 — Core contracts

Implement `core-contracts.md`:
- IDs/enums;
- ObservationEnvelope;
- EvidenceRecord;
- Asset/Interface/Identifier;
- Flow;
- Finding;
- SourceHealth.

No provider code before contract tests exist.

### P1.3 — Persistence/event foundation

Stand up:
- PostgreSQL;
- migrations;
- local BlobStore;
- NATS JetStream.

Implement:
- transaction/outbox boundary where Core publishes state-derived events;
- health checks;
- backup smoke test;
- local dev compose profile.

Acceptance:
- restart without state loss;
- NATS outage/recovery test;
- blob hash corruption test.

### P1.4 — Telemetry Gateway

Implement Go collector framework:
- authenticated source identity;
- raw evidence persistence;
- normalization interface;
- JetStream publication;
- bounded spool;
- quarantine.

First adapters:
1. Zeek JSON;
2. Suricata EVE.

Acceptance:
- captured synthetic fixtures normalize deterministically;
- duplicate/replay is idempotent;
- malformed schema becomes quarantined evidence.

### P1.5 — Identity + Security Graph

Implement:
- Asset;
- Interface;
- IP/MAC/hostname assertions;
- DHCP-aware temporal identity;
- ExternalEndpoint;
- Flow;
- relationship projection.

Acceptance:
- IP churn fixture;
- MAC randomization fixture;
- historical relationship reconstruction;
- current-state projection.

### P1.6 — Evidence API

Implement:
- metadata;
- raw event retrieval;
- artifact CAS;
- provenance traversal;
- retention protection.

Acceptance:
Finding/relationship can resolve all the way to raw source record.

### P1.7 — Core query API

REST/OpenAPI:
- sites/networks;
- assets;
- relationships;
- flows;
- evidence;
- source health;
- graph projection.

SSE:
- live graph delta;
- source health.

### P1.8 — Command Center shell

Implement canonical shell and routes.

Only functional Phase 1 pages:
- Command;
- Universe;
- Assets;
- Evidence;
- Infrastructure;
- Elyandra drawer.

Other accepted routes may use explicit “not implemented” product states rather than fake data.

### P1.9 — Universe V1

Server projection + Sigma.js renderer.

Features:
- live asset nodes;
- internal/external edges;
- direction/activity;
- time window;
- edge/node selection;
- inspector;
- evidence drill-down;
- coverage state.

No packet animation theater. Display only derived activity backed by telemetry.

### P1.10 — Elyandra read-only

Run Elyandra as separate process.

Expose only:
- get assets;
- get graph delta;
- get relationships;
- get source health;
- search/fetch evidence.

Implement structured grounded response contract.

Qualification questions:
- “What is on my network?”
- “What appeared in the last hour?”
- “Who is this asset talking to?”
- “What changed?”
- “Show me the evidence.”

### P1.11 — Qualification

Run full architecture qualification fixture and a controlled live site session.

Evidence packet:
- service health;
- ingestion metrics;
- graph screenshots;
- raw-to-canonical trace;
- Elyandra grounded answers;
- restart/recovery;
- coverage gaps;
- measured CPU/RAM/storage/event rates.

## Explicitly deferred

Phase 1 does not include:
- active assessment;
- containment;
- endpoint response;
- dynamic Plays;
- complex automation;
- cloud federation;
- commercial packaging;
- full wireless monitor-mode operations.

The architecture for those exists; implementation waits until Ely has trustworthy eyes.

## Exit criteria

Phase 1 is complete only if:

1. actual authorized traffic populates the graph;
2. every material relationship has evidence provenance;
3. source outages change coverage state;
4. Elyandra answers from product APIs with evidence refs;
5. Core restart recovers correct current state;
6. no agent process has execution authority;
7. measured capacity results are recorded and architecture defaults adjusted only where evidence warrants.
