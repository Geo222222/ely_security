# Sovereignty Program

**Status:** Accepted  
**Version:** 1.0

## Objective

Ely Security must continue to exist if any single upstream project disappears, changes license, is acquired, becomes commercial-only, suffers a major compromise, or stops fitting the product.

Sovereignty does not mean rewriting good software for pride. It means owning the contracts, state, and knowledge required to replace it.

## Dependency classes

### Primitive
A mature low-level implementation used directly behind an Ely-owned contract.

Examples: PostgreSQL, NATS, Zeek.

### Adapter dependency
A provider whose output/API is normalized at a boundary.

Examples: Suricata EVE, Arkime session/PCAP API, osquery.

### Reference implementation
A project studied for architecture, UX, algorithms, deployment, and failure history without becoming a runtime requirement.

Examples: Malcolm, Security Onion, CAI.

### Temporary strategic dependency
A component used to accelerate early operation while an Ely-owned replacement contract already exists.

### Forbidden dependency
A dependency whose license, trust model, coupling, or security model would make Ely less sovereign than the capability is worth.

## Sovereignty test

Every dependency is reviewed against eight questions:

1. What exact capability does it provide?
2. What data/state does it own?
3. Does Ely preserve a canonical copy or canonical interpretation?
4. Can another implementation satisfy the same Ely contract?
5. What breaks if the dependency disappears for 30 days?
6. Does its license constrain Ely distribution, hosting, linking, or modification?
7. Does compromise of the component cross a trust boundary?
8. What is the concrete exit plan?

## Architectural rule

External dependencies connect below Ely-owned contracts:

```text
Ely Domain Contract
       │
 Adapter / Provider Interface
       │
 ┌─────┼──────────────┐
 │     │              │
Zeek  Suricata      Arkime
```

Never:

```text
Upstream schema/API
       │
       ├── Universe
       ├── Elyandra
       ├── Plays
       └── Policy
```

## Adopt → Abstract → Validate → Replace

### Adopt
Use a mature project when it provides a proven capability.

### Abstract
Define Ely's own capability/data contract immediately.

### Validate
Test semantic equivalence, failure behavior, performance, and security.

### Replace
Replacement is optional, not ideological. We replace when sovereignty, economics, security, performance, or product differentiation justify it.

## What Ely must own permanently

- canonical identifiers and schemas;
- asset and identity resolution;
- Security Graph semantics;
- findings/investigations;
- evidence provenance;
- policy decisions;
- execution-grant semantics;
- Play definitions/state;
- automation semantics;
- audit ledger;
- UI/context contract;
- Elyandra's security tool contract.

## What Ely should usually not rebuild

Unless evidence shows a strategic need:

- packet decoding;
- protocol parsers;
- IDS signature engines;
- relational database engine;
- durable message broker;
- general search engine;
- operating-system query engine;
- cryptographic primitives.

## License isolation strategy

Permissive components may be embedded subject to their notices.

Strong-copyleft components are preferred as separate processes communicating over documented data/protocol boundaries. Ely avoids linking proprietary core code to GPL components unless the resulting licensing obligation is intentionally accepted.

ELv2/proprietary/open-core components are treated as optional integrations unless a separate commercial arrangement is deliberately chosen.

This is an architecture rule, not legal advice; release packaging receives legal review.

## Source-code reuse rule

Before copying upstream code:

1. identify exact source file/commit;
2. identify applicable license and notices;
3. decide whether reuse or independent implementation is preferable;
4. preserve attribution/notice obligations;
5. add the dependency/reuse record;
6. add tests proving Ely behavior.

Concepts and algorithms are not copied blindly. We first understand the invariant they solve.

## Exit-plan quality levels

- **S0:** no exit plan — prohibited for core architecture.
- **S1:** conceptual alternative exists.
- **S2:** adapter exists and alternate implementation is plausible.
- **S3:** alternate provider passes contract tests.
- **S4:** dependency can be switched without product-level migration.

Core runtime dependencies should reach S2 before V1 and S3 before product-scale distribution where practical.

## Governance

The dependency register is reviewed:
- before introducing a runtime dependency;
- on major-version upgrades;
- on license changes;
- after material security advisories;
- before commercial distribution.
