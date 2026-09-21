# ADR-0003 — Agent permissions are not the enforcement boundary

**Status:** Accepted  
**Date:** 2026-09-21

[← ADR-0002](ADR-0002-security-onion-as-substrate.md) · [Next ADR →](ADR-0004-plays-over-scripts.md)

## Context

Elyandra is OpenCode-derived. OpenCode provides useful permission UX but explicitly does not sandbox its agent. Cybersecurity workflows can create high-impact side effects.

## Decision

Implement deterministic policy and execution enforcement outside Elyandra/OpenCode.

Elyandra may propose typed actions. The Play Engine creates ActionRequests. The Policy Engine evaluates authority. Approved state-changing actions receive short-lived, exact-scope ExecutionGrants consumed by the Execution Gateway/Worker Agent.

## Consequences

- Agent compromise or prompt injection does not automatically confer execution authority.
- OpenCode permissions remain useful defense-in-depth and UX.
- Workers expose typed capabilities rather than arbitrary model-generated command strings.
- Policy and execution keys are inaccessible to Elyandra.
