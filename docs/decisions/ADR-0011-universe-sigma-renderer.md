# ADR-0011 — Sigma.js is the initial Universe renderer

**Status:** Accepted  
**Date:** 2026-09-21

## Context
Universe needs interactive rendering of thousands of nodes/edges without making the browser graph canonical.

## Decision
Use Sigma.js + Graphology as the initial WebGL browser renderer behind an Ely UniverseRenderer abstraction.

## Consequences
- fast initial implementation using mature MIT-licensed graph libraries;
- server-side projection remains authoritative;
- renderer can be replaced without data/domain migration.

## Evidence
Sigma.js describes its target as WebGL visualization of graphs with thousands of nodes and edges and is MIT licensed.
