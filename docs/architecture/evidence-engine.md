# Evidence Engine

**Status:** Accepted  
**Version:** 1.0

## Purpose

Preserve what Ely observed, what tools produced, and what every conclusion/action relied upon.

## Data model

### EvidenceRecord
Metadata:
- evidence_id UUIDv7;
- workspace/site;
- evidence_type;
- source identity;
- observed/collected times;
- content hash;
- size;
- MIME/encoding;
- sensitivity;
- retention class;
- storage locator;
- parent/derivation refs;
- integrity state.

### Artifact
A material object such as:
- PCAP slice;
- JSON/log bundle;
- endpoint snapshot;
- extracted file;
- command output;
- screenshot/report;
- model evaluation artifact.

### EvidenceLink
Typed relation:
`SUPPORTS | CONTRADICTS | DERIVED_FROM | PRODUCED_BY | VERIFIES`.

## Storage

### Metadata
PostgreSQL is authoritative.

### Small structured payloads
Stored inline only below a bounded threshold and when appropriate.

### Large artifacts
Content-addressed evidence store:

```text
/var/lib/ely/evidence/sha256/ab/cd/<hash>
```

The backend is abstracted as `BlobStore`; future S3-compatible/object storage can replace local filesystem.

### Packet evidence
May remain with a SessionProvider such as Arkime. Ely stores an immutable provider-qualified reference and integrity/provenance metadata; bounded PCAP exports can become Ely artifacts when required.

## Integrity

SHA-256 is the baseline content digest for interoperability and evidence verification.

On ingest:
1. stream to temporary file;
2. hash while writing;
3. fsync;
4. atomically move into CAS path;
5. commit metadata.

Duplicate content may share blob storage while retaining separate EvidenceRecords.

## Immutability

Evidence payloads are append-only.

Corrections create new records/annotations. Metadata fields that affect meaning are versioned/audited rather than rewritten invisibly.

## Retention classes

- EPHEMERAL — operational/debug, hours-days;
- HOT — active investigations, default weeks;
- STANDARD — normal security evidence, policy-defined;
- CASE — preserved with investigation;
- LEGAL_HOLD — manual protected retention.

Retention acts on evidence blobs only when no surviving record/hold requires them.

## Confidentiality

Production deployments require encrypted storage.

V1 default:
- encrypted host volume is mandatory recommendation;
- TLS/mTLS in transit;
- secrets stored separately from evidence;
- evidence authorization is workspace/site/case scoped.

Future per-object envelope encryption is supported by BlobStore contract without changing evidence IDs.

## Chain of custody

For exported case evidence record:
- original hash;
- export hash;
- exporter actor;
- time;
- selection/query;
- source records;
- tool/version.

## Failure behavior

- hash mismatch → QUARANTINED, never silently consumed;
- storage full → ingestion health CRITICAL and retention pressure workflow;
- missing external packet provider → reference marked unavailable, not fabricated;
- database/blob mismatch → reconciliation job creates integrity finding.

## Acceptance tests

- same artifact verifies after restart/export;
- corrupted blob is detected;
- evidence used by an investigation cannot be deleted by ordinary retention;
- raw provider event can be traced from a finding;
- audit records survive artifact deduplication.
