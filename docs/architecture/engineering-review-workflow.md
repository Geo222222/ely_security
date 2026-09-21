# Engineering Review Workflow

**Status:** Accepted  
**Version:** 1.0

## Goal

Architecture documents are executable engineering contracts, not prose artifacts.

## Review sequence

### 1. Vocabulary review
Every entity and state must agree with the canonical domain model.

Reject:
- vendor-specific names leaking into Ely domain;
- overloaded terms;
- identifiers without lifecycle semantics.

### 2. Responsibility review
For each subsystem verify:
- responsibilities;
- non-responsibilities;
- owned state;
- commands/queries/events;
- failure behavior.

Two subsystems must not silently own the same canonical state.

### 3. Dependency/coupling review
Ask:
- Can this module be tested without its vendor dependency?
- Does it depend on an abstraction or a specific implementation?
- Is there a circular control path?
- Is synchronous coupling actually required?

### 4. Trust-boundary review
For every ingress/egress:
- authenticate source;
- validate schema;
- classify data as trusted/untrusted;
- define authorization;
- define secret exposure;
- define replay/injection behavior.

### 5. Failure-mode review
Evaluate:
- process crash;
- network partition;
- source outage;
- duplicate event;
- delayed event;
- schema drift;
- disk full;
- clock skew;
- corrupted evidence;
- model outage;
- policy outage;
- worker compromise.

### 6. Sovereignty review
Every external component receives:
- capability contract;
- license classification;
- exit strategy;
- alternate-provider story.

### 7. Product review
The architecture must map to visible operator behavior.

An engineer must be able to identify:
- what the operator sees;
- what state changes;
- what evidence is available;
- how an error is represented.

### 8. Testability review
Every important invariant needs a deterministic acceptance test.

Examples:
- denied action cannot reach a worker;
- replay reconstructs the same graph;
- adapter schema drift quarantines instead of dropping;
- hypothesis cannot be persisted as observation;
- expired grant is rejected.

### 9. Operational review
Define:
- health signals;
- logs/metrics/traces;
- backup/restore;
- migration;
- upgrade/rollback;
- capacity signal;
- alerting.

### 10. Implementation readiness
A subsystem is implementation-ready when an engineer can build its first conforming version without inventing architecture.

## Architecture severity levels

Review findings use:

- **A0 — Constitutional violation:** must be resolved before implementation.
- **A1 — Trust/data-loss risk:** blocks affected subsystem.
- **A2 — Contract ambiguity:** resolve before integration.
- **A3 — Optimization/ergonomics:** may follow after functional acceptance.

## Definition of accepted

A document is Accepted when:
- its owned state is explicit;
- interfaces are explicit;
- failure semantics are explicit;
- security invariants are testable;
- upstream dependencies are classified;
- remaining unknowns are empirical rather than architectural;
- cross-document terminology is consistent.
