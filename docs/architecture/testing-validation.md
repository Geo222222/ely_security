# Testing and Architecture Qualification

**Status:** Accepted  
**Version:** 1.0

## Test pyramid

### Unit
Pure domain/policy/resolver/parser behavior.

### Contract
Every adapter/provider tested against Ely contracts with captured synthetic/sanitized fixtures.

### Integration
PostgreSQL, NATS, OpenSearch(optional), node RPC, evidence store.

### Replay
Same evidence/event stream reconstructs equivalent canonical state.

### Security
Authorization, injection, isolation, tenant boundary, secret leakage, grant replay.

### E2E
Operator workflow from observation through evidence/investigation/action.

### Recovery
Crash, restart, disk pressure, source outage, partial network.

## Mandatory invariant suites

### Evidence
- every material Finding has evidence;
- hash corruption detected;
- retention holds respected.

### Identity
- no IP-only permanent identity;
- randomized MAC scenario;
- merge/split reversibility.

### Policy
Property-based tests around modes, risk classes, scope, approval, deny precedence.

### Execution
Injection corpus against every tool adapter; modified/replayed/expired grants fail.

### Multi-workspace
Object-ID fuzzing cannot cross tenant boundary.

### Prompt injection
Adversarial telemetry/files cannot cause unauthorized tools or secret disclosure.

### Replay
Canonical graph/findings remain deterministic across restart/reprocessing.

## Performance gates

Initial product targets, to be qualified on target hardware:

- local UI ordinary API p95 < 250 ms for bounded current-state queries;
- policy decision p99 < 50 ms excluding external target resolution;
- operation status propagation < 500 ms local;
- Universe initial bounded projection < 2 s for normal small-site dataset;
- no event loss at the qualified site ingest rate during a 10-minute downstream search outage;
- Core restart returns policy/API service before optional search rebuild completes.

These are engineering targets, not guarantees before benchmark.

## Capacity qualification

Measure:
- events/sec by provider;
- NATS backlog and replay;
- PostgreSQL partition/index growth;
- graph neighborhood query latency;
- OpenSearch indexing/search;
- PCAP bytes/hour;
- endpoint CPU/memory;
- wireless sensor load.

Architecture changes require evidence that contract-preserving tuning cannot meet needs.

## Security release gate

No release candidate passes if:
- a known policy bypass exists;
- raw arbitrary agent shell reaches workers;
- cross-workspace access is possible;
- update signature verification fails;
- secrets appear in test traces/logs;
- evidence corruption is silent.

## Definition of architecture-qualified V1

A fresh lab deployment can:
1. ingest Zeek + Suricata;
2. identify assets/relationships;
3. show Universe;
4. create a deterministic Finding;
5. open Investigation with evidence;
6. ask Elyandra for grounded explanation;
7. run an INVESTIGATE Play;
8. deny an out-of-scope action;
9. execute an approved typed worker action;
10. recover correctly from Core restart.
