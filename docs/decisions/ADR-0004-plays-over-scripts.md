# ADR-0004 — Plays are the operational primitive

**Status:** Accepted  
**Date:** 2026-09-21

[← ADR-0003](ADR-0003-external-policy-boundary.md) · [Next ADR →](ADR-0005-postgresql-authoritative-state.md)

## Context

Operators need quick actions comparable to scripts, but security work requires branching, evidence, authorization, verification, retries, recovery, and rollback.

## Decision

The primary reusable operational unit is a versioned, typed, durable Play state machine.

Scripts may exist only as bounded implementation details behind registered ToolAdapters.

## Consequences

- Plays are inspectable, resumable, testable, and auditable.
- Dynamic Elyandra plans can be schema-validated before execution.
- Unknown state-changing outcomes enter verification rather than blind retry.
- Script escape hatches are exceptional and policy-gated, not the normal execution model.
