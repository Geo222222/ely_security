# Repository and Module Structure

**Status:** Accepted  
**Version:** 1.0

## Monorepo

Ely Security uses one product monorepo until scale/team boundaries prove a split necessary.

```text
ely_security/
├─ apps/
│  ├─ web/                     # Next.js command center
│  └─ elyandra/                # OpenCode-derived agent/operator
├─ cmd/
│  ├─ ely-core/                # Go control plane binary
│  ├─ ely-collector/           # sensor/provider collector
│  ├─ ely-node-agent/          # endpoint node
│  └─ ely-worker/              # execution worker
├─ internal/
│  ├─ domain/
│  ├─ telemetry/
│  ├─ identity/
│  ├─ graph/
│  ├─ evidence/
│  ├─ detection/
│  ├─ investigations/
│  ├─ plays/
│  ├─ policy/
│  ├─ automation/
│  ├─ execution/
│  ├─ audit/
│  ├─ auth/
│  └─ api/
├─ adapters/
│  ├─ zeek/
│  ├─ suricata/
│  ├─ arkime/
│  ├─ osquery/
│  ├─ firewall/
│  ├─ dns/
│  └─ wireless/
├─ contracts/
│  ├─ protobuf/
│  ├─ openapi/
│  ├─ events/
│  └─ schemas/
├─ packages/
│  ├─ ui/
│  ├─ universe/
│  └─ agent-tools/
├─ deploy/
│  ├─ small/
│  ├─ lab/
│  ├─ sensor/
│  └─ worker/
├─ migrations/
├─ fixtures/
│  ├─ synthetic/
│  └─ sanitized/
├─ tests/
│  ├─ contract/
│  ├─ integration/
│  ├─ replay/
│  ├─ security/
│  └─ e2e/
├─ docs/
└─ tools/
```

## Boundaries

`internal/domain` imports no vendor adapter.

Adapters depend inward on contracts/domain; domain never depends outward on provider schemas.

Elyandra cannot import authority modules. It uses network/API contracts.

Frontend cannot mutate PostgreSQL directly.

## Generated code

Protobuf/OpenAPI generated code is reproducible and clearly separated from hand-written domain code.

## Fixtures

Real operational PCAP/logs are prohibited from Git.

Fixtures must be synthetic or explicitly sanitized and labeled.

## Module split rule

A logical module becomes a separate deployable only when one of these exists:
- distinct privilege boundary;
- distinct scaling characteristic;
- independent failure domain;
- independent update lifecycle;
- hardware placement requirement.

This prevents premature microservices while preserving clean interfaces.
