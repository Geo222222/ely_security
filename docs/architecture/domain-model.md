# Domain Model

**Status:** Accepted  
**Version:** 1.0

[← System Architecture](system-architecture.md) · [Next: Threat Model →](threat-model.md)

## Purpose

This vocabulary prevents upstream tools, UI components, and model prompts from inventing incompatible representations.

## Administrative hierarchy

`Workspace → Site → Network → Zone`

- **Workspace** — tenant/ownership/authorization boundary.
- **Site** — physical or logical deployment location.
- **Network** — routable/broadcast environment.
- **Zone** — trust/functional partition.

## Core entities

### Asset
Stable Ely-tracked logical/physical device or compute unit.

State:
`KNOWN | NEW | CHANGED | SUSPICIOUS | CONTAINED | OFFLINE | RETIRED`.

### Interface
Time-bounded network-facing interface of an Asset.

### ObservedIdentifier
MAC/IP/hostname/DHCP ID/agent key/certificate/cloud ID etc. Identity is resolved through evidence; IP is never identity by itself.

### ExternalEndpoint
Observed destination/source outside managed Asset inventory.

### Relationship
Temporal typed association between graph nodes.

### Flow
**Canonical Ely network conversation aggregate.**

Fields include direction, tuple, protocol/application, bytes/packets, first/last seen, involved entities, and evidence refs.

### SessionReference
**Provider-specific session/evidence reference** such as Arkime or Zeek source context. It may support one or more canonical Flows and does not replace Flow.

### ServiceInstance
Observed listening/communicating service:
- asset/interface;
- transport/port;
- application/protocol;
- process ref when known;
- first/last seen;
- evidence.

### ProcessInstance
Observed process scoped to an Asset and boot/runtime context:
- provider process ID;
- executable/hash/path metadata;
- parent;
- user-account observation;
- start/end;
- evidence.

OS PID alone is never globally stable identity.

### PrincipalObservation
Observed endpoint account/user identity from telemetry. V1 does **not** attempt to create a universal human-person identity from endpoint usernames.

Human Ely `User` identity is a separate authentication domain.

### Observation
Immutable source statement.

### DerivedFact
Deterministically computed claim with derivation metadata.

### Hypothesis
Revisable explanatory claim with evidence for/against.

### Alert
Provider/rule notification.

### Finding
Ely security-relevant condition with severity, confidence, evidence, lifecycle.

Severity:
`INFO | LOW | MEDIUM | HIGH | CRITICAL`.

Confidence:
`LOW | MEDIUM | HIGH | CONFIRMED` plus numeric/internal method metadata where useful.

Severity and confidence are independent.

### Investigation
Structured reasoning case.

### Evidence / Artifact
Immutable provenance record / material evidence object.

### Play / PlayRun
Versioned workflow definition / one execution.

### Action
Typed query or side-effect request.

### PolicyDecision
`PERMIT | DENY | REQUIRE_APPROVAL`.

### ExecutionGrant
Short-lived capability bound to exact action/target/parameters.

### Operation
Operator-visible unit of work spanning Play/Elyandra/policy/tools.

## Epistemic model

```text
OBSERVATION → DERIVED FACT → HYPOTHESIS → DETERMINATION
```

No automatic promotion across classes.

## Time

Relationships, identities, services, processes, and assignments are temporal.

Minimum relevant fields:
`first_seen, last_seen, valid_from, valid_to, observed_at, ingested_at`.

Current state is a projection of history.

## Identity uncertainty

Resolver supports competing candidates/confidence and explicitly handles DHCP churn, randomized MAC, NAT, VPN, multiple interfaces, sleep/offline, duplicate hostnames, and ephemeral compute.

[← System Architecture](system-architecture.md) · [Next: Threat Model →](threat-model.md)
