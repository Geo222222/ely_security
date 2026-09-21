# Execution Gateway and Worker Architecture

**Status:** Accepted  
**Version:** 1.0

## Decision

Security execution occurs outside Elyandra and outside the main control-plane process.

High-risk assessment tooling runs in a dedicated Linux/Kali VM or equivalent strong isolation boundary with an Ely Worker Agent.

No persistent inbound SSH path is required for normal operation.

## Components

### Execution Gateway
Go control-plane service.

Responsibilities:
- validate PolicyDecision;
- mint short-lived ExecutionGrant;
- select eligible worker;
- bind exact action parameters/targets;
- dispatch;
- stream bounded status/output;
- enforce timeout/cancellation;
- persist result/evidence.

### Worker Agent
Go daemon inside worker node.

Responsibilities:
- mutual TLS authentication;
- advertise tool capabilities/versions;
- validate grant signature/expiry/audience;
- map typed action to registered tool adapter;
- enforce local resource limits;
- capture stdout/stderr/artifacts;
- return structured result.

### Tool Adapter
Code-owned mapping from typed parameters to safe process invocation.

Normal adapters use execve-style argument arrays, never shell string concatenation.

## ExecutionGrant

Contains:
- grant_id;
- worker audience;
- action type/version;
- exact targets;
- exact validated parameters/hash;
- policy decision ID;
- issued/expiry;
- nonce;
- maximum runtime/resources;
- artifact policy;
- signature.

Grant is one-shot unless explicitly defined otherwise.

## Worker profiles

### Diagnostic worker
Low-risk utilities; can run on managed node where appropriate.

### Defensive worker
Network/endpoint response integrations.

### Assessment worker
Dedicated VM, typically Kali-based, isolated from the control plane.

### Sensor worker
Packet/network tools requiring privileged interface access; not automatically permitted to perform assessment.

## Kali decision

Kali is a replaceable tool distribution, not an architectural dependency.

Ely depends on typed capability names such as:
- network.discovery;
- service.enumeration;
- tls.inspect;
- dns.inspect;
- packet.capture;
- endpoint.collect.

Each capability may map to Nmap, tshark, dig, etc., but product logic never depends on command-line text.

## Network isolation

Assessment worker:
- management channel only to Execution Gateway/NATS endpoint as required;
- assessment egress limited to authorized target ranges when technically feasible;
- no access to Ely signing keys/database;
- no automatic access to operator home directories/secrets;
- snapshots/rebuild supported.

## Secret handling

Workers request short-lived secret handles when an approved action requires credentials.

Secrets are:
- never placed in prompts;
- not stored in normal logs;
- scoped to target/action;
- revoked/expired after operation.

## Output limits

Tool outputs have:
- maximum bytes;
- structured parser;
- raw artifact reference when needed;
- timeout;
- process-tree kill on cancellation;
- redaction policy.

## Failure behavior

- lost worker heartbeat → operation UNKNOWN/FAILED_NEEDS_VERIFY, never assumed successful;
- timeout → kill process tree and verify target state where applicable;
- duplicate dispatch → one-shot grant/idempotency key prevents duplicate state change;
- worker compromise → cannot mint grants or alter policy.

## Acceptance tests

- raw arbitrary command rejected;
- modified action parameters invalidate grant;
- expired/replayed grant rejected;
- worker cannot act outside target set;
- command-injection strings remain literal argv values;
- worker loss does not mark action successful.
