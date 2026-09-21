# Product Page Stack

**Status:** Accepted  
**Version:** 1.0

[← Play Engine](../architecture/play-engine.md) · [Next: Upstream Adoption →](../research/upstream-adoption.md)

## Persistent shell

- workspace/site;
- primary navigation;
- global search/command palette;
- operating mode;
- time/live context;
- coverage/system health;
- active Operation count;
- attention indicator;
- contextual Play launcher;
- persistent/collapsible Elyandra operator.

Exactly one primary route is active.

## Visual language

Ely uses a dark operational interface:
- near-black/deep-navy surfaces;
- electric purple/blue accent family;
- high-contrast neutral text;
- semantic state colors reserved for status/severity;
- dense but structured data layout;
- no decorative glow that reduces legibility.

Ely owns tokens/components. Radix primitives may supply accessible behavior underneath.

## Routes

`/command` — mission control.

`/universe` — live/replayable Security Graph.

`/assets` — canonical inventory/identity.

`/wireless` — AP/SSID/client/coverage.

`/threats` — Findings and Provider Alerts.

`/investigations` — evidence-backed cases.

`/plays` — investigate/defend/assess workflows.

`/operations` — live execution cockpit.

`/evidence` — provenance/artifacts/session/PCAP.

`/automations` — WHEN/IF/THEN/VERIFY.

`/policies` — authority/scope/approvals.

`/elyandra` — sessions/activity/memory/evaluations.

`/infrastructure` — nodes/providers/storage/health.

`/system` — users, updates, backup, certificates, diagnostics.

Detailed contracts: [page-specifications.md](page-specifications.md).

## Elyandra UI context

```text
workspace_id
site_id
route
time_window
selected_entity_ids[]
selected_relationship_ids[]
investigation_id?
operation_id?
mode
```

Context does not grant authority.

## Universe

Views:
`Live | External | Connections | Geographic | Timeline | Replay`.

Inspector:
`Overview | Connections | Processes | Services | Findings | History | Evidence`.

Initial renderer: Sigma.js + Graphology.

### Projection density
Server projection targets a default interactive budget of roughly 800 visible nodes / 2,500 edges. Above the budget, Ely clusters/aggregates and expands on demand rather than dumping the whole graph into the browser.

The budget is configurable and later tuned by performance/UX tests.

### Geographic privacy
Geographic view is disabled for precise private-site positioning.

It may display coarse external destination GeoIP/provider geography. Ely does not plot the operator's home/site at a precise public-map coordinate by default.

## Accessibility

- WCAG-conscious contrast;
- keyboard navigation for all core actions;
- non-color status indicators;
- `prefers-reduced-motion` disables animated flow motion/transitions;
- graph has list/table alternative for critical information;
- approval cannot rely on hover-only content.

## Responsive policy

Desktop: complete operational environment.

Tablet: full triage/investigation/approval with simplified Universe.

Mobile: awareness, investigation status, evidence summaries, approvals/emergency response. Dense graph manipulation is not required.

[← Play Engine](../architecture/play-engine.md) · [Next: Upstream Adoption →](../research/upstream-adoption.md)
