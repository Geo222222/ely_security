# Threat Model

**Status:** Review  
**Version:** 0.1

[← Domain Model](domain-model.md) · [Next: Security Graph →](security-graph.md)

## Protected assets

- source code and intellectual property;
- credentials, signing keys, tokens, browser sessions, and secrets;
- development and personal endpoints;
- security telemetry and packet evidence;
- Ely Security control-plane authority;
- configuration, policies, and allowlists;
- audit/evidence integrity;
- availability of monitoring.

## Trust boundaries

1. Upstream/campground/ISP network is untrusted.
2. Managed local networks are monitored but not assumed uncompromised.
3. Telemetry payloads are untrusted input.
4. Model/provider output is untrusted until validated.
5. OpenCode/Elyandra process is not an enforcement boundary.
6. Execution workers/Kali are isolated from the control plane.
7. Third-party security stacks are separate administrative/data boundaries.
8. Browser/UI is not trusted to authorize actions by itself.

## Threat classes

### Network adversary
Unauthorized device, hostile upstream peer, malicious destination, spoofing, scanning, interception attempts, lateral movement.

### Compromised managed endpoint
An authorized device may become malicious while retaining valid network identity.

### Physical loss/tampering
Portable/home/RV deployments face theft, powered-on device access, removable media, and sensor tampering.

### Supply-chain compromise
Dependencies, container images, rules, model plugins, MCP servers, packages, or upstream projects may be compromised.

### Agent/tool abuse
Prompt injection, malicious telemetry text, poisoned evidence, unsafe tool arguments, shell injection, confused-deputy behavior, excessive authority.

### Insider/operator error
Wrong target, overly broad scope, accidental containment, destructive Play, secret exposure.

### Evidence attacks
Log deletion, timestamp manipulation, sensor spoofing, replay, artifact substitution, provenance loss.

## Required controls

- explicit workspace/site/network authorization scope;
- fail-closed policy for state-changing actions;
- typed tool adapters; avoid model-constructed shell where a typed primitive exists;
- execution isolation (VM/container/sandbox as appropriate);
- short-lived grants and credentials;
- no long-lived root SSH credential exposed to the model;
- network egress controls for workers where practical;
- append-only audit ledger;
- evidence hashes and source identity;
- secret scanning and no raw operational evidence in Git;
- signed/verified release pipeline as the product matures;
- dependency/SBOM/vulnerability management;
- separation of passive observation from active assessment;
- confirmation/approval gates based on action class;
- sanitization/context separation for untrusted telemetry shown to models.

## OpenCode-specific boundary

OpenCode documents that its permission system is not a sandbox. Ely Security therefore treats OpenCode permissions as operator UX and defense-in-depth only. Policy enforcement and worker isolation must exist outside the agent process.

## CAI-specific lesson

The archived CAI project contains valuable agent/guardrail research but also documented command-injection advisories in agent tools. Ely Security will not copy its command execution boundary. We study patterns, tests, and failures; execution is reimplemented around typed actions, policy decisions, and isolation.

## Security testing boundary

ASSESS mode operates only on explicit authorized target sets. Discovery of an unknown/upstream device does not create authorization to test it. Scope expansion requires an operator/policy change.

## Open questions

- Hardware-backed key strategy for local appliance deployments.
- Root of trust for sensor identities.
- Remote administration design.
- Secure update/TUF-style strategy.
- Evidence encryption and retention defaults.

[← Domain Model](domain-model.md) · [Next: Security Graph →](security-graph.md)
