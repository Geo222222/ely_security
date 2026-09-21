# Architecture Roadmap

**Status:** Accepted  
**Version:** 1.0

This roadmap orders architectural certainty, not marketing milestones.

## A0 — Constitution and sovereignty

**Complete when:** Ely's non-negotiable laws, dependency policy, research method, and review process are accepted.

Artifacts:
- Constitution
- Sovereignty Program
- Research Methodology
- Engineering Review Workflow

## A1 — Canonical reality model

Define the world Ely believes can exist.

Artifacts:
- Domain Model
- Security Graph
- Asset/Identity Resolution
- Evidence Engine
- Time/replay semantics

Exit criteria:
- vendor-neutral canonical IDs and schemas;
- uncertainty represented explicitly;
- every graph assertion can resolve to provenance.

## A2 — Observation/data plane

Artifacts:
- Telemetry Ingestion
- Sensor/adapter contracts
- Normalization rules
- Search projection
- storage/retention
- backpressure/replay

Exit criteria:
- Zeek, Suricata, endpoint, and generic infrastructure events can enter through versioned adapters;
- raw evidence is preserved;
- source outage/schema drift are visible.

## A3 — Security knowledge plane

Artifacts:
- detection/correlation;
- findings;
- investigations;
- baseline/change model;
- enrichment;
- threat-intel boundary.

Exit criteria:
- alerts are not confused with findings;
- hypotheses preserve evidence for/against;
- deterministic detection works without Elyandra.

## A4 — Control and enforcement plane

Artifacts:
- Play Engine
- Policy Engine
- Execution Gateway
- Worker protocol
- Automation Engine
- approval model

Exit criteria:
- no state-changing action bypasses policy;
- worker compromise cannot create authority;
- every execution produces auditable evidence.

## A5 — Elyandra reasoning plane

Artifacts:
- Elyandra Gateway
- typed tool catalog
- contextual UI contract
- memory model
- prompt-injection/data-boundary controls
- evaluation harness

Exit criteria:
- Elyandra can answer environment questions without direct DB/shell credentials;
- model outputs remain typed proposals;
- evidence links survive rendering.

## A6 — Operator experience

Artifacts:
- page stack;
- page specifications;
- Universe projections;
- Operations state model;
- approval UX;
- accessibility/responsive behavior.

Exit criteria:
- each operator question maps to a route, data contract, and action;
- exactly one canonical source drives shared navigation/context.

## A7 — Deployment and lifecycle

Artifacts:
- local appliance topology;
- multi-site federation;
- identity/RBAC;
- updates;
- backup/restore;
- observability;
- supply-chain controls.

Exit criteria:
- single-site local deployment can recover from reboot/source outage;
- future multi-workspace boundaries are explicit without forcing SaaS.

## A8 — Architecture qualification

Implementation spikes validate:
- event throughput;
- storage growth;
- graph query performance;
- PCAP/session retrieval;
- worker isolation;
- policy latency;
- replay determinism;
- upgrade/recovery.

Only empirical thresholds are adjusted. Architectural invariants require ADRs to change.
