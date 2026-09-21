# Project Audit — CAI

**Decision:** Research mine only. No production dependency and no code copying from proprietary/research-only portions.  
**Status:** Archived upstream on 2026-08-28.

## Verified facts

CAI is archived and receives no further fixes, patches, or support.

The final repository license is mixed:
- MIT-derived components under `src/cai/agents`;
- Alias Robotics additions licensed for non-commercial research use unless separately licensed.

The project itself warns that the archived offensive-security framework should not be part of a production security programme.

Published critical advisories include command injection in agent tools such as file finding and SSH command execution.

## Why Ely studies it

CAI is useful evidence about:
- cybersecurity-agent decomposition;
- handoffs;
- multi-agent coordination;
- guardrails;
- HITL/HOTL patterns;
- benchmarking;
- prompt-injection defenses;
- what fails when security agents construct commands.

## Explicit non-adoption

Ely will not:
- depend on CAI at runtime;
- copy research/proprietary components into Ely;
- inherit command execution tools;
- inherit provider assumptions;
- infer that agentic offensive capability is safe merely because it benchmarks well.

## What Ely extracts conceptually

- benchmark the agent as a security component;
- treat prompt injection as a first-class threat;
- separate reasoning from execution;
- use purpose-specific agents only when they improve measurable behavior;
- record handoffs and tool calls.

## Sources

- https://github.com/aliasrobotics/cai
- https://github.com/aliasrobotics/cai/blob/main/LICENSE
- https://github.com/aliasrobotics/cai/security/advisories
- https://github.com/aliasrobotics/cai/blob/main/DISCLAIMER

## Remaining empirical work

None required to establish the architecture decision. Specific research papers may be mined later when designing Elyandra evaluations.
