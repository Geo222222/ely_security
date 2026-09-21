# Domain Model

**Status:** Review  
**Version:** 0.1

[← System Architecture](system-architecture.md) · [Next: Threat Model →](threat-model.md)

## Purpose

This vocabulary prevents upstream tools, UI components, and model prompts from inventing incompatible representations.

## Administrative hierarchy

`Workspace → Site → Network → Zone`

- **Workspace** — ownership/authorization boundary.
- **Site** — physical or logical deployment location.
- **Network** — routable/broadcast environment known to Ely.
- **Zone** — trust/functional partition within a network.

## Core entities

### Asset
A thing Ely intends to track: workstation, phone, router, server, camera, sensor, VM, container host, IoT device.

Identity is not reduced to an IP address.

Key state:
`KNOWN | NEW | CHANGED | SUSPICIOUS | CONTAINED | OFFLINE | RETIRED`

### Interface
Network-facing identity observed on an Asset. May include MAC, IP assignments, wireless properties, agent identity, and validity windows.

### ExternalEndpoint
Observed destination/source outside managed asset inventory. May later resolve to provider, domain, ASN, region, service, or known asset.

### Relationship
Temporal association between graph nodes. Examples:
- asset communicates_with external_endpoint;
- asset resolved domain;
- interface assigned_ip;
- finding affects asset;
- investigation examines relationship.

### Flow
Aggregated network conversation with direction, tuple, protocol/application metadata, bytes/packets, first/last seen, and evidence references.

### Session
Sensor-specific higher-level conversation representation (for example Arkime/Zeek). A session is evidence-backed and may support one or more canonical flows.

### Observation
Immutable statement from a source: “sensor X observed Y at time T.”

### DerivedFact
Deterministically computed claim from observations, with derivation metadata.

### Hypothesis
Revisable explanatory claim with evidence for and against.

### Finding
A security-relevant condition requiring awareness, investigation, or action. A finding is not automatically an incident.

### Alert
A notification/detection emitted by a sensor/rule. Alerts may support Findings.

### Investigation
Structured reasoning case: scope, hypotheses, evidence, timeline, determinations, owner, status.

### Evidence
Reference to an immutable observation or artifact plus provenance/integrity metadata.

### Artifact
Material evidence: PCAP slice, log bundle, extracted file, process snapshot, command output, screenshot, report.

### Play
Versioned workflow definition.

### PlayRun
One execution of a Play against a fixed authorized scope and policy context.

### Action
Typed requested side effect or query.

### PolicyDecision
`PERMIT | DENY | REQUIRE_APPROVAL` plus rule, reason, scope, expiry, and approval requirements.

### ExecutionGrant
Short-lived capability produced after policy authorization; consumed by the Execution Gateway/worker.

### Operation
Operator-visible unit of work spanning investigation, Play, Elyandra, and tool activity.

## Epistemic model

Ely must preserve the difference between:

```text
OBSERVATION → DERIVED FACT → HYPOTHESIS → DETERMINATION
```

A model-generated hypothesis cannot be stored as an observation. A determination records its evidence set and method.

## Identity confidence

Asset resolution produces confidence and competing candidates when needed. It must tolerate:
- DHCP churn;
- randomized MAC addresses;
- NAT;
- VPNs;
- multiple interfaces;
- sleeping/offline devices;
- shared hostnames;
- ephemeral containers.

## Time

Most domain entities are temporal. Relationships and identities use validity/observation windows rather than destructive overwrites.

Minimum temporal fields where relevant:
`first_seen, last_seen, valid_from, valid_to, observed_at, ingested_at`.

## Open questions

- Whether Flow and Session remain distinct persisted entities after implementation benchmarks.
- Canonical service/process identity representation.
- User/person identity scope for V1.
- Standard taxonomy for finding severity vs confidence.

[← System Architecture](system-architecture.md) · [Next: Threat Model →](threat-model.md)
