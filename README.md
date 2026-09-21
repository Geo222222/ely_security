# Ely Security

> AI-native security operations environment for people and teams that need continuous visibility, evidence-backed reasoning, and governed action without operating a traditional SOC.

**Status:** Architecture foundation / pre-implementation  
**Primary deployment:** Local-first, single-operator proving ground  
**Target architecture:** Multi-workspace, multi-site product  
**Agent foundation:** Elyandra (OpenCode-derived)  
**Security principle:** The AI is an operator, never the security boundary.

## What Ely Security is

Ely Security is a persistent security operations environment. It combines established network and endpoint telemetry with a canonical Security Graph, an evidence system, Elyandra's agentic reasoning, and governed **Plays** that can investigate, defend, or assess explicitly authorized systems.

The product is designed around six questions:

1. What exists in this environment?
2. What is communicating with what?
3. What changed?
4. Why might it matter?
5. What evidence supports that conclusion?
6. What action is permitted and appropriate?

Ely Security is not intended to replace Zeek, Suricata, Arkime, Security Onion, or other mature sensors and analysis systems. It integrates or learns from them and creates a higher-level operating experience.

## Product surfaces

- **Command** — posture, attention, active investigations, Elyandra focus.
- **Universe** — live temporal graph of assets, identities, connections, flows, external destinations, and findings.
- **Assets** — canonical inventory and observed posture.
- **Wireless** — wireless networks, access points, clients, trust zones, and wireless observations.
- **Threats** — correlated detections and abnormal observations.
- **Investigations** — evidence-backed cases and hypotheses.
- **Plays** — reusable defensive and authorized security-assessment workflows.
- **Operations** — live execution view of Elyandra and running Plays.
- **Evidence** — immutable observations, artifacts, provenance, and retrieval.
- **Elyandra** — operator conversation, activity ledger, memory, and reasoning outputs.
- **Infrastructure** — sensors, Kali execution nodes, Security Onion, integrations, and health.
- **Automations** — continuous trigger/condition/action/verification rules.
- **Policies** — scopes, authority, approvals, and autonomy.
- **System** — configuration, retention, updates, diagnostics, and product administration.

## Core operating modes

`OBSERVE → INVESTIGATE → DEFEND → ASSESS`

Modes are authority envelopes, not themes. A requested action must be allowed by both the active mode and policy. Active assessment is restricted to explicitly authorized targets.

## High-level architecture

```text
Sensors / Endpoints / Network Infrastructure
                 │
                 ▼
        Telemetry Adapters
                 │
                 ▼
     Normalization + Provenance
                 │
        ┌────────┴────────┐
        ▼                 ▼
 Evidence Store      Security Graph
        │                 │
        └────────┬────────┘
                 ▼
        Detection / Correlation
                 │
        ┌────────┴─────────┐
        ▼                  ▼
   Investigations       Universe
        │
        ▼
      Elyandra
        │
        ▼
     Play Engine
        │
        ▼
    Policy Engine
        │
        ▼
 Execution Gateway ──► isolated Kali / response nodes
        │
        ▼
 Results + Evidence ──► graph / investigation / audit ledger
```

## Architectural laws

1. Observations are evidence; interpretations are revisable.
2. Every conclusion must be traceable to evidence.
3. Every action must have actor, reason, target, scope, authority, result, and timestamp.
4. Elyandra cannot bypass policy.
5. OpenCode permissions are UX controls, not isolation.
6. Execution occurs through constrained gateways and isolated workers.
7. Telemetry collection continues when Elyandra is unavailable.
8. Vendor/tool schemas never become the canonical domain model.
9. Raw packet evidence is retained according to policy; the Universe renders flows and relationships, not packet noise.
10. Security testing is allowed only against explicitly authorized scope.
11. Local-first operation must remain viable without a vendor cloud.
12. The architecture must support future multi-workspace/multi-site deployments without forcing V1 to become SaaS.

## Repository map

```text
apps/                 # product applications (future)
services/             # domain services and engines (future)
agents/               # Elyandra and execution-node adapters (future)
packages/             # shared contracts, SDKs, UI, schemas (future)
docs/
  architecture/       # system and domain architecture
  product/            # operating experience and page contracts
  research/           # upstream project adoption research
  decisions/          # Architecture Decision Records
```

## Architecture documentation

Start at [docs/README.md](docs/README.md).

Key documents:
- [Product vision](docs/product/vision.md)
- [System architecture](docs/architecture/system-architecture.md)
- [Domain model](docs/architecture/domain-model.md)
- [Security Graph](docs/architecture/security-graph.md)
- [Play Engine](docs/architecture/play-engine.md)
- [Product/page stack](docs/product/page-stack.md)
- [Upstream adoption research](docs/research/upstream-adoption.md)
- [Threat model](docs/architecture/threat-model.md)

## Current definition of done

Architecture Foundation is complete when the vocabulary, trust boundaries, upstream adoption strategy, core domain objects, page stack, Security Graph, Play/Policy separation, and execution boundary are internally consistent and reviewable by an engineer before implementation begins.

Implementation has **not** started. Open questions are intentionally documented rather than silently resolved.

## License

No project license has been selected yet. Do not assume upstream licenses transfer to Ely Security. Every reused dependency or copied implementation must undergo license review and be recorded in the upstream adoption register.
