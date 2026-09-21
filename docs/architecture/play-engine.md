# Play Engine

**Status:** Accepted  
**Version:** 1.0

[← Security Graph](security-graph.md) · [Next: Page Stack →](../product/page-stack.md)

## Definition

A Play is a versioned, typed, durable workflow:

```text
Trigger → Resolve Scope → Observe → Gather Evidence → Evaluate
        → Branch → Request/Act → Verify → Record → Close/Rollback
```

Scripts may exist behind registered ToolAdapters but are not the workflow abstraction.

## Runtime

Play Engine is a Go module in Ely Core.

Durable state is PostgreSQL. NATS carries wakeups/events/results; NATS is not the workflow source of truth.

On Core restart, runs resume from persisted state.

## Classes

- OBSERVE;
- INVESTIGATE;
- DEFEND;
- ASSESS.

## Definition

A Play records:
- play_id/version/hash/publisher;
- purpose/class/required mode;
- typed inputs;
- scope constraints;
- preconditions;
- steps/branches;
- action risk;
- policy requirements;
- timeouts;
- failure/retry semantics;
- verification;
- rollback/compensation;
- expected evidence.

## Step types

- graph/evidence query;
- source/provider query;
- deterministic condition;
- Elyandra classification;
- branch;
- approval request;
- typed worker action;
- wait for observation;
- verify;
- create/update Finding/Investigation;
- rollback/compensate.

## Policy

Before every side effect, the Play Engine emits an ActionRequest.

Policy returns:
`PERMIT | DENY | REQUIRE_APPROVAL`.

A permit yields an exact short-lived ExecutionGrant through Execution Gateway.

## Approval semantics

Approvals bind:
- Play/action;
- resolved target set;
- parameters/constraints;
- approver;
- expiration;
- allowed use count.

Default interactive approval is one-shot and short-lived. V1 UI defaults to 10 minutes for R3–R5 requests; policy may shorten it. Longer reusable approvals require explicit policy, not a UI checkbox.

## Retry semantics

### Read/idempotent
May retry with bounded exponential backoff.

### State-changing with confirmed failure-before-effect
May retry according to adapter contract.

### State-changing with unknown outcome
Never blindly retry. State becomes `VERIFY_REQUIRED`; a verification step determines target state before continuation.

## Dynamic Plays

Elyandra may propose a temporary Play using registered primitives.

Before execution:
- schema validation;
- scope resolution;
- version/hash assigned;
- policy evaluation;
- operator preview when required.

Text cannot introduce a new executable primitive.

## Publishing/signing

### Built-in Plays
Versioned in source and covered by signed Ely release manifest.

### Local Plays
Stored with workspace publisher identity, content hash, revision history, and audit. No public Play marketplace in V1.

A modified Play receives a new version/hash.

## Initial Plays

- Unknown Device Investigation
- Suspicious Outbound Connection
- Unexpected Service
- Endpoint Triage
- Exposure Assessment
- Contain Endpoint

## Run state

`QUEUED | RUNNING | WAITING_APPROVAL | WAITING_EVIDENCE | VERIFY_REQUIRED | VERIFYING | SUCCEEDED | FAILED | CANCELLED | ROLLED_BACK`.

Each step persists:
- state;
- attempt;
- inputs hash;
- policy decision;
- worker/tool;
- evidence;
- timing;
- output/result.

## Acceptance tests

- Core restart resumes correctly;
- same idempotency key cannot duplicate containment;
- unknown side-effect result requires verification;
- Play edit changes hash/version;
- dynamic Play cannot invent raw shell tool;
- approval for Asset A cannot be reused for Asset B.

[← Security Graph](security-graph.md) · [Next: Page Stack →](../product/page-stack.md)
