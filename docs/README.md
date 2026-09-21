# Ely Security Architecture Book

This directory is the canonical architecture record for Ely Security.

## Start here

1. [Constitution](constitution.md)
2. [Product Vision](product/vision.md)
3. [System Architecture](architecture/system-architecture.md)
4. [Sovereignty Program](architecture/sovereignty-program.md)
5. [Technology Stack](architecture/technology-stack.md)
6. [Core Contracts](architecture/core-contracts.md)
7. [Architecture Roadmap](architecture/architecture-roadmap.md)
8. [Architecture Review — 2026-09-21](reviews/architecture-review-2026-09-21.md)
9. [Phase 1 — Give Ely Eyes](implementation/phase-1-foundation.md)

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

## Research / mining

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
  - [OpenCode / Elyandra](research/projects/opencode-elyandra.md)
  - [CAI](research/projects/cai.md)

## Architecture decisions

ADRs live under [decisions/](decisions/).

Accepted direction:

- ADR-0001 — local-first control plane;
- ADR-0002 — Security Onion substrate concept **superseded** by ADR-0009 after deeper research;
- ADR-0003 — agent permissions are not enforcement;
- ADR-0004 — Plays over scripts;
- ADR-0005 — PostgreSQL authoritative state/graph;
- ADR-0006 — NATS JetStream event backbone;
- ADR-0007 — OpenSearch is optional/rebuildable;
- ADR-0008 — Go authority services;
- ADR-0009 — native upstream sensor stack;
- ADR-0010 — isolated active-assessment worker;
- ADR-0011 — Sigma.js initial Universe renderer.

## What “architecture complete” means here

Architecture complete does **not** mean implementation or production qualification is complete.

It means the engineer is not expected to invent:

- who owns canonical state;
- which services exist;
- where trust boundaries sit;
- how evidence/provenance work;
- how identity is resolved;
- how policy/approval works;
- how tools execute;
- which technologies implement V1;
- how upstream dependencies are isolated;
- what pages/workflows the product exposes.

Remaining unknowns are empirical qualification items such as actual events/sec, hardware sizing, packet-retention duration, wireless-driver qualification, and provider performance.

## Document lifecycle

`Draft → Review → Accepted → Superseded`.

Accepted architecture changes through explicit review/ADR, not silent implementation drift.

## Source-of-truth rules

- Constitution governs invariants.
- ADRs record why consequential choices were made.
- Architecture docs define the current intended system.
- Product docs define operator behavior.
- Research docs distinguish verified upstream facts from Ely decisions.
- Core Contracts define the inter-module boundary engineers implement.
- Code cannot silently supersede architecture.

[← Repository README](../README.md)
