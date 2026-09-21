# Project Audit — Arkime

**Decision:** Preferred optional session/PCAP provider behind Ely Evidence/Session contracts.  
**License:** Apache 2.0.  
**Sovereignty target:** S3 alternate provider before broad product distribution.

## Verified facts

Arkime is an open-source large-scale full-packet capture, indexing, and database system. It stores PCAP and indexes session metadata in OpenSearch/Elasticsearch. Its architecture separates capture, viewer/API, and search storage. The project exposes APIs for session information and packet retrieval.

## Why Ely wants it

The Security Graph should not hold every packet. Arkime offers a mature lower-level boundary:

```text
Universe relationship
    → canonical Flow
        → SessionReference
            → Arkime metadata
                → PCAP evidence
```

This preserves operator drill-down without forcing Ely to build high-volume capture/indexing immediately.

## Ely-owned abstraction

`SessionProvider`:
- find sessions by canonical selectors/time;
- fetch session metadata;
- retrieve bounded PCAP;
- return provider provenance;
- expose health/capacity.

Arkime IDs never become global Ely IDs.

## What Ely will learn

- sparse packet retrieval;
- session indexing;
- capture/viewer separation;
- linked session segments;
- search-backed metadata;
- bounded PCAP extraction.

## What Ely will not inherit

- Arkime's user model;
- Arkime session schema as canonical Flow;
- direct frontend coupling;
- mandatory OpenSearch as Ely's primary database.

## Exit strategy

Alternate providers may include:
- Suricata PCAP indexer/adapter;
- direct capture store;
- future Ely capture service.

## Source

- https://github.com/arkime/arkime

## Remaining empirical work

Benchmark session lookup + PCAP slicing under V1 traffic volume and disk constraints.
