# ADR-0009 — Native upstream sensors are the default stack

**Status:** Accepted  
**Date:** 2026-09-21

## Context
Security Onion is valuable but ELv2/product/API coupling conflicts with Ely's sovereignty goal. Malcolm proves useful independent composition.

## Decision
The default Ely sensor profile is composed from upstream primitives:

- Zeek for passive metadata;
- Suricata for IDS/NSM;
- Arkime optional for indexed sessions/PCAP;
- osquery through Ely Node Agent for endpoint query;
- OpenSearch optional for search.

Security Onion and Malcolm are supported/reference profiles, not mandatory foundations.

## Consequences
Ely must own packaging, normalization, health, configuration, and upgrade integration that an integrated distribution would otherwise provide.
