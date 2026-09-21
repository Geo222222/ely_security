# ADR-0006 — NATS JetStream is the internal event backbone

**Status:** Accepted  
**Date:** 2026-09-21

## Context
Ely needs durable local-first event delivery, backpressure, replay, and a path from one appliance to distributed sites without Kafka-class operational weight.

## Decision
Use NATS JetStream for canonical internal event transport.

## Constraints
- at-least-once delivery;
- consumers idempotent;
- NATS is transport, not evidence archive;
- event subjects/schemas are Ely-owned.

## Consequences
NATS can be replaced behind the event abstraction, but V1 engineering standardizes on one broker.

## Evidence
NATS Server/clients are Apache-2.0 and JetStream provides durable streams/consumers.
