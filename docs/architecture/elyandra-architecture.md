# Elyandra Architecture

**Status:** Accepted  
**Version:** 1.0

## Role

Elyandra is Ely Security's reasoning/operator layer.

She does not own:
- telemetry;
- canonical state;
- policy authority;
- execution credentials;
- evidence truth.

## Process boundary

Elyandra runs as a separate TypeScript process derived from OpenCode concepts/code under its license.

The Core exposes a dedicated `Elyandra Gateway`.

```text
UI context / Operator
        ↓
     Elyandra
        │ typed tools
        ▼
Elyandra Gateway
   ├─ Graph Query
   ├─ Evidence Search
   ├─ Investigations
   ├─ Play Proposal/Run
   └─ Policy Explain
```

No direct PostgreSQL, NATS administration, SSH, or signing-key access.

## Context contract

Every request carries explicit context:
- workspace/site;
- route;
- selected entity IDs;
- selected relationship IDs;
- time window;
- investigation/operation ID;
- operating mode.

UI selection provides context, never authorization.

## Tool categories

### Read
- assets/relationships;
- findings;
- evidence;
- investigations;
- source health;
- policy explanations.

### Propose
- hypothesis;
- Finding candidate;
- Investigation;
- Play/automation draft.

### Request
- run existing Play;
- request approval;
- request bounded data collection.

All requests still pass normal policy.

## Memory

### Conversation memory
Operator dialogue and current task state.

### Procedural memory
Prior Play outcomes, resolved investigations, operator preferences that are not secrets.

### Security knowledge
Never copied into opaque model memory as canonical truth. Security knowledge is retrieved from Graph/Evidence/Investigation stores.

Memory records include source and expiry/retention class.

## Untrusted-content handling

Telemetry, logs, files, web content, tool output, and TI descriptions are untrusted data.

The Gateway:
- serializes them into data fields;
- labels source/sensitivity;
- strips/escapes control markup where needed;
- limits size;
- does not expose secrets unnecessary to the question.

Prompt instructions found inside evidence have no authority.

## Model providers

Provider abstraction supports local or remote models.

Per-tool/request policy determines what data may leave the site.

Sensitive/raw evidence defaults to local-only processing or explicit operator permission.

## Reasoning artifacts

For material security conclusions Elyandra returns a structured product:

- question;
- observed facts;
- inference/hypothesis;
- evidence for;
- evidence against;
- unknowns;
- confidence;
- recommended safe next action.

The rendered prose is downstream of the structured result.

## Agent specialization

V1 prefers one primary Elyandra plus bounded specialist reasoning prompts/tools.

Subagents are introduced only when evaluations show measurable gain. Agent count is not an architecture goal.

## Evaluation

Qualification suites include:
- evidence-grounding;
- unsupported-claim rate;
- prompt-injection resistance;
- tool-selection correctness;
- scope preservation;
- abstention when evidence is insufficient;
- recovery from contradictory evidence.

## Acceptance tests

- malicious log text cannot call a tool;
- Elyandra cannot create approval;
- evidence citation IDs in response exist;
- deleting model provider access does not stop telemetry/control plane;
- selected UI asset changes context but not target authorization.
