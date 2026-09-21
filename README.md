# Ely Security

> **See further. Stay ahead.**  
> Local-first, evidence-backed, AI-operated security operations without surrendering the security boundary to the AI or to an upstream product.

**Status:** Architecture-qualified design / pre-implementation  
**Default V1:** Small-site local deployment  
**Agent:** Elyandra (OpenCode-derived, outside enforcement boundary)

## Mission

Ely answers:

1. What is here?
2. What is communicating?
3. What changed?
4. Why might it matter?
5. What evidence proves or weakens that conclusion?
6. What can we safely do?
7. What did Ely itself do?

## Architecture in one view

```text
Untrusted network / endpoints
          │
          ▼
 Zeek / Suricata / Arkime? / osquery / infrastructure
          │
          ▼
      Ely Collectors
          │
   raw evidence + normalize
          ▼
     NATS JetStream
          │
 ┌────────┼───────────┬───────────────┐
 ▼        ▼           ▼               ▼
Graph  Detection  Investigations  OpenSearch*
 │        │           │
 └────────┴── PostgreSQL ─────────────┘
                │
          Ely Core APIs
          │           │
          ▼           ▼
    Command Center  Elyandra
          │           │ typed tools only
          └─────┬─────┘
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

* OpenSearch is optional/rebuildable, never canonical truth.
```

## Ely-owned product layer

Ely permanently owns:
- canonical domain/identifiers;
- temporal Security Graph;
- asset/identity resolution;
- evidence/provenance;
- Findings and Investigations;
- Plays and Automations;
- policy/approval model;
- execution-grant contract;
- audit semantics;
- APIs and product UX.

External projects supply replaceable primitives.

## Chosen V1 stack

- **Go:** Core, collectors, policy, execution gateway, node/worker agents.
- **TypeScript/Next.js:** Command Center.
- **TypeScript/OpenCode-derived:** Elyandra.
- **PostgreSQL:** authoritative operational state + temporal graph.
- **NATS JetStream:** durable event backbone.
- **OpenSearch:** optional search/hunt projection.
- **Zeek:** passive network observation.
- **Suricata:** IDS/NSM, separate GPL process.
- **Arkime:** optional indexed session/PCAP provider.
- **osquery:** endpoint query primitive behind Ely Node Agent.
- **Sigma.js/Graphology:** initial Universe browser renderer.
- **Kali VM:** initial isolated ASSESS worker profile, not a control plane.

Security Onion and Malcolm are architectural mines/reference integrations—not Ely's foundation.

## Operating modes

`OBSERVE → INVESTIGATE → DEFEND → ASSESS`

Modes are authority envelopes. Visibility never implies authorization.

## Product surfaces

**Command · Universe · Assets · Wireless · Threats · Investigations · Plays · Operations · Evidence · Automations · Policies · Elyandra · Infrastructure · System**

Universe shows aggregated relationships/flows; packet-level truth remains drill-down evidence.

## Constitutional rules

- evidence before interpretation;
- unknown is valid;
- AI cannot create authority;
- policy fails closed;
- every action has provenance;
- history is temporal and preserved;
- external schemas never become Ely schemas;
- dependencies require exit strategies;
- local defense works without an Ely cloud;
- active assessment requires explicit owned/administered scope.

Read the full [Ely Constitution](docs/constitution.md).

## Architecture book

Start with [docs/README.md](docs/README.md).

High-value references:
- [System Architecture](docs/architecture/system-architecture.md)
- [Technology Stack](docs/architecture/technology-stack.md)
- [Deployment Architecture](docs/architecture/deployment-architecture.md)
- [Policy Engine](docs/architecture/policy-engine.md)
- [Execution Gateway](docs/architecture/execution-gateway.md)
- [Elyandra Architecture](docs/architecture/elyandra-architecture.md)
- [Page Specifications](docs/product/page-specifications.md)
- [Security Stack Genealogy](docs/research/security-stack-genealogy.md)
- [Dependency Register](docs/research/dependency-register.md)

## What remains unknown

Architecture decisions are not being deferred to implementation.

Remaining unknowns require measurement:
- qualified hardware sizing;
- event/packet throughput on target hardware;
- disk-retention duration under real traffic;
- exact wireless chipset/driver qualification;
- performance threshold where optional OpenSearch becomes necessary.

Those are resolved by architecture qualification tests, not speculation.

## Licensing discipline

Ely will comply with upstream licenses and preserve required notices. Strong-copyleft and ELv2/open-core components are isolated deliberately. No historical/open-source code is assumed reusable without source/version/license review.

No Ely project license has been selected yet; that decision should be made before external code contribution or commercial distribution.
