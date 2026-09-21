# Deployment Architecture

**Status:** Accepted  
**Version:** 1.0

## Deployment unit

The product deployment unit is an **Ely Site**.

A Site contains one Core Node and zero or more Sensor, Endpoint, and Worker nodes.

## V1 topology

```text
                       Operator Browser
                              │ HTTPS
                              ▼
                        ELY CORE NODE
 ┌────────────────────────────────────────────────────────┐
 │ Command API / UI                                      │
 │ Policy / Plays / Investigations / Automations         │
 │ Security Graph / Evidence metadata                    │
 │ PostgreSQL │ NATS JetStream │ optional OpenSearch     │
 └──────────────────────┬─────────────────────────────────┘
                        │ mTLS/gRPC
          ┌─────────────┼───────────────────┐
          ▼             ▼                   ▼
      SENSOR NODE   ENDPOINT NODES     ASSESSMENT WORKER
   Zeek/Suricata     Ely Agent +         Kali VM +
    packet/session     osquery          Ely Worker
```

## Core Node

Supported production OS target: current stable Linux distribution.

Core Node is not a packet-analysis appliance by requirement. Sensor processes may be colocated only in Small/Lab profile.

Core Node owns:
- authoritative PostgreSQL;
- NATS;
- evidence metadata/blob store;
- policy/control services;
- UI/API;
- Elyandra gateway;
- optional OpenSearch.

## Profiles

### LAB
Core + sensor services may share one host.
Assessment worker remains isolated VM where active testing is enabled.

### SMALL
Core node + one dedicated gateway/sensor + assessment VM.

### DISTRIBUTED
Core/management separated from sensor/search/storage nodes.

### MULTI-SITE
Each Site keeps local collection/policy capability. A future federation plane aggregates metadata/management without making local defense cloud-dependent.

## Containers

Application services may be packaged as OCI containers, but containers are deployment units, not security boundaries for hostile assessment tools.

Databases and NATS may run containerized in LAB/SMALL; production packaging must preserve durable volumes, health, backup, and upgrade semantics.

## Service topology

V1 is a **modular monolith plus isolated infrastructure services**, not dozens of microservices.

Recommended deployables:
1. `ely-core` Go process containing domain modules;
2. `ely-web` Next.js/TypeScript UI;
3. `elyandra` isolated agent process;
4. PostgreSQL;
5. NATS;
6. optional OpenSearch;
7. collectors/workers on their nodes.

Modules can split later only for scaling/failure reasons.

## Node enrollment

1. operator creates one-time enrollment token;
2. node generates keypair locally;
3. Core authenticates enrollment and issues node certificate;
4. node gets immutable node_id/site_id/capabilities;
5. token is invalidated;
6. all remote RPC uses mTLS.

Certificate rotation is automatic; revoked nodes cannot reconnect.

## Upgrades

- signed release manifest;
- preflight storage/schema compatibility;
- database backup before destructive migration;
- rolling node-agent upgrade where possible;
- Core migration with explicit rollback boundary;
- version compatibility window for node protocols.

## Air-gap/local-first

Core monitoring/control supports operation without Internet.

External enrichment feeds degrade visibly. Product updates and rules can be imported as verified offline bundles.

## Acceptance tests

- Internet outage does not break local observation/policy;
- Core restart reconstructs current graph from database;
- sensor disconnection is visible;
- old compatible node agent reconnects during upgrade window;
- revoked node certificate cannot publish events.
