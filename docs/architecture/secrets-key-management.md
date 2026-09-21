# Secrets and Key Management

**Status:** Accepted  
**Version:** 1.0

## Principle

Secrets are references in normal domain state, never values in prompts, logs, NATS events, or Git.

## Secret classes

- model/provider API credentials;
- integration credentials;
- endpoint/assessment credentials;
- TLS private keys;
- execution signing keys;
- backup encryption keys;
- external enrichment tokens.

## Secret store

V1 implements an Ely Secret Service in the Core.

Secret ciphertext + metadata may reside in PostgreSQL, but encryption keys do not.

Envelope model:
- random DEK per secret/version;
- authenticated encryption;
- DEK wrapped by site KEK;
- KEK sourced from OS protected key store/TPM where available;
- development profile may use an explicitly configured local master key with prominent degraded-security state.

Cryptographic algorithms come from established libraries; Ely does not implement primitives.

## Signing keys

ExecutionGrant signing keys are isolated from Elyandra and workers.

Key rotation supports overlapping verification window.

Node CA/private key receives stronger filesystem/TPM protection.

## Secret handles

A Play/worker receives a short-lived handle scoped to:
- action;
- target;
- secret purpose;
- expiry.

Where possible the Worker Agent obtains/injects the secret directly so Elyandra never sees it.

## Logging/redaction

Structured fields are marked sensitive.

Logger refuses known secret fields and applies redaction patterns as defense-in-depth. Redaction is not a substitute for not transporting secrets.

## Backup

Secrets are included only in encrypted backups whose key lifecycle is independent from the data being protected.

## Acceptance tests

- model context inspection contains no secret value;
- NATS capture contains no secret value;
- expired handle fails;
- rotating KEK preserves decryptability through migration;
- worker result cannot echo registered secret without redaction alert.
