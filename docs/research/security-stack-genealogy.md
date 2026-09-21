# Security Stack Genealogy

**Status:** Accepted for architecture direction  
**Evidence date:** 2026-09-21

## Conclusion

Ely will not be built on Security Onion as a product foundation. Security Onion is treated as an architectural case study and optional integration.

The useful pre-2022 lesson is decomposition:

```text
Capture → Protocol Metadata → Detection → Queue/Pipeline → Search
       → Endpoint Queries → Analyst Workflow → Cases
```

Ely keeps that decomposition while replacing product-level coupling with Ely-owned contracts.

## Historical baseline

Security Onion 2.3 was already a composition of upstream engines and product-specific integration. In 2021 Security Onion 2.3 incorporated Elastic 7.11.2 after Elastic's licensing change. Security Onion's 2022 announcement then established ELv2 for Security Onion components and introduced the enterprise-feature direction.

This means “start before 2022” is useful as an **architectural decomposition exercise**, not a safe licensing shortcut. Historical Security Onion code is not assumed reusable merely because it predates a later announcement. Any copied historical file would require commit-level license provenance.

## Capability lineage

| Capability | Historical/industry primitive | Ely decision |
|---|---|---|
| packet acquisition | libpcap/AF_PACKET, Suricata, Stenographer | use maintained capture provider behind Ely evidence contract |
| protocol/network metadata | Zeek / Suricata | integrate via versioned adapters |
| signature detection | Suricata | integrate as separate GPL process |
| full packet retrieval | Stenographer / Suricata / Arkime | prefer maintained provider; Arkime is current primary candidate |
| search/index | Elasticsearch historically | OpenSearch is Ely's optional Apache-2.0 search projection |
| durable transport | Redis/Logstash patterns | NATS JetStream for Ely event backbone |
| endpoint query | osquery | integrate behind Ely Endpoint contract |
| endpoint fleet control | Fleet/Elastic Agent patterns | Ely Node Agent owns contract; provider remains replaceable |
| case management | Security Onion/SIEM-specific | Ely builds Investigation Engine |
| analyst console | Kibana/SOC dashboards | Ely builds Command/Universe/Operations |
| orchestration/config | Salt/product-specific | Ely builds lifecycle/deployment management |
| AI operator | not part of historic baseline | Elyandra behind Ely APIs and policy |

## What we learn from Security Onion

### Keep
- separate sensor and management/search roles;
- local packet evidence close to the sensor;
- queueing between collection and indexing;
- ability to run standalone for small deployments and distributed for scale;
- network evidence plus endpoint evidence;
- hunt-to-PCAP-to-case workflow;
- operational health as a first-class surface.

### Change
- no vendor schema becomes canonical;
- no Elasticsearch/Elastic license becomes architectural destiny;
- no monolithic product API becomes mandatory;
- no single analyst console owns investigations;
- no AI process receives shell authority.

## What we learn from Malcolm

Malcolm demonstrates that Zeek, Suricata, Arkime, and OpenSearch can be composed independently of Security Onion and that normalization/enrichment is itself a valuable architectural layer.

Ely adopts that composition lesson but owns its event envelope, identity model, graph, evidence semantics, and UX.

## Packet capture decision

Google Stenographer demonstrated a valuable invariant: packet storage and sparse retrieval should be optimized separately from deep protocol analysis. The repository was archived in November 2022, so Ely does not choose Stenographer as a strategic runtime dependency.

Current Ely direction:
- Suricata may provide packet capture in small deployments;
- Arkime is the preferred session/PCAP integration candidate when indexed retrieval is required;
- the Evidence contract permits future Ely-native or third-party capture providers.

## Endpoint lineage

osquery remains a strong low-level endpoint query primitive. Fleet demonstrates scalable osquery fleet management, but Ely does not make Fleet's data model or paid/free boundaries canonical.

Ely Node Agent will eventually own:
- enrollment identity;
- secure transport;
- scheduled evidence collection;
- action/response capability;
- local health;
- osquery invocation where useful.

## Architectural outcome

The pre-2022 exercise yields a cleaner stack:

```text
                        ELY EXPERIENCE
             Command / Universe / Investigations
                              │
                        ELY CONTROL PLANE
       Graph / Evidence / Policy / Plays / Automations
                              │
                         NATS JETSTREAM
                              │
                      ELY ADAPTER CONTRACTS
          ┌───────────┼───────────┬────────────┐
          │           │           │            │
        Zeek       Suricata     Arkime       osquery
```

Security Onion and Malcolm become reference/integration profiles rather than owners of Ely.

## Sources

- https://blog.securityonion.net/2021/03/
- https://docs.securityonion.net/en/2.4/license.html
- https://docs.securityonion.net/en/2.4/architecture.html
- https://docs.securityonion.net/en/2.4/introduction.html
- https://github.com/cisagov/Malcolm
- https://github.com/google/stenographer
- https://github.com/zeek/zeek
- https://github.com/OISF/suricata
- https://github.com/arkime/arkime
- https://github.com/osquery/osquery

## Remaining empirical work

Only implementation measurements remain:
- packet capture provider throughput on target hardware;
- retention/storage growth;
- comparative Arkime vs direct-PCAP operational footprint.
