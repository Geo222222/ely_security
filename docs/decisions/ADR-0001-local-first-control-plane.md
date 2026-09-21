# ADR-0001 — Local-first control plane

**Status:** Accepted  
**Date:** 2026-09-21

[← Upstream Adoption](../research/upstream-adoption.md) · [Next ADR →](ADR-0002-security-onion-as-substrate.md)

## Context

The initial environment is local and security-sensitive. Monitoring must not depend on Ely Security cloud availability. The product may later serve multiple users/sites.

## Decision

Build Ely Security local-first. Site telemetry, policy enforcement, worker execution, evidence access, and core operator functionality run locally. Future cloud services are optional coordination/federation layers, not mandatory trust anchors for local defense.

## Consequences

- Ely owns local packaging, upgrade, backup, and lifecycle responsibilities.
- Local visibility and enforcement survive Internet/Ely-cloud loss.
- Multi-site architecture federates local Sites rather than converting them into thin cloud clients.
- V1 proves the security loop without premature SaaS infrastructure.

## Alternatives rejected

**Cloud-first centralized SOC:** rejected because it adds availability, privacy, latency, cost, and sovereignty dependencies before the core operating model is proven.
