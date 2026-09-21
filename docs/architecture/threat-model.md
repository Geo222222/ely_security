# Threat Model

**Status:** Accepted  
**Version:** 1.0

[← Domain Model](domain-model.md) · [Next: Security Graph →](security-graph.md)

## Protected assets

- source code/IP;
- credentials, keys, tokens, sessions, secrets;
- managed endpoints and networks;
- telemetry/packet evidence;
- control-plane authority;
- policies/allowlists;
- audit/evidence integrity;
- monitoring availability.

## Trust boundaries

1. Upstream/ISP/public Wi-Fi is untrusted.
2. Managed LANs are monitored, not assumed safe.
3. Telemetry is untrusted input.
4. Model output is untrusted until validated.
5. Elyandra is not an enforcement boundary.
6. Browser/UI cannot authorize by itself.
7. Collectors/nodes authenticate separately.
8. Assessment/response workers are isolated and untrusted relative to Core.
9. Third-party sensor/search systems are providers, not trust anchors.

## Threat classes

### Network adversary
Unauthorized device, spoofing, interception, malicious destination, lateral movement, hostile upstream peer.

### Compromised managed endpoint
Valid identity does not imply trustworthy behavior.

### Physical loss/tampering
Portable/small-site deployments face theft, powered-on access, storage removal, and sensor tampering.

### Supply chain
Dependencies, images, rules, models, packages, MCP/tools, updates.

### Agent/tool abuse
Prompt injection, poisoned telemetry, shell/argument injection, confused deputy, excessive authority.

### Operator error
Wrong target, broad scope, accidental containment, secret exposure.

### Evidence attack
Deletion, spoofing, timestamp manipulation, replay, artifact substitution, provenance loss.

## Mandatory controls

- explicit workspace/site/target scope;
- mTLS node identity;
- one-time enrollment;
- deterministic Policy Engine;
- typed actions/argv process execution;
- short-lived grants;
- isolated assessment VM;
- no model-held root SSH credential;
- worker egress restriction where practical;
- evidence hashes;
- append-only tamper-evident audit chain;
- encrypted production storage;
- secrets outside prompts/logs/events;
- signed update manifests + SBOM;
- passive observation separated from active assessment;
- model context separation for untrusted data.

## Root of trust

### Site CA
Core owns the Site node-identity CA/private material, protected by filesystem/OS key store and TPM where available.

### Enrollment
One-time token → node-generated keypair → Core-issued certificate → token invalidated.

### Execution signing
Separate signing key for short-lived ExecutionGrants. Elyandra/workers never possess it.

## Host/storage protection

Production Small profile requires/recommends full-disk encrypted Linux storage (for example LUKS-class protection) and secure boot/TPM where hardware supports it.

Ely's BlobStore/Secret Service contracts permit stronger per-object envelope encryption without schema changes.

## Remote administration

V1 Core does not require public Internet exposure.

Default:
- bind management to local/private interface;
- HTTPS;
- remote use through operator-controlled VPN/private overlay;
- no unauthenticated server mode.

Future OIDC federation is additive.

## Update trust

Signed release manifest, checksums, SBOM, pinned dependencies, offline verified bundles, backup before destructive migration.

See Supply Chain & Updates.

## OpenCode boundary

OpenCode states its permission system is not a sandbox. Ely uses those permissions only as UX/defense-in-depth.

## CAI lesson

CAI's archived runtime and critical command-injection advisories reinforce typed actions and external isolation. Its mixed licensing also makes it research-only.

## Security-testing boundary

ASSESS requires an explicit AssessmentScope. Discovery never expands authorization.

## Residual risks

- privileged sensor/worker compromise can falsify its own source evidence;
- physical compromise may defeat software controls if keys are accessible;
- coverage gaps can hide activity;
- model reasoning can still be wrong even when authority is constrained.

Ely surfaces these limits rather than claiming perfect detection.

[← Domain Model](domain-model.md) · [Next: Security Graph →](security-graph.md)
