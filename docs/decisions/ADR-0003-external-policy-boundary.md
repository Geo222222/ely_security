# ADR-0003 — Agent permissions are not the enforcement boundary

**Status:** Proposed  
**Date:** 2026-09-21

[← ADR-0002](ADR-0002-security-onion-as-substrate.md) · [Next ADR →](ADR-0004-plays-over-scripts.md)

## Context
Elyandra is OpenCode-derived. OpenCode provides useful permission UX but explicitly does not sandbox its agent. Cybersecurity workflows can create high-impact side effects.

## Decision
Implement deterministic policy and execution enforcement outside Elyandra/OpenCode. Elyandra proposes typed actions. The Play Engine requests policy. The Policy Engine issues decisions. Approved state-changing actions receive short-lived ExecutionGrants consumed by an isolated Execution Gateway/worker.

## Consequences
- More engineering than exposing a shell.
- Compromise/prompt injection of the agent does not automatically grant execution authority.
- OpenCode permissions remain useful defense-in-depth and UX.
- Worker APIs must be typed and narrowly scoped.
