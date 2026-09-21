# Policy Engine

**Status:** Accepted  
**Version:** 1.0

## Decision

Ely implements its own deterministic typed policy evaluator in Go.

V1 does not embed a general scripting language, Rego, JavaScript, or LLM inside the authority path.

## Purpose

Answer one question:

> May this actor perform this typed action against this exact scope under the current mode and approvals?

## Inputs

```text
actor
workspace
site
role/capabilities
operating_mode
action_type
action_risk
target_set
target_authorization
play_id/version?
operation_id?
current_approvals
time
policy_version
context_facts (bounded, typed)
```

## Output

`PERMIT | DENY | REQUIRE_APPROVAL`

plus:
- decision_id;
- matched rules;
- reason codes;
- exact target scope;
- expiry;
- approval requirements;
- policy hash/version.

## Operating modes

### OBSERVE
Allowed:
- telemetry read;
- evidence read;
- passive collection;
- health queries.

### INVESTIGATE
Adds:
- approved non-destructive discovery;
- endpoint diagnostic collection;
- bounded network probes explicitly marked safe.

### DEFEND
Adds defensive state change:
- block/contain;
- kill/quarantine where provider supports it;
- disable credential/session;
- configuration remediation.

Risk-based approval applies.

### ASSESS
Adds active security testing only against explicit AssessmentScope.

ASSESS never treats visibility as authorization.

## Action risk classes

- R0 READ
- R1 PASSIVE_COLLECT
- R2 SAFE_DIAGNOSTIC
- R3 REVERSIBLE_CHANGE
- R4 DISRUPTIVE_CHANGE
- R5 ACTIVE_ASSESSMENT
- R6 DESTRUCTIVE / credential-impacting / irreversible

R6 is denied by default in V1 unless a specifically implemented action has an explicit policy and human approval flow.

## Scope authorization

Targets resolve to immutable IDs at decision time.

A permit contains the resolved target IDs and network ranges. Workers cannot substitute a different hostname/IP after authorization.

DNS-based targets are resolved and pinned according to action semantics.

## Approval

Approval is a signed/audited control-plane object:
- approver;
- action/Play;
- target scope;
- allowed parameters;
- expiration;
- one-shot/reusable count.

“Approve this Play” never means approve arbitrary later commands.

## Evaluation rules

Order:
1. authenticate actor;
2. validate workspace/site;
3. validate mode;
4. classify action/risk;
5. resolve explicit target authorization;
6. apply deny rules;
7. evaluate required approvals;
8. apply permit rules;
9. produce immutable decision.

Explicit deny wins.

## Failure semantics

Policy service unavailable → state-changing execution fails closed.

Stale policy version → grant rejected.

Unresolved target identity → deny/require operator resolution.

## Storage and audit

Policy definitions/version history in PostgreSQL.

Every decision is appended to Audit Ledger and references policy hash.

## Acceptance/property tests

- agent cannot escalate its own mode;
- wildcard scope cannot arise from empty target list;
- deny overrides permit;
- expired approval cannot produce grant;
- target mutation invalidates grant;
- replaying same policy/input yields same decision;
- R5 outside AssessmentScope is always denied.
