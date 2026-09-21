# Architecture Review — 2026-09-21

**Scope:** Ely Security architecture foundation  
**Reviewer role:** Chief Systems Reviewer  
**Result:** PASS WITH EMPIRICAL QUALIFICATION REQUIRED  
**Implementation status:** Architecture ready for Phase 1 vertical slice; not yet production-qualified.

## Review method

Applied the accepted Engineering Review Workflow:

1. vocabulary;
2. responsibility/state ownership;
3. dependency/coupling;
4. trust boundaries;
5. failure modes;
6. sovereignty;
7. product traceability;
8. testability;
9. operations;
10. implementation readiness.

## A0 constitutional findings

### Resolved — AI enforcement ambiguity
Earlier agent concepts could be misread as granting OpenCode permissions security authority.

Resolution:
- ADR-0003 accepted;
- deterministic Go Policy Engine;
- isolated Execution Gateway/worker;
- no Elyandra execution keys/root credentials.

### Resolved — upstream product dependency
Early architecture treated Security Onion as a possible substrate.

Resolution:
- deeper license/history research;
- ADR-0002 retained but superseded;
- ADR-0009 selects native Zeek/Suricata/optional Arkime/osquery composition;
- Security Onion/Malcolm become reference/optional integrations.

No unresolved A0 findings remain.

## A1 trust/data-loss findings

### Resolved — canonical search-store ambiguity
Earlier design could allow search infrastructure to become truth.

Resolution:
- PostgreSQL authoritative;
- Evidence BlobStore authoritative for artifacts;
- OpenSearch explicitly disposable/rebuildable;
- NATS transport only.

### Resolved — packet evidence ownership
Packet evidence may be provider-owned at high volume, but Ely owns immutable references/provenance and exports protected case evidence when necessary.

### Resolved — identity overconfidence
Asset resolver no longer treats IP/MAC as stable identity. Randomized MAC/DHCP churn are explicit.

### Resolved — state-changing retry hazard
Unknown outcome now enters VERIFY_REQUIRED; no blind retry.

No unresolved A1 architecture findings remain.

## A2 contract ambiguity findings

### Resolved — technology decisions
Chosen:
- Go authority services;
- PostgreSQL;
- NATS JetStream;
- optional OpenSearch;
- Next.js/TypeScript UI;
- separate TypeScript Elyandra;
- Sigma.js/Graphology renderer;
- gRPC/mTLS node protocol;
- REST/OpenAPI product API;
- SSE realtime default.

### Resolved — domain distinctions
Defined:
- Flow vs provider SessionReference;
- Alert vs Finding;
- severity vs confidence;
- Ely User vs endpoint PrincipalObservation;
- Observation vs Fact vs Hypothesis vs Determination.

### Resolved — product architecture
Canonical page stack, shell, operator workflows, coverage semantics, Universe density/privacy/accessibility rules documented.

No unresolved A2 architecture findings remain for Phase 1.

## Sovereignty review

### Core Ely-owned
PASS:
- domain;
- graph;
- identity;
- evidence;
- investigations;
- Plays;
- policy;
- execution grants;
- audit;
- APIs;
- UX.

### Dependencies
Each current strategic dependency has a documented role/exit boundary.

Particular licensing constraints recorded:
- Security Onion/Elastic ELv2;
- Suricata GPLv2 / OISF commercial option;
- CAI mixed/research restrictions;
- permissive licenses for selected infrastructure where verified.

Legal review is still required before commercial redistribution; this is a release/legal qualification, not an unanswered system architecture decision.

## Failure-mode review

Architecture has explicit behavior for:
- Elyandra/model outage;
- NATS outage/backlog;
- PostgreSQL outage;
- OpenSearch outage;
- source/sensor outage;
- worker outage;
- schema drift;
- duplicate/late event;
- clock skew;
- disk pressure;
- corrupted evidence;
- unknown action outcome;
- node revocation.

## Product traceability

PASS.

Core promises map to architecture components and acceptance tests in `requirements-traceability.md`.

## Remaining unknowns

Only empirical/qualification items remain:

1. qualified V1 Core/Sensor hardware sizing;
2. real event rate and CPU/RAM utilization;
3. PCAP retention duration for a given disk budget;
4. Arkime vs simpler packet-provider footprint;
5. OpenSearch activation threshold;
6. wireless monitor-mode chipset/driver qualification;
7. exact provider-version compatibility matrices;
8. final commercial redistribution/legal packaging review.

These must be measured or legally reviewed; inventing numeric answers would be false precision.

## Implementation readiness

### Ready
Phase 1 observation vertical slice:
- contracts;
- PostgreSQL/NATS/BlobStore;
- Zeek/Suricata ingestion;
- identity/graph;
- evidence;
- Command/Universe;
- read-only Elyandra.

### Architecture defined but implementation gated
- DEFEND;
- ASSESS;
- isolated workers;
- automations;
- endpoint response.

These are gated by earlier observation/identity qualification, not by missing design.

## Final reviewer conclusion

The architecture is internally coherent enough to begin Phase 1 engineering.

The defining rule for implementation is:

> Engineering may discover empirical limits. It may not silently invent new architecture.

Any deviation from accepted contracts/invariants requires an ADR or document revision.
