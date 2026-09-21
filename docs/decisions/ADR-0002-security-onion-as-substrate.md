# ADR-0002 — Security Onion is a substrate, not the Ely product shell

**Status:** Superseded by [ADR-0009](ADR-0009-native-sensor-stack.md)  
**Date:** 2026-09-21  
**Superseded:** 2026-09-21

[← ADR-0001](ADR-0001-local-first-control-plane.md) · [Next ADR →](ADR-0003-external-policy-boundary.md)

## Historical context

Early architecture work identified Security Onion as a candidate integrated telemetry/SOC substrate because it already combines mature network/host visibility and analyst workflows.

Even at this stage, Ely was to own its canonical domain, Security Graph, Universe, investigations, Plays, policy, and operator experience.

## Original decision

Treat Security Onion as one candidate integrated telemetry/SOC substrate, isolated behind Ely adapters.

## Why this was superseded

Deeper licensing, historical, and dependency research established that Ely can compose the underlying capabilities more sovereignly from current upstream primitives:

- Zeek;
- Suricata;
- optional Arkime;
- Ely Node Agent + osquery;
- PostgreSQL/NATS/OpenSearch projections.

Security Onion remains valuable as a reference architecture and optional integration profile, but it is no longer the default Ely runtime substrate.

Current decision: [ADR-0009 — Native upstream sensors are the default stack](ADR-0009-native-sensor-stack.md).

## Preserved lesson

This ADR is intentionally retained. Architecture history should show how research changed the decision rather than rewriting the past.
