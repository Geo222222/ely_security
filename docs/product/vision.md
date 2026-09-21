# Product Vision

**Status:** Review  
**Version:** 0.1

[← Architecture Book](../README.md) · [Next: System Architecture →](../architecture/system-architecture.md)

## Mission

Ely Security is an AI-native security operations environment for homes, developers, small organizations, and eventually managed environments that need continuous security understanding without staffing a conventional SOC.

The initial proving ground is a local environment with untrusted upstream connectivity, valuable development systems, multiple wireless/device classes, and a need for continuous network awareness.

## End state

An operator should be able to open Ely Security and understand, within seconds:
- which sites, networks, zones, and assets are present;
- which assets are known, new, changed, suspicious, contained, or offline;
- which internal and external endpoints are communicating;
- what changed over any selected time window;
- which observations triggered attention;
- what Elyandra is investigating and why;
- what evidence supports each conclusion;
- which Plays can be safely executed;
- what authority is required before an action occurs.

The long-term product is local-first and productized for multiple workspaces and sites. V1 is deliberately single-operator and local-first.

## Differentiation

Ely Security is not another alert table and not an LLM wrapper around shell access.

Its differentiated layer is:
1. **Security Graph** — canonical temporal model of the environment.
2. **Universe** — live/replayable visual operating surface over that graph.
3. **Evidence model** — provenance for observations, conclusions, and actions.
4. **Elyandra** — contextual operator reasoning over selected product state.
5. **Plays** — stateful workflows that branch based on evidence.
6. **Policy Engine** — deterministic authority boundary independent of the model.
7. **Operations view** — live observability into what the AI and tools are doing.

## Non-goals for V1

- Reimplement a packet capture engine.
- Reimplement Zeek or Suricata.
- Build a new general-purpose SIEM.
- Build billing, subscriptions, reseller administration, or enterprise SSO.
- Give an LLM unrestricted root/SSH access.
- Treat all campground/upstream devices as authorized assessment targets.
- Automatically exploit arbitrary systems to determine whether they are vulnerable.

## Product principles

### Evidence before confidence
Unknown is a valid answer. Confidence without traceable evidence is not.

### Changes matter
The product emphasizes deltas from known state and baseline, not just static inventory.

### Human agency
The operator controls scope and consequential actions. Elyandra can recommend and execute within explicit policy, but cannot manufacture authority.

### Security survives AI failure
Collection, detection, retention, and deterministic enforcement remain operational if Elyandra or the model provider is unavailable.

### Local-first
Core monitoring and evidence access must work without requiring Ely Security cloud services.

## Success criteria for the first operational milestone

An operator can:
1. open Universe and see the authorized local environment populate from real telemetry;
2. select an asset and see observed internal/external relationships;
3. drill from relationship → flow/session → supporting evidence;
4. ask Elyandra what changed during a time window;
5. receive an answer whose claims link to evidence;
6. launch an Unknown Device or Suspicious Outbound Connection investigation Play;
7. see each Play step, tool call, policy decision, result, and artifact;
8. confirm that denied/out-of-scope actions cannot be executed by Elyandra.

## Open questions

- Exact V1 hardware topology and capture method.
- Whether Security Onion, Malcolm, or a thinner Zeek/Suricata/Arkime stack is the default packaged deployment.
- Graph persistence technology after workload benchmarking.
- Endpoint telemetry provider(s) for V1.
- Wireless sensor hardware and driver constraints.

## Known risks

- High telemetry volume can make an attractive UI misleading if aggregation semantics are weak.
- AI prompt injection and untrusted telemetry can influence model reasoning.
- Network identity is probabilistic when MAC randomization, NAT, VPNs, and ephemeral addressing are present.
- Upstream project licenses constrain how components may be redistributed or embedded.

[← Architecture Book](../README.md) · [Next: System Architecture →](../architecture/system-architecture.md)
