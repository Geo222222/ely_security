# Product Page Specifications

**Status:** Accepted for V1 architecture  
**Version:** 1.0

## Global shell

Persistent:
- Ely logo/product identity;
- workspace/site;
- global mode;
- current time window/live state;
- infrastructure health;
- attention count;
- operation count;
- global search/command palette;
- Elyandra drawer.

Left navigation order:
`Command, Universe, Assets, Wireless, Threats, Investigations, Plays, Operations, Evidence, Automations, Policies, Elyandra, Infrastructure, System`.

Exactly one primary route is active.

## Command

Purpose: “What requires attention now?”

Sections:
- posture statement with evidence;
- newly changed assets/relationships;
- active critical/high Findings;
- active Investigations;
- running/waiting Operations;
- source coverage/health;
- Elyandra briefing.

No vanity KPI without operator action relevance.

## Universe

Purpose: “What exists and what is communicating?”

Views:
- Live;
- External;
- Connections;
- Geographic;
- Timeline;
- Replay.

Universe consumes a server-side projection, not raw provider events.

Node states:
- known/new/changed/suspicious/contained/offline;
- type/zone;
- coverage/confidence.

Edges:
- direction;
- current activity;
- bytes/flows;
- protocol/service summary;
- first/last seen;
- novelty/finding indicator.

Inspector:
`Overview | Connections | Processes | Services | Findings | History | Evidence`.

Renderer: Sigma.js/Graphology initial implementation behind Ely adapter.

## Assets

Inventory with:
- identity confidence;
- interfaces/IP history;
- zone;
- owner/labels;
- endpoint enrollment;
- services;
- software/process evidence where available;
- Findings;
- relationship history;
- coverage.

## Wireless

- managed SSIDs/APs;
- clients;
- BSSID/channel/security;
- recognized/new;
- signal/activity history when source supports it;
- wireless coverage;
- config change;
- monitor sensor health.

Never imply packet visibility that is unavailable.

## Threats

Two explicit tabs:
- Findings;
- Provider Alerts.

This prevents upstream alert noise from becoming product truth.

Finding detail shows evidence, confidence, coverage, affected entities, investigation/Play status.

## Investigations

Workspace:
- hypotheses;
- evidence FOR/AGAINST;
- timeline;
- selected assets/relationships;
- operations;
- determinations;
- disposition.

Elyandra appears context-bound to the case.

## Plays

Tabs:
`Quick Actions | Investigate | Defense | Assess | Running | History | Builder`.

Preview before run:
- purpose;
- target/scope;
- mode;
- risk;
- steps;
- tools;
- approval;
- expected evidence;
- rollback/verification.

## Operations

Live execution cockpit.

Each Operation shows:
- stage;
- Play/version;
- Elyandra/tool activities;
- policy decisions;
- approvals;
- worker;
- timing;
- evidence count;
- failure/retry state.

## Evidence

Search/filter:
- source;
- asset;
- investigation;
- type;
- time;
- hash;
- sensitivity.

Supports raw event view, artifact details, session/PCAP retrieval/export, provenance chain.

## Automations

Rule builder around:
`WHEN → IF → THEN → VERIFY → COOLDOWN`.

Simulation mode replays historical events without actions.

## Policies

- modes/risk classes;
- target scopes;
- roles/capabilities;
- approval rules;
- worker permissions;
- retention;
- outbound/model data policy.

Policy simulator answers “would this be allowed and why?”

## Elyandra

- operator conversations;
- current context;
- activity/tool ledger;
- model/provider status;
- memory controls;
- evaluations;
- proposed Plays/automations.

## Infrastructure

Nodes/sources:
- Core;
- collectors;
- Zeek;
- Suricata;
- session/PCAP;
- endpoints;
- workers;
- NATS;
- PostgreSQL;
- OpenSearch.

Each exposes health, version, lag/capacity, last evidence.

## System

- users/roles;
- updates;
- backups;
- certificates;
- storage/retention;
- diagnostics;
- license/notices;
- audit verification.
