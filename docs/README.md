# Ely Security Architecture Book

This directory is the canonical architecture record for Ely Security.

## Reader journey

1. [Product Vision](product/vision.md)
2. [System Architecture](architecture/system-architecture.md)
3. [Domain Model](architecture/domain-model.md)
4. [Threat Model](architecture/threat-model.md)
5. [Security Graph](architecture/security-graph.md)
6. [Play Engine](architecture/play-engine.md)
7. [Page Stack](product/page-stack.md)
8. [Upstream Adoption Research](research/upstream-adoption.md)
9. Architecture Decision Records in [decisions/](decisions/)

## Document lifecycle

Documents use these states: **Draft → Review → Accepted → Superseded**.

A document is not Accepted merely because it exists. Review requires:
- terminology consistency;
- dependency/interface review;
- trust-boundary review;
- failure-mode review;
- traceability to product requirements;
- explicit open questions and risks;
- buildability by an engineer;
- testability of claimed behavior.

## Source-of-truth rules

- ADRs record *why* consequential choices were made.
- Architecture docs describe current intended structure.
- Product docs define operator experience and product behavior.
- Research docs distinguish verified upstream capability from Ely Security design.
- Code will supersede neither architecture nor ADRs silently; divergence requires an update.

## Navigation

[← Repository README](../README.md) · [Next: Product Vision →](product/vision.md)
