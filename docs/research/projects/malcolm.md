# Project Audit — Malcolm

**Decision:** Learn from heavily; selectively reuse Apache-2.0 code/patterns after file-level review. Optional interoperability.  
**Sovereignty target:** Reference, not required runtime.  
**Evidence date:** 2026-09-21.

## Verified facts

CISA/INL Malcolm:
- accepts PCAP, Zeek logs, and Suricata alerts;
- normalizes, enriches, and correlates traffic data;
- uses OpenSearch Dashboards and Arkime for analysis;
- deploys as a composition of software containers;
- is licensed Apache 2.0.

## High-value mechanisms

### Normalization pipeline
Malcolm proves that heterogeneous network-security outputs can be normalized/enriched before analyst use.

Ely will study:
- field normalization;
- Community ID/correlation strategies;
- GeoIP/OUI enrichment;
- user asset/network-segment enrichment;
- JA4/fingerprint enrichment;
- container boundaries.

### Composition
Malcolm demonstrates a non-Security-Onion composition around open primitives. This is directly aligned with Ely sovereignty.

## What Ely will not inherit

- OpenSearch document structure as domain truth;
- dashboard-driven product architecture;
- container topology as immutable product topology;
- all enrichments by default regardless of privacy/cost.

## Reuse policy

Apache-2.0 makes selective reuse possible, but code reuse is not automatic.

For each reused file/module:
- record commit;
- preserve notice;
- isolate it behind Ely contracts;
- add Ely-owned tests;
- prefer concept reimplementation when the upstream code drags unnecessary dependencies.

## Ely destination

Patterns learned from Malcolm feed:
- Telemetry Gateway;
- Enrichment Pipeline;
- Session/PCAP Adapter;
- container deployment profile.

## Source

- https://github.com/cisagov/Malcolm

## Remaining empirical work

Run Malcolm against a representative PCAP/Zeek/Suricata sample and compare:
- fields produced;
- enrichment cost;
- OpenSearch footprint;
- Arkime integration behavior.

The architecture decision to own normalization does not depend on the benchmark.
