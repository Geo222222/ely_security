# Upstream Adoption Research

**Status:** Accepted baseline  
**Version:** 1.0  
**Evidence date:** 2026-09-21

## Decision

Ely's default architecture is **not built on Security Onion or Malcolm**.

Ely composes current upstream primitives behind product-owned contracts:

- Zeek — passive network observation;
- Suricata — IDS/NSM, separate GPL process;
- Arkime — preferred optional indexed session/PCAP provider;
- osquery — endpoint query primitive behind Ely Node Agent;
- PostgreSQL — canonical operational state;
- NATS JetStream — durable event backbone;
- OpenSearch — optional rebuildable search projection.

Security Onion and Malcolm remain valuable reference implementations and optional integration profiles.

## Decision vocabulary

- **Depend** — direct runtime dependency behind Ely contract.
- **Integrate** — separate provider consumed through adapter.
- **Reuse selectively** — licensed code copied only after file/commit review.
- **Learn** — architecture/algorithms/UX/failure history only.
- **Reject** — intentionally not inherited.

## Security Onion — LEARN + OPTIONAL INTEGRATE

Verified:
- integrates Zeek, Suricata, packet capture, Elastic-based search/endpoint visibility, SOC/cases;
- separates manager/sensor/search roles;
- Security Onion and Elastic components in current 2.4 docs are ELv2;
- Connect API is a Pro feature from 2.4.120.

Ely takes:
- deployment-role lessons;
- sensor/search separation;
- queueing/recovery lessons;
- hunt-to-packet-to-case workflow;
- operational health concepts.

Ely does not take:
- SOC UI;
- canonical event/user/case schema;
- mandatory Connect API;
- ELv2 product core.

Detailed audit: [projects/security-onion.md](projects/security-onion.md).

## Malcolm — LEARN + SELECTIVE REUSE

Verified:
- accepts PCAP/Zeek/Suricata;
- normalizes/enriches/correlates;
- combines OpenSearch + Arkime;
- container composition;
- Apache 2.0.

Ely mines normalization/enrichment and deployment patterns while keeping its own schema and UX.

Detailed audit: [projects/malcolm.md](projects/malcolm.md).

## Arkime — OPTIONAL INTEGRATE

Apache 2.0. Preferred V1 candidate for session-indexed PCAP retrieval.

Ely owns `SessionProvider`; Arkime IDs/schema never become canonical.

Detailed audit: [projects/arkime.md](projects/arkime.md).

## Zeek — DEPEND/INTEGRATE

BSD licensed. Default passive observation engine.

Ely normalizes Zeek protocol/connection evidence and preserves raw provenance.

Detailed audit: [projects/zeek.md](projects/zeek.md).

## Suricata — DEPEND/INTEGRATE AS SEPARATE PROCESS

GPLv2. Default IDS/NSM provider. OISF documents redistribution obligations and commercial non-GPL licensing options.

Ely consumes EVE/PCAP outputs over process/data boundaries; provider severity is not final Ely severity/confidence.

Detailed audit: [projects/suricata.md](projects/suricata.md).

## OpenCode → Elyandra — EVOLVE

MIT licensed.

OpenCode explicitly states its permissions are not a sandbox. Ely therefore keeps agent/session/tool ergonomics but moves policy and execution authority outside the process.

Detailed audit: [projects/opencode-elyandra.md](projects/opencode-elyandra.md).

## CAI — LEARN ONLY

Archived 2026-08-28. Mixed MIT + research-use/proprietary licensing in final tree. Critical command-injection advisories exist.

Ely studies cyber-agent decomposition, evaluations, handoffs, guardrails, and failures. No production dependency.

Detailed audit: [projects/cai.md](projects/cai.md).

## Historical conclusion

The pre-2022 Security Onion exercise is documented in [security-stack-genealogy.md](security-stack-genealogy.md).

The useful lesson is the decomposition of capture, observation, detection, transport, search, endpoint, and analyst workflow—not copying an old distribution.

## Dependency source of truth

See [dependency-register.md](dependency-register.md).

## Empirical qualification remaining

Architecture is decided. Implementation spikes must measure:
- Zeek/Suricata event rate and CPU;
- packet retention/storage;
- Arkime footprint vs direct capture;
- PostgreSQL graph/search latency;
- point at which optional OpenSearch becomes necessary;
- target wireless hardware behavior.

## Primary sources

- https://docs.securityonion.net/en/2.4/license.html
- https://docs.securityonion.net/en/2.4/pro.html
- https://docs.securityonion.net/en/2.4/architecture.html
- https://blog.securityonion.net/2021/03/
- https://github.com/cisagov/Malcolm
- https://github.com/arkime/arkime
- https://github.com/zeek/zeek
- https://github.com/OISF/suricata
- https://suricata.io/gpl-faqs/
- https://github.com/anomalyco/opencode/security/policy
- https://github.com/aliasrobotics/cai
