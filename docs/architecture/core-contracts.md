# Core Contracts

**Status:** Accepted for V1 implementation  
**Version:** 1.0

This document defines the cross-module contracts that engineers implement before provider-specific behavior. Field types shown are logical; Protobuf/OpenAPI/Go definitions are generated from versioned schemas.

## Identifier policy

Canonical Ely resources use UUIDv7 unless an external protocol mandates otherwise.

Provider IDs are stored as provider-qualified attributes and never become Ely primary identifiers.

Required IDs include:

- `workspace_id`
- `site_id`
- `network_id`
- `zone_id`
- `asset_id`
- `interface_id`
- `event_id`
- `evidence_id`
- `finding_id`
- `investigation_id`
- `play_id`
- `play_run_id`
- `operation_id`
- `policy_decision_id`
- `execution_grant_id`
- `node_id`

## Canonical ObservationEnvelope

```text
ObservationEnvelope {
  event_id: UUIDv7
  workspace_id: UUID
  site_id: UUID
  source: SourceIdentity
  observed_at: Timestamp
  ingested_at: Timestamp
  schema: { name, version }
  classification: ObservationClass
  raw_evidence_ref: EvidenceRef
  integrity_hash: SHA256
  trace_id?: string
  payload: typed message
}
```

### Invariants

- `workspace_id/site_id` derive from authenticated collector identity, not untrusted payload.
- `observed_at` is preserved even when late.
- `ingested_at` is Core/collector controlled.
- every normalized payload retains raw evidence provenance;
- consumers assume at-least-once delivery.

## SourceIdentity

```text
SourceIdentity {
  source_type: enum
  source_instance_id: UUID
  node_id?: UUID
  provider: string
  provider_version?: string
  adapter: string
  adapter_version: string
  provider_event_id?: string
}
```

## AssetIdentityAssertion

```text
IdentityAssertion {
  assertion_id: UUID
  asset_id?: UUID
  identifier_type: enum
  identifier_value: string
  network_id?: UUID
  interface_id?: UUID
  confidence: Confidence
  method: string
  valid_from: Timestamp
  valid_to?: Timestamp
  evidence_refs: EvidenceRef[]
  competing_asset_ids?: UUID[]
}
```

Low-confidence assertions do not force asset merge.

## Flow

```text
Flow {
  flow_id: UUID
  site_id: UUID
  network_id: UUID
  src_entity_ref
  dst_entity_ref
  src_ip, src_port?
  dst_ip, dst_port?
  transport_protocol
  application_protocol?
  direction
  first_seen
  last_seen
  packets_in/out?
  bytes_in/out?
  community_id?
  source_refs[]
  evidence_refs[]
}
```

A provider session may support a Flow but cannot replace the canonical Flow identity.

## EvidenceRecord

```text
EvidenceRecord {
  evidence_id: UUID
  workspace_id
  site_id
  evidence_type
  source_identity
  observed_at?
  collected_at
  sha256
  size_bytes
  content_type
  sensitivity
  retention_class
  storage_locator
  parent_evidence_ids[]
  producer_ref?
  integrity_state
}
```

Payload is immutable after successful commit.

## Finding

```text
Finding {
  finding_id: UUID
  workspace_id
  site_id
  type
  title
  severity: INFO|LOW|MEDIUM|HIGH|CRITICAL
  confidence: LOW|MEDIUM|HIGH|CONFIRMED
  state
  affected_entity_refs[]
  first_seen
  last_seen
  evidence_refs[]
  detection_methods[]
  coverage_snapshot
  disposition?
  recommended_play_ids[]
}
```

Provider alert severity never maps automatically to `CONFIRMED`.

## Investigation

```text
Investigation {
  investigation_id
  scope
  state
  initiating_refs[]
  hypotheses[]
  timeline_refs[]
  evidence_refs[]
  operation_ids[]
  determinations[]
  disposition?
  owner_user_id?
}
```

## ActionRequest

```text
ActionRequest {
  action_request_id: UUID
  actor: ActorIdentity
  workspace_id
  site_id
  operating_mode
  action_type
  action_version
  risk_class
  target_refs[]
  parameters
  parameters_hash
  play_run_id?
  operation_id
  requested_at
}
```

Targets are canonical immutable resource IDs. Human-readable hostnames/IPs are parameters/evidence, not authority identifiers.

## PolicyDecision

```text
PolicyDecision {
  policy_decision_id
  action_request_id
  result: PERMIT|DENY|REQUIRE_APPROVAL
  policy_version
  policy_hash
  matched_rule_ids[]
  reason_codes[]
  resolved_target_refs[]
  required_approval?
  decided_at
  expires_at?
}
```

Same policy version + normalized input must evaluate deterministically.

## Approval

```text
Approval {
  approval_id
  approver_user_id
  policy_decision_id
  action_type
  target_refs[]
  parameter_constraints
  max_uses
  issued_at
  expires_at
  revoked_at?
}
```

Approval cannot broaden the ActionRequest.

## ExecutionGrant

```text
ExecutionGrant {
  grant_id
  policy_decision_id
  worker_node_id
  action_type
  action_version
  target_refs[]
  parameters_hash
  resource_limits
  issued_at
  expires_at
  nonce
  max_uses: 1
  signature
}
```

Workers reject:
- wrong audience;
- expired grant;
- reused nonce;
- parameter mismatch;
- target mismatch;
- invalid signature.

## ToolResult

```text
ToolResult {
  operation_id
  play_run_id?
  worker_node_id
  action_type
  started_at
  ended_at
  status: SUCCEEDED|FAILED|CANCELLED|UNKNOWN
  structured_output?
  stdout_evidence_ref?
  stderr_evidence_ref?
  artifact_refs[]
  verification_required: bool
  error_code?
}
```

`UNKNOWN` for state-changing actions always leads to verification, never implicit retry.

## UIContext

```text
UIContext {
  workspace_id
  site_id
  route
  time_window
  selected_entity_ids[]
  selected_relationship_ids[]
  investigation_id?
  operation_id?
  operating_mode
}
```

UIContext supplies relevance, not authority.

## SourceHealth

```text
SourceHealth {
  source_instance_id
  state: HEALTHY|DEGRADED|UNAVAILABLE|UNKNOWN
  last_observation_at?
  backlog_events?
  backlog_bytes?
  coverage_effects[]
  reason_codes[]
  observed_at
}
```

UNKNOWN is never rendered as healthy.

## Versioning

- additive fields are backward-compatible;
- required semantic changes create a new major contract version;
- adapters declare supported input/output contract versions;
- raw evidence enables re-normalization under newer adapters;
- old persisted events remain interpretable through schema registry/migrations.

## Contract qualification

Before an adapter/tool/provider is accepted it must pass:
- schema fixtures;
- malformed-input suite;
- duplicate/replay suite;
- provenance suite;
- workspace/site isolation suite;
- version compatibility suite.
