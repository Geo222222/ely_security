# Detection and Correlation Architecture

**Status:** Accepted  
**Version:** 1.0

## Principle

Provider alerts are observations. Ely Findings are product-level security conclusions requiring evidence and lifecycle.

## Inputs

- Suricata alerts/anomalies;
- Zeek observations;
- endpoint observations;
- asset/identity changes;
- graph relationship changes;
- threat-intelligence matches;
- policy/config changes;
- source-health events;
- baseline deviations.

## Pipeline

```text
Provider Alert / Observation
          ↓
Normalization
          ↓
Deterministic Detection Rules
          ↓
Correlation / Baseline Context
          ↓
Finding Candidate
          ↓
Finding + evidence + confidence
          ↓
Investigation / Automation
```

## V1 rule engine

Implemented in Go with typed rule definitions.

Supported:
- event match;
- temporal count/rate;
- sequence;
- asset/zone conditions;
- relationship novelty;
- baseline deviation;
- source combination;
- suppression/cooldown.

No arbitrary code inside rule definitions.

## Finding fields

- finding_id;
- type;
- title;
- severity;
- confidence;
- affected entities;
- first/last seen;
- evidence;
- detection methods;
- state;
- disposition;
- source coverage;
- recommended next Play.

## Severity vs confidence

Severity answers potential impact.

Confidence answers evidentiary support.

A critical-severity/low-confidence finding is valid and displayed distinctly from high-confidence critical.

## Correlation

Correlation keys:
- asset;
- identity;
- external endpoint/domain;
- Community ID/flow;
- process;
- finding family;
- time window.

Provider-specific IDs remain evidence attributes.

## Baselines

V1 uses transparent statistical baselines, not opaque ML.

Track:
- destination recurrence;
- service/port recurrence;
- volume ranges;
- time-of-day behavior;
- asset appearance patterns;
- relationship novelty.

Robust statistics and configurable minimum history prevent “first day” false certainty.

## Threat intelligence

TI is enrichment, not truth.

Every match records:
- feed/provider;
- indicator;
- feed timestamp;
- confidence/reputation;
- match method.

A stale/revoked indicator can be re-evaluated without rewriting the original observation.

## Elyandra role

Elyandra may synthesize hypotheses/explanations and suggest correlation, but deterministic Finding state is stored independently.

Model-generated detection can create a `MODEL_CANDIDATE` requiring a typed evaluation path, never an unqualified alert.

## Acceptance tests

- same Suricata alert does not create duplicate Finding on replay;
- severity and confidence vary independently;
- baseline absence produces UNKNOWN, not anomaly;
- TI match keeps provider/timestamp;
- provider alert dismissal does not erase raw evidence.
