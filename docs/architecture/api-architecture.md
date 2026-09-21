# API Architecture

**Status:** Accepted  
**Version:** 1.0

## Contract styles

Ely uses three communication styles for distinct purposes.

### External/product API
HTTPS REST + JSON with OpenAPI schemas.

Used by:
- Command Center;
- integrations;
- operator automation;
- read/query workflows.

### Internal service/node RPC
gRPC + Protocol Buffers.

Used by:
- collectors;
- node agents;
- worker agents;
- high-integrity typed internal operations.

Remote RPC uses mutual TLS. Local privileged communication may use Unix domain sockets.

### Eventing
NATS JetStream with versioned protobuf/JSON-compatible event envelopes.

### Realtime UI
Server-Sent Events for ordered status/event feeds by default. WebSocket is reserved for bidirectional interactive surfaces that truly require it.

## No GraphQL in V1

The product's security and temporal queries benefit from explicit, auditable endpoints and bounded query cost. REST/query endpoints remain easier to authorize and observe.

## API domains

```text
/workspaces
/sites
/assets
/relationships
/flows
/findings
/investigations
/evidence
/plays
/play-runs
/operations
/policies
/approvals
/automations
/infrastructure
/elyandra
/audit
```

## Identity

Every request context contains authenticated:
- user/service/node ID;
- workspace;
- roles/capabilities;
- session/credential identity;
- request ID/trace ID.

Client-supplied workspace/site identifiers are authorization inputs, not trusted facts.

## Query boundaries

Graph/search APIs use bounded:
- time ranges;
- page/cursor limits;
- traversal depth;
- result sizes.

Expensive exports become asynchronous Operations.

## Elyandra tool API

Elyandra uses a strict subset of product APIs exposed as typed tools.

Examples:
- `get_asset(asset_id)`
- `get_relationships(asset_id, window)`
- `search_evidence(query, scope, window)`
- `open_investigation(...)`
- `propose_play(...)`
- `run_play(play_id, target_ids, params)`
- `explain_policy(action_request)`

No generic SQL/shell endpoint exists.

## Versioning

- API path/major version for breaking public changes;
- protobuf package version for breaking RPC/event contracts;
- additive fields preferred;
- deprecation period before removal.

## Error model

Structured errors include:
- code;
- safe message;
- correlation ID;
- retryability;
- relevant resource IDs;
- no secret/provider raw error leakage.

## Idempotency

Mutation APIs that can be retried accept an idempotency key.

Approval, execution, containment, and Play launch are idempotent by contract.

## Acceptance tests

- unauthorized cross-workspace ID returns no information;
- traversal limits cannot be bypassed;
- duplicate mutation key does not duplicate action;
- Elyandra API has no raw command/SQL surface;
- API/audit request IDs correlate end-to-end.
