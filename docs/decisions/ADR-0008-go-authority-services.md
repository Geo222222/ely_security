# ADR-0008 — Authority-bearing services are Go

**Status:** Accepted  
**Date:** 2026-09-21

## Context
Policy, ingestion, node identity, and execution grants are security-critical long-running services. Elyandra/OpenCode is TypeScript and intentionally outside the enforcement boundary.

## Decision
Implement Ely Core, collectors, Policy Engine, Execution Gateway, Node Agent, and Worker Agent in Go.

Use TypeScript for UI and Elyandra.

## Consequences
- clear language/process trust boundary;
- simple static deployment for nodes;
- multi-language monorepo;
- protobuf/OpenAPI contracts prevent direct implementation coupling.
