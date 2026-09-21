# Canonical Operator Workflows

**Status:** Accepted  
**Version:** 1.0

## 1. Unknown device

```text
Asset appears
 → identity resolver marks NEW/UNRESOLVED
 → automation opens Finding
 → Unknown Device Investigation
 → passive identity/history evidence
 → optional approved safe discovery
 → Elyandra summarizes evidence
 → operator recognizes OR policy escalates
 → disposition + asset state
```

No active scan is automatic merely because an unknown device exists.

## 2. Suspicious outbound connection

```text
New/abnormal relationship
 → correlate Zeek/Suricata/DNS/endpoint
 → Finding
 → Investigation
 → destination/history/process evidence
 → hypothesis + evidence for/against
 → optional containment request
 → Policy approval
 → Execution
 → verify connection/state
```

## 3. Endpoint containment

```text
Investigation determines containment warranted
 → launch Contain Endpoint Play
 → resolve immutable asset/interface target
 → policy R4 decision
 → approval
 → worker/provider action
 → verification query
 → record rollback path/evidence
```

## 4. Authorized exposure assessment

```text
Operator enters ASSESS
 → selects existing AssessmentScope
 → launches Exposure Assessment
 → policy validates exact targets
 → ExecutionGrant
 → assessment worker performs typed probes
 → structured results/evidence
 → Findings created separately
```

Discovering another host does not expand AssessmentScope.

## 5. “What changed in the last hour?”

```text
UI/Elyandra Query
 → Graph delta projection
 → asset/relationship/finding/config/source changes
 → retrieve supporting evidence
 → structured grounded answer
 → links into Universe/Investigations/Evidence
```

## 6. Source outage

```text
Collector heartbeat/lag fails
 → SourceHealth DEGRADED/UNAVAILABLE
 → coverage changes
 → Command attention
 → Finding if policy threshold met
 → no claims of “no activity” for uncovered interval
```

## 7. Automation simulation

Operator creates automation and runs it against historical event stream.

Simulation produces:
- triggers that would fire;
- predicates;
- proposed actions;
- policy outcomes;
- no real execution.

Activation requires validation and authorization.
