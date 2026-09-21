# ADR-0007 — OpenSearch is optional and rebuildable

**Status:** Accepted  
**Date:** 2026-09-21

## Context
Security telemetry benefits from inverted-index search and aggregations, but making search-engine documents canonical repeats the coupling Ely is designed to avoid.

## Decision
Use OpenSearch when event volume/search needs justify it, as a projection fed by canonical events.

PostgreSQL/Evidence remain authoritative.

## Consequences
- Ely can run before OpenSearch is installed for smaller profiles;
- search index can be deleted/rebuilt;
- product APIs do not expose OpenSearch DSL as the canonical contract.

## Evidence
OpenSearch is Apache-2.0 and purpose-built for search/analytics.
