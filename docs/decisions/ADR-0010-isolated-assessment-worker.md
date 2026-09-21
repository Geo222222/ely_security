# ADR-0010 — Active assessment executes in isolated workers

**Status:** Accepted  
**Date:** 2026-09-21

## Context
OpenCode explicitly does not provide a sandbox; CAI history includes command-injection failures. Security assessment tools can have high privilege and impact.

## Decision
Active assessment runs through typed actions on a dedicated worker VM (Kali is the initial tool distribution) authenticated with mTLS and short-lived signed ExecutionGrants.

No normal Elyandra-to-root SSH path exists.

## Consequences
- stronger isolation and auditable scope;
- additional VM/runtime overhead;
- tool adapters must be engineered and tested;
- worker can be rebuilt/replaced independently.
