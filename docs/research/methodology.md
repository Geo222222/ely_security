# Architecture Research Methodology

**Status:** Accepted  
**Version:** 1.0

## Purpose

Ely architecture is evidence-led. Research exists to resolve decisions, not postpone them.

## Evidence hierarchy

Prefer evidence in this order:

1. upstream source code, license files, security policy, release notes;
2. official upstream documentation;
3. maintainers' official blog/advisories;
4. standards/RFCs/vendor protocol documentation;
5. reputable independent technical analysis;
6. community reports used only as supporting evidence.

Marketing copy alone does not establish an architectural fact.

## Claim classes

Every research document separates:

### Verified fact
Directly supported by a primary source.

### Engineering inference
Conclusion derived from verified facts and stated reasoning.

### Architecture decision
Choice Ely makes after evaluating evidence and constraints.

### Empirical unknown
Question that cannot be answered responsibly without measurement, a prototype, hardware access, traffic samples, or legal review.

We do not create an “open question” merely because the architect has not made a choice yet.

## Project-mining procedure

For every upstream project:

1. establish project purpose and maintained status;
2. inspect license(s);
3. inspect architecture/deployment documentation;
4. inspect canonical data formats/APIs relevant to Ely;
5. inspect security policy and material advisories;
6. identify state owned by the project;
7. identify valuable algorithms/patterns;
8. identify coupling and operational costs;
9. map capabilities to Ely-owned contracts;
10. decide: depend / integrate / learn / reuse selectively / reject;
11. record exit strategy.

## Historical research

When studying pre-2022 architecture, historical code is used to understand decomposition and design lineage, not as a reason to deploy vulnerable or unmaintained versions.

Ely implements current maintained versions of selected primitives unless a reproducibility experiment explicitly requires an old version in an isolated lab.

## License research

The architecture records:
- upstream license;
- whether Ely merely communicates with the component or links/includes code;
- redistribution implications known from the upstream project's own guidance;
- whether counsel/release review is required.

The architecture does not invent legal conclusions.

## Security research

For agent/execution frameworks, review is incomplete without:
- threat model;
- sandbox/isolation claim;
- authentication exposure;
- shell/command construction;
- secret handling;
- plugin/MCP trust boundary;
- security advisories.

## Performance research

Performance choices require representative measurements. Synthetic benchmarks are labeled synthetic.

For Ely V1, required measurements include:
- normalized events/sec;
- graph update latency;
- search p50/p95/p99;
- packet/session storage growth;
- evidence storage growth;
- NATS backlog recovery;
- endpoint agent resource use;
- worker startup/action latency.

## Decision threshold

A design decision is made when evidence establishes a safe, coherent default. It is not deferred simply because a theoretically better implementation may exist.

Only empirical parameters remain unresolved, such as:
- hardware-specific throughput;
- retention days for a given disk budget;
- exact graph partition thresholds;
- Wi-Fi chipset/driver behavior.

## Research record format

Each project/subsystem research file contains:

- conclusion;
- verified facts;
- useful mechanisms;
- failure/security lessons;
- license boundary;
- Ely adoption decision;
- Ely-owned abstraction;
- exit plan;
- evidence sources;
- empirical work remaining.

## Review rule

Before an architecture document reaches Accepted:
- every factual claim that materially affects a decision must have a source;
- every upstream dependency must have a sovereignty classification;
- every remaining unknown must explain why measurement is required.
