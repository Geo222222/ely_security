# Product Vision

**Status:** Accepted for V1 architecture  
**Version:** 1.0

[← Architecture Book](../README.md) · [Next: System Architecture →](../architecture/system-architecture.md)

## Mission

Ely Security is a local-first, AI-native security operations environment for homes, developers, small organizations, and eventually managed environments that need continuous security understanding without staffing a conventional SOC.

The initial proving ground is a small site with untrusted upstream connectivity, valuable development systems, multiple network/wireless device classes, and a requirement for continuous evidence-backed awareness.

## End state

An operator opens Ely and understands within seconds:

- which sites, networks, zones, and assets are present;
- which assets are known, new, changed, suspicious, contained, or offline;
- which internal and external endpoints are communicating;
- what changed during a selected time window;
- what Ely can and cannot currently observe;
- which observations triggered attention;
- what Elyandra is investigating and why;
- which evidence supports or contradicts each conclusion;
- which Plays can be safely executed;
- what authorization is required before an action occurs;
- exactly what Ely itself has done.

The long-term product supports multiple workspaces and sites. V1 proves the architecture locally with one operator/site while preserving those boundaries.

## Differentiation

Ely is not another alert table, a Security Onion skin, or an LLM attached to a shell.

Its owned product layer is:

1. **Security Graph** — canonical temporal model of the environment.
2. **Universe** — live/replayable visual operating surface.
3. **Evidence Engine** — provenance and artifact integrity.
4. **Identity Resolver** — stable assets from uncertain network identities.
5. **Detection/Correlation** — provider alerts become evidence, not truth.
6. **Investigations** — hypotheses with evidence for and against.
7. **Elyandra** — contextual reasoning over product-owned APIs.
8. **Plays** — stateful workflows.
9. **Policy Engine** — deterministic authority boundary.
10. **Execution Gateway** — typed, isolated action path.
11. **Operations/Audit** — visibility into what humans, AI, policy, and tools did.

## V1 technology direction

- native sensor composition: Zeek + Suricata;
- Arkime optional for indexed session/PCAP;
- Ely Node Agent + osquery for endpoint query;
- PostgreSQL authoritative operational state and temporal graph;
- NATS JetStream event backbone;
- OpenSearch optional/rebuildable search projection;
- Go authority/control services;
- TypeScript/Next.js Command Center;
- Elyandra as separate TypeScript agent process;
- dedicated isolated assessment worker VM.

Security Onion and Malcolm are reference/optional integration profiles, not product foundations.

## Non-goals for V1

- rebuild packet decoders or mature IDS engines;
- build a generic SIEM;
- build billing/reseller/enterprise SSO;
- give an LLM unrestricted root/SSH access;
- treat visible upstream devices as assessment targets;
- automatically exploit arbitrary systems;
- introduce Kubernetes or a microservice fleet before evidence requires it.

## Product principles

### Evidence before confidence
Unknown and insufficient-evidence are valid outcomes.

### Changes matter
Deltas from known state and baseline drive attention.

### Human agency
The operator controls scope and consequential action. Elyandra cannot manufacture authority.

### Security survives AI failure
Collection, deterministic detection, retention, policy, and non-AI automations continue if Elyandra/model access fails.

### Local-first
Core visibility, evidence, enforcement, and operation do not require Ely cloud services.

### Sovereignty
Every upstream dependency has an Ely contract and an exit path.

## First operational milestone

An operator can:

1. deploy Core + sensor;
2. open Universe and see real authorized assets/relationships;
3. select an asset and inspect internal/external relationships;
4. drill relationship → flow/session → evidence/PCAP where available;
5. see coverage limitations rather than false “all clear”;
6. ask Elyandra what changed in the last hour;
7. receive an evidence-grounded answer;
8. launch Unknown Device and Suspicious Outbound Connection Plays;
9. see policy, execution, artifacts, and verification in Operations;
10. prove an out-of-scope active action is denied;
11. restart Core and reconstruct correct state.

## Empirical qualification remaining

These are measurements, not missing architecture decisions:

- exact qualified hardware sizing;
- events/sec and storage growth on representative traffic;
- PCAP retention duration for chosen disk capacity;
- wireless chipset/driver qualification;
- Arkime vs direct packet-storage performance for the first appliance;
- OpenSearch threshold at which it becomes required rather than optional.

## Known risks

- telemetry volume can overwhelm useful visual aggregation;
- prompt injection/untrusted telemetry can influence reasoning if context boundaries fail;
- asset identity remains probabilistic without agent/strong signals;
- GPL/ELv2/open-core redistribution must be continuously reviewed;
- a sensor cannot observe traffic outside its vantage point.

[← Architecture Book](../README.md) · [Next: System Architecture →](../architecture/system-architecture.md)
