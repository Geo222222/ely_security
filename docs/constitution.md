# Ely Security Constitution

**Status:** Accepted for architecture work  
**Version:** 1.0  
**Date:** 2026-09-21

This document contains the non-negotiable engineering laws of Ely Security. Implementation choices may change. These laws do not change silently.

## 1. Sovereignty

Ely owns the concepts that define the product:

- canonical domain model;
- Security Graph;
- observation/evidence model;
- investigation model;
- Play model;
- policy and authorization contract;
- execution contract;
- public/internal APIs;
- audit semantics;
- operator experience.

Third-party software may implement replaceable primitives. No third-party schema, UI, API, database, or agent runtime is allowed to become the definition of Ely.

## 2. Evidence before interpretation

Ely preserves four epistemic classes:

`OBSERVATION → DERIVED FACT → HYPOTHESIS → DETERMINATION`.

They are never silently collapsed. A model-generated statement cannot become an observation. A determination records the evidence and method that produced it. Unknown and insufficient-evidence are valid outcomes.

## 3. Provenance is mandatory

Every material claim and action must be attributable.

At minimum:

`who/what, when, target, source, evidence, reason, authority, result`.

Raw source evidence remains retrievable according to retention policy. Normalization never destroys provenance.

## 4. AI is an operator, never an authority boundary

Elyandra may observe, reason, recommend, compose Plays, and request typed actions.

Elyandra may not:

- create authorization;
- expand target scope;
- bypass policy;
- turn text into unrestricted shell authority;
- convert untrusted telemetry into instructions;
- declare its own action safe.

All consequential execution crosses deterministic policy and execution boundaries outside the agent process.

## 5. Scope is explicit

Active security assessment is permitted only against explicit authorized scope.

Observation of a device, address, SSID, upstream network, domain, or endpoint does not authorize active testing of it.

Scope expansion is an operator/policy event and is auditable.

## 6. Replaceability is designed, not promised

Every external dependency receives:

- a capability contract;
- an adapter or process boundary;
- a license record;
- an upgrade strategy;
- an exit strategy.

If replacing a dependency requires redesigning Universe, Elyandra, Plays, or policy, the abstraction is wrong.

## 7. Collection survives intelligence failure

Sensors, ingestion, durable evidence, deterministic detections, policy enforcement, and existing deterministic automations continue when Elyandra or its model provider is unavailable.

Loss of AI capability degrades intelligence, not visibility or enforcement.

## 8. Enforcement fails closed

If policy state, target identity, authorization scope, or execution grant validity cannot be established, state-changing execution does not proceed.

Read-only observation may degrade independently when safe to do so.

## 9. Workers are untrusted

Kali and other execution nodes are workers, not controllers.

They receive short-lived, typed grants and return structured results/evidence. They do not receive permanent model-held root credentials or unilateral policy authority.

## 10. History is preserved

Security state is temporal.

Asset identity, relationships, policies, investigations, findings, and actions are modeled over time. Current state is a projection of history, not a destructive rewrite of it.

## 11. Product code and evidence are separate

Source repositories never contain real operational secrets, credentials, PCAP, host triage bundles, or private evidence.

Synthetic fixtures are explicitly labeled.

## 12. Local-first is a product property

A site can perform core monitoring, evidence retrieval, policy enforcement, investigations, and approved operations without requiring an Ely cloud service.

Future cloud coordination cannot become a hidden dependency for local defense.

## 13. Upstream code is mined lawfully

Open source is used according to its license.

For each upstream capability Ely will choose one of:

- depend;
- integrate;
- extract/reuse under license;
- learn and independently implement;
- reject.

License obligations are architecture constraints, not release-time paperwork.

## 14. Security boundaries are independently testable

No security boundary exists only because a prompt says so.

Policy, execution grants, worker isolation, authentication, tenancy, secret access, and audit integrity require deterministic tests.

## 15. Architecture is traceable

Consequential decisions require an ADR or an architecture document with rationale, alternatives, consequences, and evidence.

Unknowns are recorded only when they depend on measurement, external facts, or implementation experiments. The architect resolves design questions.

## Amendment rule

A constitutional change requires:

1. explicit proposed amendment;
2. threat-model review;
3. sovereignty review;
4. migration consequences;
5. ADR explaining why the prior law is no longer correct.
