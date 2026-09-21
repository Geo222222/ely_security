# Automation Engine

**Status:** Accepted  
**Version:** 1.0

## Purpose

Continuously evaluate security state and start bounded workflows without turning Elyandra into an uncontrolled daemon.

## Rule model

```text
WHEN <typed event/state change>
IF   <deterministic predicates>
THEN <typed actions>
VERIFY <postconditions>
COOLDOWN <duration/key>
```

Automation definitions are versioned data, not arbitrary executable code.

## Triggers

- canonical event;
- finding lifecycle;
- asset state transition;
- source health change;
- time schedule;
- Play completion/failure;
- policy/config change.

## Predicates

V1 deterministic predicates:
- equality/set membership;
- numeric/time comparison;
- CIDR/network membership;
- graph relationship existence;
- baseline threshold;
- asset/zone/tag;
- finding severity/confidence/state;
- rate/count window.

Model-assisted classification is an explicit step producing a typed classification result. It cannot directly bypass policy.

## Actions

Automation can:
- create/update Finding;
- create Investigation;
- launch OBSERVE/INVESTIGATE Play;
- request approval;
- notify operator;
- tag/change non-security metadata;
- request DEFEND/ASSESS action through normal Policy Engine.

Automation does not receive special authority.

## Example

```text
WHEN AssetStateChanged(to=NEW, zone=TRUSTED_LAN)
IF not recognized within 120s
THEN create Investigation
     launch UnknownDeviceInvestigation
VERIFY investigation has identity evidence
COOLDOWN asset_id: 1h
```

## Loop prevention

- causation/correlation IDs;
- maximum chain depth;
- cooldown keys;
- dedupe keys;
- rule cannot re-trigger itself from its own bookkeeping event unless explicit;
- rate budget per workspace/site.

## Determinism

The same ordered event stream + same rule versions produces the same deterministic automation actions, excluding explicitly labeled external/model classifications.

## Safety

Every state-changing action still passes Policy Engine.

Automation may request approval; it cannot synthesize one.

## Acceptance tests

- event replay does not duplicate idempotent action;
- runaway rule hits chain/rate limit;
- model classification failure degrades to UNKNOWN;
- rule version used is recorded;
- policy denial is visible and does not retry forever.
