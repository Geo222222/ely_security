# Security Graph

**Status:** Accepted  
**Version:** 1.0

[← Threat Model](threat-model.md) · [Next: Play Engine →](play-engine.md)

## Purpose

The Security Graph is Ely's canonical temporal representation of the environment. Universe, investigations, Elyandra context, detection/correlation, and scope-aware Plays consume it.

It is not a raw evidence store.

## Storage decision

PostgreSQL is the authoritative V1 graph store (ADR-0005).

Ely uses relational temporal node/edge tables, observations, validity intervals, indexes, recursive CTEs, and materialized current-state projections.

OpenSearch may project graph/event data for search. Browser graph libraries render server projections. Neither is canonical.

A specialized graph database may be introduced later only as a rebuildable projection if measured traversal workloads require it.

## Node classes

- Workspace, Site, Network, Zone
- Asset, Interface, Identity
- ExternalEndpoint, Domain, Service
- Process
- Flow/SessionReference
- Alert, Finding
- Investigation
- Evidence/Artifact reference
- PlayRun/Operation

## Relationship examples

```text
Asset -HAS_INTERFACE→ Interface
Interface -ASSIGNED→ IP
Asset -COMMUNICATES_WITH→ ExternalEndpoint
Asset -RESOLVED→ Domain
Process -INITIATED→ Flow
Alert -SUPPORTS→ Finding
Finding -AFFECTS→ Asset
Investigation -EXAMINES→ Relationship
Evidence -SUPPORTS|CONTRADICTS→ Hypothesis
PlayRun -TARGETS→ Asset
Operation -PRODUCED→ Evidence
```

## Temporal semantics

Graph history is never overwritten away.

The system stores event/observation history and derives current projections.

Universe windows:
`LIVE | 5M | 1H | 6H | 24H | 7D | REPLAY`.

Temporal fields use source observation time plus ingest time. Identity/relationship validity is explicit.

## Provenance

Every material assertion resolves to:
- source observations;
- deterministic derivation; or
- explicitly labeled hypothesis/determination.

Confidence never replaces provenance.

## Projection service

Universe receives bounded server-side projections:
- site topology;
- selected-asset neighborhood;
- external communications;
- new/suspicious relationships;
- investigation scope;
- replay at T/during window.

Projection rules specify aggregation. Packet count does not become browser nodes.

## Baseline/change model

Track:
- first/last seen;
- recurrence;
- time-of-day distribution;
- destinations/services;
- volume ranges;
- identity stability;
- source coverage.

Baseline means historically typical, not safe.

## Cross-site identity

Assets remain site-scoped unless strong global identity (enrolled cryptographic Node identity or explicit operator association) supports a cross-site relationship.

No IP/MAC-only global merge.

## Caching

Current-state and common neighborhood projections may be cached, but cache entries are disposable and keyed by graph/policy/time-version.

## Acceptance criteria

- reconstruct external relationships for a window;
- every visible material edge links to evidence;
- deterministic replay produces equivalent graph;
- uncertainty is representable;
- retire/delete UI action never erases history;
- browser projection cannot mutate canonical state;
- deleting OpenSearch/Sigma client state does not affect truth.

[← Threat Model](threat-model.md) · [Next: Play Engine →](play-engine.md)
