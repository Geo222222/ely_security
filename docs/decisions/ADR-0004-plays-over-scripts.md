# ADR-0004 — Plays are the operational primitive

**Status:** Proposed  
**Date:** 2026-09-21

[← ADR-0003](ADR-0003-external-policy-boundary.md) · [Back to Architecture Book](../README.md)

## Context
Operators need quick actions comparable to scripts, but security work requires branching, evidence, authorization, verification, retries, and rollback.

## Decision
The primary reusable unit is a versioned Play state machine. Scripts may exist only as bounded implementation details behind registered typed actions.

## Consequences
- Plays are inspectable, resumable, testable, and auditable.
- Dynamic Elyandra plans can be validated before execution.
- Workflow runtime becomes core infrastructure.
- Script escape hatches require explicit policy and should not be the normal path.
