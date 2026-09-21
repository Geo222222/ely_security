# ADR-0001 — Local-first control plane

**Status:** Proposed  
**Date:** 2026-09-21

[← Upstream Adoption](../research/upstream-adoption.md) · [Next ADR →](ADR-0002-security-onion-as-substrate.md)

## Context
The initial environment is local and security-sensitive. Monitoring must not depend on Ely Security cloud availability. The product may later serve multiple users/sites.

## Decision
Build Ely Security local-first. Site telemetry, policy enforcement, worker execution, evidence access, and core operator functionality must be capable of running locally. Future cloud services are optional coordination/product layers, not mandatory trust anchors for local defense.

## Consequences
- Higher local packaging/upgrade responsibility.
- Better resilience and privacy.
- Multi-site architecture needs explicit federation later.
- V1 can prove the product without premature SaaS work.

## Alternatives rejected
Cloud-first centralized SOC: rejected for V1 because it adds availability, privacy, cost, and product complexity before the core operating loop is proven.
