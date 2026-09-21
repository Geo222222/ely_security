# ADR-0005 — PostgreSQL is authoritative operational state

**Status:** Accepted  
**Date:** 2026-09-21

## Context
Ely needs transactions, temporal asset/identity state, investigations, policies, audit metadata, and bounded graph traversal. Introducing a specialized graph database before measured need would create another licensing/operational dependency and split truth.

## Decision
Use PostgreSQL as the authoritative operational store, including the V1 temporal Security Graph.

OpenSearch is a projection. Packet/session stores remain evidence providers.

## Consequences
- one transactional source for core state;
- relational graph schema must be designed carefully;
- high-volume tables require partitioning/rollups;
- a graph engine can be added later as a rebuildable projection if benchmarks justify it.

## Evidence
PostgreSQL uses the liberal PostgreSQL License and has mature JSONB/index/recursive-query capabilities.
