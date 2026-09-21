# System Architecture

**Status:** Review  
**Version:** 0.1

[← Product Vision](../product/vision.md) · [Next: Domain Model →](domain-model.md)

## Architectural style

Ely Security is a local-first, event-driven security control plane. Mature sensors remain authoritative for what they observe; Ely normalizes their outputs into product-owned contracts.

The logical architecture is modular. This does **not** require every module to be an independently deployed microservice in V1. Deployment boundaries are earned by isolation, scaling, failure-domain, or lifecycle requirements.

## Planes

### 1. Observation plane
Collects network, endpoint, wireless, infrastructure, and tool telemetry.

Candidate integrations:
- Zeek for protocol-neutral network observations.
- Suricata for detection and structured EVE events.
- Arkime or equivalent for indexed session/PCAP retrieval.
- Security Onion for integrated network/host visibility and analyst workflows.
- Endpoint agents/osquery where appropriate.
- Router/firewall/DNS/syslog sources.

### 2. Evidence plane
Stores immutable source observations and artifact metadata. Evidence records include content hash, source, sensor identity, collection time, observed time, parser/schema version, retention class, and access controls.

### 3. Knowledge plane
Builds the Security Graph and canonical asset/identity/relationship state. It distinguishes:
- observation;
- derived fact;
- hypothesis;
- determination.

### 4. Reasoning plane
Elyandra queries bounded product APIs. Model outputs are advisory until transformed into typed proposals. Untrusted telemetry is data, never instruction.

### 5. Orchestration plane
The Play Engine executes typed workflow state machines. It requests policy decisions before side effects and records every transition.

### 6. Enforcement/execution plane
A deterministic Policy Engine evaluates authority. An Execution Gateway sends approved, typed tasks to isolated execution nodes. Kali is a worker profile, not the control plane.

### 7. Experience plane
Command Center, Universe, Investigations, Operations, Evidence, Plays, and administration surfaces consume the same canonical APIs.

## Core components

### Telemetry Gateway
Receives adapter events, validates envelopes, assigns provenance, deduplicates where safe, and writes raw observations.

### Normalizers
Map upstream schemas to canonical Ely observations while preserving the original payload reference. Normalization is versioned and replayable.

### Asset/Identity Resolver
Correlates IP, MAC, hostname, DHCP, endpoint agent identity, user labels, certificates, and history without pretending uncertain identity is certain.

### Security Graph
Temporal graph of assets, interfaces, networks, zones, external endpoints, identities, relationships, findings, investigations, and evidence.

### Evidence Service
Content-addressed metadata and artifact access with retention and chain-of-custody fields.

### Detection/Correlation Service
Combines upstream detections, deterministic rules, baselines, and graph changes. It may create findings; it does not grant authority.

### Investigation Service
Tracks hypotheses, evidence for/against, timeline, observables, determinations, owner, and lifecycle.

### Elyandra Gateway
Provides scoped tools over product APIs. It does not expose arbitrary database credentials or unrestricted host shells.

### Play Engine
Runs versioned workflow definitions and records deterministic state transitions.

### Policy Engine
Evaluates actor, workspace, site, mode, target scope, action class, risk, approvals, and expiry. It returns permit/deny/require-approval with reason.

### Execution Gateway
Accepts only policy-approved typed actions, issues short-lived execution grants, dispatches to workers, enforces timeout/resource constraints, and captures output.

### Worker Nodes
Isolated execution environments. A Kali worker may expose approved security tools through typed adapters. Workers are replaceable and untrusted relative to the control plane.

### Audit Ledger
Append-only record of security-relevant control-plane actions: policy decisions, approvals, Play transitions, Elyandra tool calls, execution grants, and configuration changes.

## Canonical event envelope

Every normalized observation must carry at least:

```text
event_id
workspace_id
site_id
source_type
source_instance_id
source_event_id?
observed_at
ingested_at
schema_name
schema_version
raw_evidence_ref
integrity_hash
classification
payload
```

## Failure behavior

- **Elyandra unavailable:** telemetry, graph updates, deterministic detections, policy, and existing non-AI automations continue.
- **Security Onion unavailable:** adapters mark source degradation; other sources continue; no synthetic “healthy” state.
- **Graph unavailable:** raw evidence ingestion should spool within bounded limits; execution requiring graph scope resolution fails closed.
- **Policy unavailable:** state-changing execution fails closed.
- **Worker unavailable:** Play pauses/fails explicitly; no alternate worker is silently selected if scope/authority would change.
- **Clock skew:** record source and ingest clocks; flag material skew rather than rewriting evidence timestamps.
- **Schema drift:** quarantine incompatible events; do not silently discard fields.

## Deployment evolution

### V1 — Personal/local
One workspace, one site, local control plane, one or more sensors/workers.

### V2 — Multi-site
Same workspace, multiple sites, site-local collectors/workers, central operator experience.

### V3 — Productized multi-workspace
Strict tenant isolation, workspace-scoped identity/RBAC, per-site data residency/retention options, fleet lifecycle.

No V1 service should assume a global singleton for workspace, site, network, or worker.

## Dependencies

Domain Model, Threat Model, Security Graph, Play Engine, Upstream Adoption Research.

## Open questions

- Event bus technology and persistence.
- Graph storage implementation.
- Artifact storage implementation.
- V1 endpoint agent.
- Packaging strategy for third-party stacks.

[← Product Vision](../product/vision.md) · [Next: Domain Model →](domain-model.md)
