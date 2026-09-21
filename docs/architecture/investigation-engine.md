# Investigation Engine

**Status:** Accepted  
**Version:** 1.0

## Purpose

Turn observations/findings into structured, evidence-backed reasoning that humans and Elyandra can inspect and continue.

## Lifecycle

`OPEN → TRIAGE → INVESTIGATING → DETERMINED → REMEDIATING → VERIFYING → CLOSED`

Alternative terminal state: `CANCELLED`.

Reopening creates a new lifecycle transition; history is preserved.

## Investigation contains

- scope;
- initiating finding/event;
- owner/participants;
- timeline;
- observables;
- hypotheses;
- evidence for/against;
- operations/PlayRuns;
- determinations;
- recommended/approved actions;
- closure reason;
- residual risk.

## Hypothesis model

A hypothesis contains:
- statement;
- created_by;
- created_at;
- status;
- evidence_for[];
- evidence_against[];
- confidence;
- falsification criteria.

Statuses:
`PROPOSED | SUPPORTED | WEAKENED | REJECTED | CONFIRMED`.

“CONFIRMED” requires a determination rule or explicit human determination; an LLM confidence score alone is insufficient.

## Determination

Records:
- conclusion;
- determining actor/method;
- evidence set;
- applicable rule/play/version;
- confidence;
- known limitations.

## Timeline

Timeline events reference canonical event/evidence IDs rather than copying prose.

It combines:
- observed security activity;
- analyst/Elyandra reasoning events;
- policy decisions;
- Play steps;
- execution results.

## Relationship with findings

Alert → may create/support Finding.

Finding → may create/join Investigation.

Closing an Investigation does not delete the Finding. Finding disposition is explicit:
`TRUE_POSITIVE | BENIGN_EXPECTED | BENIGN_CHANGED | FALSE_POSITIVE | INCONCLUSIVE`.

## Relationship with Elyandra

Elyandra can:
- propose hypotheses;
- retrieve evidence;
- request Plays;
- explain evidence changes;
- draft determination.

Elyandra cannot silently mark its own hypothesis confirmed or close a high-impact investigation contrary to policy.

## Acceptance tests

- evidence can support and contradict same hypothesis;
- rejected hypothesis remains in history;
- closing investigation requires explicit disposition;
- every determination resolves to evidence;
- replay shows reasoning/action chronology.
