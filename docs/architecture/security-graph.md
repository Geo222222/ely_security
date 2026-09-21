# Security Graph

**Status:** Review  
**Version:** 0.1

[← Threat Model](threat-model.md) · [Next: Play Engine →](play-engine.md)

## Purpose

The Security Graph is Ely Security's canonical temporal representation of the environment. It is the source used by Universe, investigations, Elyandra context, and scope-aware Plays.

It is **not** a replacement for raw evidence stores.

## Graph node classes

- Workspace, Site, Network, Zone
- Asset, Interface, Identity
- ExternalEndpoint, Domain, Service
- Process (when endpoint evidence supports it)
- Flow/Session reference
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

The graph must answer both:
- “What is true/observed now?”
- “What did the graph look like at T?”

Do not mutate history away. Store observations/events and derive materialized current state.

Universe time controls:
`LIVE | 5M | 1H | 6H | 24H | 7D | REPLAY`.

## Provenance

Every graph assertion must resolve to:
- source observation(s);
- deterministic derivation; or
- explicitly labeled hypothesis/determination.

Graph edges may have confidence, but confidence cannot replace provenance.

## Universe projection

The Universe does not render raw graph density. A projection service produces view-specific graphs:
- site topology;
- selected asset neighborhood;
- external communications;
- suspicious/new relationships;
- investigation scope;
- historical replay.

Aggregation rules must be explicit. Example: thousands of packets may become one flow edge; multiple flows may become a relationship edge with counts/volume.

## Baseline/change model

Baseline is descriptive history, not “safe.” The graph tracks:
- first seen;
- last seen;
- recurrence;
- typical time-of-day;
- typical destinations/services;
- volume ranges;
- identity stability.

A baseline deviation creates an observation/finding candidate; it does not independently prove maliciousness.

## Storage decision deferred

We intentionally do not choose Neo4j, PostgreSQL, OpenSearch, or another graph store yet. The logical graph contract comes first. Benchmark requirements include temporal queries, neighborhood traversal, high-rate edge updates, retention, replay, and local deployment footprint.

## Acceptance criteria

- An asset's external relationships can be reconstructed for a time window.
- Each visible relationship links to evidence.
- Replay produces deterministic state from the same event set.
- Identity uncertainty is representable.
- Deleting/retiring an asset does not erase historical evidence.
- UI projection cannot silently alter canonical graph state.

## Open questions

- Event-sourced vs bitemporal relational implementation.
- Hot/cold relationship retention.
- Graph projection caching.
- Cross-site identity reconciliation.

[← Threat Model](threat-model.md) · [Next: Play Engine →](play-engine.md)
