# ADR-0002 — Security Onion is a substrate, not the Ely product shell

**Status:** Proposed  
**Date:** 2026-09-21

[← ADR-0001](ADR-0001-local-first-control-plane.md) · [Next ADR →](ADR-0003-external-policy-boundary.md)

## Context
Security Onion already integrates mature network/host visibility and analyst workflows. Rebuilding those primitives wastes engineering effort. However its schemas, UI, licensing, and API availability should not define Ely's product architecture.

## Decision
Treat Security Onion as one candidate integrated telemetry/SOC substrate. Ely owns its canonical domain, Security Graph, Universe, investigations abstraction, Plays, policy, and operator experience.

Adapters must prevent Security Onion-specific fields from leaking across Ely's domain boundary.

## Consequences
- Ely can operate with alternative sensor stacks.
- Integration engineering is required.
- We preserve Security Onion as a lower-level analyst console.
- Pro/ELv2 licensing constraints cannot silently become product requirements.

## Follow-up
Prototype supported data-access paths and perform license review before implementation dependency is accepted.
