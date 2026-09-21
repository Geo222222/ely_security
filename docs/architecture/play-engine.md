# Play Engine

**Status:** Review  
**Version:** 0.1

[← Security Graph](security-graph.md) · [Next: Page Stack →](../product/page-stack.md)

## Definition

A **Play** is a versioned, typed, stateful security workflow. A shell script may be one implementation detail of a controlled step, but a Play is not a script.

```text
Trigger → Scope → Observe → Gather Evidence → Evaluate
        → Branch → Propose/Act → Verify → Record → Close/Rollback
```

## Play classes

- **Observe** — passive collection/query.
- **Investigate** — non-destructive diagnostics.
- **Defend** — containment/remediation under policy.
- **Assess** — active testing of explicitly authorized targets.

## Required Play definition fields

```text
play_id
version
name
class
purpose
required_mode
input_schema
scope_constraints
preconditions
steps
policy_requirements
timeouts
failure_policy
verification
rollback?
evidence_outputs
risk_class
owner
```

## Step types

- query graph;
- query evidence;
- invoke sensor/search integration;
- request Elyandra classification;
- deterministic condition;
- branch;
- request approval;
- invoke typed worker action;
- wait/observe;
- verify;
- emit finding;
- update investigation;
- rollback/compensate.

## Safety model

The Play Engine does not decide whether a side effect is authorized. It constructs an ActionRequest and asks the Policy Engine.

Policy input includes:
- actor/service identity;
- workspace/site;
- active operating mode;
- Play and version;
- target set;
- requested action;
- action risk class;
- current approvals;
- time/expiry;
- relevant policy facts.

The Policy Engine returns:
`PERMIT | DENY | REQUIRE_APPROVAL`.

A permit yields a short-lived ExecutionGrant. Workers cannot accept arbitrary “because Elyandra said so” execution.

## Dynamic Plays

Elyandra may propose a new Play or a temporary parameterized plan from approved primitives. Proposed Plays are data, not executable authority. They must:
1. validate against the Play schema;
2. use registered primitives;
3. resolve explicit scope;
4. pass policy;
5. preserve a version/hash;
6. be visible to the operator before consequential execution when policy requires it.

## Initial Play library

### Unknown Device Investigation
Correlate identity evidence, history, DHCP/network observations, passive behavior, known inventory, and optional approved non-destructive discovery.

### Suspicious Outbound Connection
Establish relationship history, destination context, initiating process when available, IDS evidence, baseline, and evidence for/against suspiciousness.

### Unexpected Service
Verify observation, determine owning asset/process, compare history, inspect exposure and policy, create finding if justified.

### Endpoint Triage
Collect bounded host/network evidence without remediation.

### Exposure Assessment
Against an explicitly authorized asset, enumerate approved exposure information and produce findings/evidence.

### Contain Endpoint
Defensive, high-impact Play requiring explicit policy/approval; verifies containment and provides rollback path.

## Idempotency and recovery

Every step has a stable execution key. On restart, the engine must distinguish:
- never started;
- started/unknown result;
- completed;
- failed;
- compensated.

State-changing steps require explicit idempotency/verification semantics.

## Operations UX

A running Play is observable:
`QUEUED → RUNNING → WAITING_APPROVAL → VERIFYING → SUCCEEDED|FAILED|CANCELLED|ROLLED_BACK`.

The operator sees each step, tool, policy decision, evidence output, duration, and Elyandra rationale.

## Open questions

- Workflow runtime implementation.
- Human approval expiry semantics.
- Distributed worker retry rules.
- Play signing/publishing model.

[← Security Graph](security-graph.md) · [Next: Page Stack →](../product/page-stack.md)
