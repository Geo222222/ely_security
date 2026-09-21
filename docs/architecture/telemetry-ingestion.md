# Telemetry Ingestion Architecture

**Status:** Accepted  
**Version:** 1.0

## Purpose

Convert heterogeneous, untrusted security telemetry into replayable Ely observations without losing raw provenance.

## Pipeline

```text
Provider
  ↓
Ely Collector / Adapter
  ↓
Raw evidence persist
  ↓
Canonical validation + normalization
  ↓
NATS JetStream
  ↓
┌──────────────┬───────────────┬──────────────┐
Graph Projector Detection/Correlation Search Projector
  ↓              ↓               ↓
PostgreSQL     PostgreSQL     OpenSearch(optional)
```

Raw source persistence occurs before or atomically with acknowledgement whenever the source can be replayed.

## Provider classes

- network metadata: Zeek;
- IDS/NSM: Suricata;
- session/packet: Arkime or alternate provider;
- endpoint: Ely Node Agent/osquery;
- infrastructure: firewall/router/DNS/DHCP/syslog;
- wireless: AP/controller/monitor sensor;
- execution: Ely Worker Agent;
- product internal events.

## Transport

### Local
Unix domain socket, local file tail, or loopback gRPC depending on provider.

### Remote node
gRPC over mutual TLS between enrolled Ely nodes.

### Internal durable bus
NATS JetStream.

NATS subjects are product-owned, for example:
- `ely.obs.network.v1`
- `ely.obs.endpoint.v1`
- `ely.alert.provider.v1`
- `ely.source.health.v1`
- `ely.operation.result.v1`

Provider names never define the subject taxonomy.

## Canonical envelope

```text
event_id          UUIDv7
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
trace_id?
payload
```

## Raw evidence

Original provider output is retained or referenced before normalization.

Examples:
- original Zeek JSON line;
- original Suricata EVE object;
- osquery result set;
- router syslog record;
- worker command result;
- Arkime session reference.

Normalization records:
- adapter name/version;
- source schema/version when available;
- transformation version;
- validation warnings.

## Delivery semantics

Ely assumes at-least-once delivery.

Therefore:
- `event_id` is stable;
- adapters preserve provider event IDs when possible;
- consumers are idempotent;
- duplicates are observable but do not duplicate canonical state;
- events can arrive late/out of order.

Exactly-once is not an architecture assumption.

## Backpressure

Collectors use bounded local spool storage.

When downstream is unavailable:
1. spool locally;
2. report source degradation/backlog;
3. preserve order where meaningful;
4. drop only under an explicit retention/pressure policy;
5. record a DataLossEvent if dropping occurs.

Silent loss is prohibited.

## Schema evolution

Schemas use explicit versioning.

Breaking input change:
- adapter quarantines incompatible records;
- source health changes to DEGRADED;
- sample payload and validation error become evidence;
- no best-effort field guessing in the authoritative path.

## Security

Telemetry is untrusted data.

Controls:
- maximum record size;
- parser limits;
- content-type validation;
- no template/code evaluation from event values;
- structured model context escaping;
- tenant/site assignment from authenticated collector identity, not event body;
- replay protection where remote transport requires it.

## Acceptance tests

- duplicate event produces one canonical state change;
- late event updates temporal history correctly;
- malformed source payload is quarantined;
- NATS outage spools and recovers;
- raw evidence can be fetched from a canonical observation;
- model/prompt-like strings in telemetry cannot create tool calls.
