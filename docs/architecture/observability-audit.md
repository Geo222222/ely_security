# Observability and Audit Architecture

**Status:** Accepted  
**Version:** 1.0

## Two distinct systems

### Technical observability
Answers: is Ely healthy and performing correctly?

Signals:
- structured logs;
- metrics;
- distributed traces;
- health/readiness;
- queue depth;
- storage pressure;
- adapter lag;
- worker latency.

Ely uses OpenTelemetry-compatible instrumentation so backends remain replaceable.

### Security audit ledger
Answers: who/what changed security-relevant state and under what authority?

Audit is product evidence, not disposable logs.

## Audit events

Include:
- login/session elevation;
- user/role/policy changes;
- node enrollment/revocation;
- Play launch/cancel;
- approvals;
- policy decisions;
- ExecutionGrant issuance/use;
- worker actions/results;
- Elyandra tool requests;
- evidence export/deletion/hold;
- configuration/retention change.

## Audit integrity

Audit events are append-only in normal operation.

Each event includes previous-chain hash within a ledger partition so deletion/reordering is detectable. Periodic checkpoints are signed by a Core audit key.

This is tamper-evidence, not a claim of immutable hardware-backed logging.

## Trace correlation

One `trace_id/operation_id` connects:
UI → API → Elyandra/Play → Policy → Execution → Evidence.

## Health model

Every component reports:
`HEALTHY | DEGRADED | UNAVAILABLE | UNKNOWN`.

Product posture never converts UNKNOWN into HEALTHY.

## Acceptance tests

- one operation can be reconstructed across all services;
- deleting/reordering audit event breaks chain verification;
- logging outage does not silently disable audit;
- source lag appears in Infrastructure/Command;
- secret fields are absent from logs/traces.
