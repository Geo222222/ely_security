# Ely Security Architecture Book

This directory is the canonical architecture record for Ely Security.

## Start here

1. [Constitution](constitution.md)
2. [Product Vision](product/vision.md)
3. [System Architecture](architecture/system-architecture.md)
4. [Sovereignty Program](architecture/sovereignty-program.md)
5. [Technology Stack](architecture/technology-stack.md)
6. [Architecture Roadmap](architecture/architecture-roadmap.md)

## Canonical reality/data plane

- [Domain Model](architecture/domain-model.md)
- [Asset & Identity Resolution](architecture/asset-identity-resolution.md)
- [Security Graph](architecture/security-graph.md)
- [Telemetry Ingestion](architecture/telemetry-ingestion.md)
- [Evidence Engine](architecture/evidence-engine.md)
- [Storage & Retention](architecture/storage-retention.md)
- [Network Sensing & Wireless](architecture/network-sensing-wireless.md)
- [Detection & Correlation](architecture/detection-correlation.md)

## Control/reasoning plane

- [Investigation Engine](architecture/investigation-engine.md)
- [Play Engine](architecture/play-engine.md)
- [Policy Engine](architecture/policy-engine.md)
- [Execution Gateway](architecture/execution-gateway.md)
- [Automation Engine](architecture/automation-engine.md)
- [Elyandra Architecture](architecture/elyandra-architecture.md)
- [API Architecture](architecture/api-architecture.md)

## Security/operations

- [Threat Model](architecture/threat-model.md)
- [Identity/Auth/RBAC](architecture/identity-auth-rbac.md)
- [Secrets & Key Management](architecture/secrets-key-management.md)
- [Observability & Audit](architecture/observability-audit.md)
- [Supply Chain & Updates](architecture/supply-chain-updates.md)
- [Deployment Architecture](architecture/deployment-architecture.md)
- [Testing & Qualification](architecture/testing-validation.md)
- [Repository Structure](architecture/repository-structure.md)
- [Requirements Traceability](architecture/requirements-traceability.md)
- [Engineering Review Workflow](architecture/engineering-review-workflow.md)

## Product architecture

- [Page Stack](product/page-stack.md)
- [Page Specifications](product/page-specifications.md)
- [Operator Workflows](product/operator-workflows.md)

## Research/mining

- [Research Methodology](research/methodology.md)
- [Security Stack Genealogy](research/security-stack-genealogy.md)
- [Upstream Adoption](research/upstream-adoption.md)
- [Dependency Register](research/dependency-register.md)
- Project audits:
  - [Security Onion](research/projects/security-onion.md)
  - [Malcolm](research/projects/malcolm.md)
  - [Arkime](research/projects/arkime.md)
  - [Zeek](research/projects/zeek.md)
  - [Suricata](research/projects/suricata.md)
  - [OpenCode/Elyandra](research/projects/opencode-elyandra.md)
  - [CAI](research/projects/cai.md)

## Architecture decisions

ADRs are under [decisions/](decisions/).

Current accepted direction includes:
- local-first control plane;
- upstream sensor composition rather than Security Onion foundation;
- PostgreSQL authoritative state/graph;
- NATS JetStream event backbone;
- OpenSearch optional projection;
- Go authority services;
- external policy boundary;
- isolated assessment workers;
- Plays rather than scripts;
- Sigma.js initial Universe renderer.

## Document lifecycle

`Draft → Review → Accepted → Superseded`.

“Accepted” means the architecture question is answered. Remaining unknowns must be empirical qualification items, not work handed back to implementation.

## Source-of-truth rules

- Constitution governs invariants.
- ADRs record why consequential choices were made.
- Architecture docs define current intended system.
- Product docs define operator behavior.
- Research docs distinguish verified upstream facts from Ely decisions.
- Code cannot silently supersede architecture; divergence requires an ADR/document update.

[← Repository README](../README.md)
