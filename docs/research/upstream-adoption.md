# Upstream Adoption Research

**Status:** Review  
**Version:** 0.1  
**Rule:** “Open source” does not mean “copy freely without license/design review.”

[← Page Stack](../product/page-stack.md) · [Next: ADRs →](../decisions/ADR-0001-local-first-control-plane.md)

## Decision vocabulary

- **Integrate** — operate upstream product and consume supported outputs/APIs.
- **Depend** — ship/use upstream component directly.
- **Learn from** — study architecture, UX, schemas, tests, and failure history; reimplement Ely-owned contract.
- **Do not inherit** — explicitly avoid an upstream boundary/pattern.
- **Evaluate** — unresolved pending prototype/license/performance review.

## Security Onion

### Verified capabilities
Security Onion combines network visibility, host visibility, intrusion detection, log management, and case management. Its documented sensor architecture uses Zeek, Suricata, and full packet capture; endpoint visibility uses Elastic Agent/osquery. SOC provides alerts, dashboards, hunt, cases, detections, and PCAP retrieval.

### What Ely uses
**Integrate / learn from**, not fork the UI.

Use it as a candidate telemetry/SOC substrate and fallback analyst console. Learn from its alert→hunt→PCAP→case workflow and distributed manager/sensor/search separation.

### Important constraint
Security Onion components and Elastic components use Elastic License 2.0. Its Connect API is documented as a Pro/enterprise feature. Therefore Ely must **not** architect itself around an assumption of a free production API. Adapters need alternative paths and a licensing review.

### Do not inherit
- SOC UI as Ely's product shell.
- Security Onion event schema as Ely's canonical domain.
- A hard dependency on Pro-only APIs.

## Malcolm (CISA)

### Verified capabilities
Malcolm ingests PCAP, Zeek logs, and Suricata alerts; normalizes/enriches/correlates network session data; uses OpenSearch Dashboards and Arkime; and is containerized. It enriches with GeoIP, OUI/vendor, user asset inventory, network segment names, JA4 and related metadata.

### What Ely uses
**Learn from heavily; evaluate integration.**

Malcolm is our strongest reference for:
- reproducible containerized network-analysis composition;
- normalization/enrichment pipelines;
- Zeek/Suricata/Arkime correlation;
- home/field deployment patterns;
- asset enrichment and protocol dashboards.

Its Apache-2.0 license makes code reuse more tractable than ELv2 components, but reuse still requires attribution/license tracking.

### Do not inherit
- OpenSearch document shape as Ely's domain model.
- dashboard-first operating experience.

## Arkime

### Verified capabilities
Arkime captures traffic, stores standard PCAP, indexes session metadata in OpenSearch/Elasticsearch, and exposes APIs for JSON session data and PCAP retrieval. Architecture separates capture, viewer, and search storage.

### What Ely uses
**Integrate/evaluate as the packet-session evidence boundary.**

Universe should normally render canonical flow relationships. When an operator drills deeper, Arkime-style session APIs provide the bridge to session metadata and PCAP evidence.

Learn from:
- session indexing;
- PCAP retention/retrieval;
- linked segments;
- central viewer/gateway patterns;
- threat-intelligence enrichment via WISE/Cont3xt concepts.

### Do not inherit
- packet/session store as canonical asset graph.

## Zeek

### Verified capabilities
Zeek is a passive network traffic analyzer. Its event engine converts packet streams into higher-level, policy-neutral events; default logs describe connections and application protocols.

### What Ely uses
**Depend/integrate.**

This observation-vs-interpretation separation aligns directly with Ely's epistemic model. Zeek observations are excellent source evidence for relationships, DNS, TLS, HTTP and connection history.

### Do not inherit
Zeek event identifiers as global Ely identities.

## Suricata

### Verified capabilities
Suricata EVE emits JSON for alerts, anomalies, metadata, files, flows, and protocol-specific records.

### What Ely uses
**Depend/integrate.**

Build a versioned EVE adapter. Preserve raw EVE evidence; normalize selected fields into canonical observations/alerts/flows.

### Do not inherit
Suricata alert severity as Ely's final finding severity/confidence.

## OpenCode → Elyandra

### Verified capabilities
OpenCode provides agent/session/tool infrastructure, custom tools/MCP, subagents, and allow/ask/deny permissions. Its own security policy explicitly states that the agent is not sandboxed and permissions are not security isolation.

### What Ely uses
**Fork/evolve the agent product layer already selected for Elyandra, while moving security authority outside it.**

Retain/use:
- conversation/session experience;
- provider abstraction;
- tool registration concepts;
- subagents;
- permission UX;
- client/server separation where useful.

Build separately:
- Security Graph tools;
- evidence query tools;
- Play proposal/run tools;
- Policy API;
- Execution Gateway;
- security-specific activity ledger;
- typed UI context.

### Do not inherit
- unrestricted shell as the security execution contract;
- “permission prompt = sandbox” assumption;
- unauthenticated or weakly protected server deployment.

## CAI (archived)

### Verified capabilities
CAI was an agentic cybersecurity framework with agents, tools, handoffs, MCP, multi-agent patterns, guardrails, and benchmarking. It is archived and explicitly warns against production security use. GitHub advisories include critical command-injection issues in agent tools.

### What Ely uses
**Research reference only.**

Study:
- cybersecurity-specific agent decomposition;
- handoff patterns;
- benchmark/evaluation approach;
- guardrail/prompt-injection research;
- failure/advisory history.

### Do not inherit
- production runtime dependency;
- archived command execution tools;
- unrestricted offensive autonomy;
- provider/agent assumptions without revalidation.

## Comparative adoption matrix

| Capability | Primary source/reference | Ely strategy |
|---|---|---|
| Passive protocol evidence | Zeek | Integrate |
| IDS/detection events | Suricata | Integrate |
| Session/PCAP evidence | Arkime / Security Onion | Evaluate/integrate |
| Integrated SOC/host telemetry | Security Onion | Integrate where licensing/deployment fits |
| Normalization/enrichment | Malcolm | Learn/reuse selectively |
| Agent UX/runtime | OpenCode/Elyandra | Evolve |
| Cyber-agent research | CAI | Learn only |
| Canonical security graph | Ely Security | Build |
| Universe | Ely Security | Build |
| Play Engine | Ely Security | Build |
| Policy/authority boundary | Ely Security | Build |
| Execution Gateway | Ely Security | Build |
| Audit/evidence linkage | Ely Security | Build |

## Required pre-implementation research

1. Prototype Security Onion data access available without Pro-only API assumptions.
2. Prototype Malcolm/Arkime session and PCAP retrieval.
3. Define adapter contracts using captured sample schemas.
4. Run license inventory for every candidate dependency.
5. Benchmark local hardware footprint for SO vs Malcolm vs thinner composition.
6. Threat-model OpenCode server/session integration.
7. Review upstream security advisories before pinning any version.

## Sources

This document was produced from official project documentation and repositories current as of 2026-09-21. Exact URLs are intentionally kept in ADR/research commit history and should be converted into a maintained dependency/source register during implementation.

[← Page Stack](../product/page-stack.md) · [Next: ADR-0001 →](../decisions/ADR-0001-local-first-control-plane.md)
