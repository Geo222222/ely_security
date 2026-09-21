# Storage and Retention Architecture

**Status:** Accepted  
**Version:** 1.0

## Storage roles

### PostgreSQL — authoritative operational state
Stores:
- workspaces/sites/networks/zones;
- assets/interfaces/identity assertions;
- temporal Security Graph nodes/edges;
- evidence metadata;
- findings/investigations;
- Plays/PlayRuns;
- policies/approvals;
- operations/audit indexes;
- configuration.

### Evidence BlobStore — authoritative immutable artifacts
V1: local content-addressed filesystem.
Future: S3-compatible/object backend through the same interface.

### NATS JetStream — durable transport, not archive
Stores events long enough for delivery/recovery. It is never the only copy of evidence or canonical state.

### OpenSearch — optional rebuildable search projection
Used for high-volume free-text/event hunting and aggregations when PostgreSQL alone is insufficient.

Deleting OpenSearch must not destroy Ely truth.

### Session/PCAP provider
Arkime/Suricata/alternate packet storage may own high-volume packet blobs. Ely owns references/provenance and can export case evidence into BlobStore.

## PostgreSQL graph design

V1 graph stays relational.

Core tables:
- graph_nodes;
- graph_edges;
- node_identifiers;
- edge_observations;
- temporal_state;
- evidence_links.

Use:
- UUIDv7 primary keys;
- time partitioning for high-volume observation/flow tables;
- GiST/GIN/B-tree indexes as appropriate;
- recursive CTEs for bounded traversal;
- materialized/current-state projections.

A graph database is not introduced until measured traversal workloads demonstrate PostgreSQL cannot meet latency/cost targets.

## Retention defaults

Defaults are policy profiles and remain configurable.

### Audit/policy/investigation
Preserve indefinitely by default for the V1 local installation unless operator explicitly configures retention.

### Asset/identity/relationship summaries
Preserve long-term. Rolled-up temporal history remains after detailed events expire.

### Detailed canonical observations/flows
Default hot window: 30 days where disk allows.

### OpenSearch projection
Default 14 days hot, rebuildable from retained canonical/evidence sources where available.

### Full packet capture
Ring-buffer semantics. Default capacity is disk-percentage based rather than a promised number of days.

Watermarks:
- 80% evidence/capture volume: pressure warning;
- 90%: aggressive rotation of unprotected packet data;
- 95%: critical; preserve case/hold evidence and stop lower-priority capture before corrupting core state.

### NATS
Bounded by age and bytes; default event recovery window targets 72 hours for local operation, with acknowledged durable consumers.

## Rollups

Before detailed flow expiry, Ely maintains relationship summaries:
- first/last seen;
- counts;
- bytes;
- protocol/service distribution;
- destination recurrence;
- baseline statistics;
- source coverage.

Rollup is derived state and can be recomputed within source retention.

## Backup

### Required
- PostgreSQL logical/physical backup;
- product configuration;
- keys/identity metadata;
- evidence metadata;
- protected case artifacts.

### Optional/large
- full packet ring;
- rebuildable OpenSearch indices;
- ephemeral NATS streams.

Backups are encrypted and manifest-hashed.

## Restore

Restore procedure validates:
1. database schema/migration version;
2. key availability;
3. evidence blob reconciliation;
4. node identity;
5. search projection rebuild status.

## Acceptance tests

- delete OpenSearch → core product remains correct and can rebuild search;
- crash during artifact write does not create valid metadata for partial blob;
- retention never deletes LEGAL_HOLD/CASE evidence;
- packet pressure cannot consume database/system partition;
- database restore reconciles missing blobs visibly.
