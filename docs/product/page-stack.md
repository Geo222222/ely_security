# Product Page Stack

**Status:** Review  
**Version:** 0.1

[← Play Engine](../architecture/play-engine.md) · [Next: Upstream Adoption →](../research/upstream-adoption.md)

## Shell

One persistent application shell:
- workspace/site selector;
- global search/command palette;
- operating mode indicator;
- sensor/system health;
- active operation count;
- alert/attention indicator;
- Elyandra drawer;
- contextual Play launcher.

Selection context survives navigation where meaningful. Elyandra receives explicit UI context objects, not scraped screen text.

## Routes

### /command
Mission control. Posture, attention queue, active investigations, operations, environment health, recent changes, Elyandra briefing.

### /universe
Primary live visual surface.

Tabs/views:
`Live | External | Geographic | Connections | Timeline | Replay`

Inspector tabs:
`Overview | Connections | Processes | Services | Findings | History | Evidence`

Visual semantics are based on state and direction; color is never the only carrier of meaning.

### /assets
Inventory, identity confidence, posture, interfaces, services, ownership, history, evidence.

### /wireless
Authorized wireless environment: SSIDs, APs, clients, channels/radio observations where sensors support them, trust zones, identity changes, findings.

### /threats
Correlated detection stream. Separates source alerts from Ely findings. Filters by site, asset, confidence, severity, source, status, and time.

### /investigations
Cases with hypotheses, evidence for/against, observables, timeline, operations, determinations, notes, and closure reason.

### /plays
`Quick Actions | Defense | Assess | Investigate | Running | History | Builder`

Every Play preview shows target, scope, tools/primitives, expected impact, authority requirement, verification, evidence output, and rollback where applicable.

### /operations
Live execution cockpit. Shows concurrent Elyandra/Play/tool activity and where work is blocked/waiting.

### /evidence
Searchable provenance layer. Supports event/log/session/PCAP/artifact references without pretending all evidence types are locally stored in the same database.

### /elyandra
Conversation, activity ledger, sessions, reasoning products, memory controls, tool activity, and model/runtime status.

### /infrastructure
Security Onion, sensors, endpoint agents, Kali workers, routers/firewalls, integrations, queues, storage, versions, and health.

### /automations
Continuous `WHEN → IF → THEN → VERIFY` rules. Automation is deterministic by default; model classification is an explicit step when used.

### /policies
Authorization scope, operating modes, action classes, approvals, worker permissions, target allowlists, retention, and autonomy.

### /system
Product configuration, users/roles, updates, diagnostics, storage, backup/restore, and audit.

## Elyandra contextual contract

Each page can publish a typed context envelope:

```text
workspace
site
route
time_window
selected_entities[]
selected_relationships[]
investigation_id?
operation_id?
mode
```

The agent never receives implicit authority from UI selection.

## Universe interaction model

- Click node: select asset/endpoint.
- Click edge: select relationship/flow aggregate.
- Double-click/drill: narrower topology.
- Scroll/zoom: graph navigation.
- Timeline scrub: historical projection.
- “Evidence”: opens exact supporting records.
- “Investigate”: creates/proposes Investigation/Play with selected context.
- “Ask Elyandra”: binds context but does not execute.

## Responsive policy

Desktop is the full operational surface. Tablet supports investigation/triage. Mobile is primarily awareness, approval, and incident response; dense graph authoring is not a mobile requirement.

## Open questions

- Final visual language/logo assets.
- Geographic view privacy defaults.
- Accessibility motion-reduction behavior for live flows.
- Maximum graph density before forced aggregation.

[← Play Engine](../architecture/play-engine.md) · [Next: Upstream Adoption →](../research/upstream-adoption.md)
