# Project Audit — OpenCode → Elyandra

**Decision:** Evolve/fork the operator-agent experience; strip it of security authority.  
**License:** MIT.  
**Security classification:** untrusted reasoning process relative to Ely enforcement.

## Verified facts

OpenCode is an AI coding/agent system with file, shell, web, tool/MCP, session, and subagent capabilities.

Its security policy explicitly states:
- the agent is not sandboxed;
- permissions are UX, not security isolation;
- true isolation should use a container or VM;
- server mode can be unauthenticated unless configured with a password.

The current repository also has published advisories involving command execution through its web/server surface.

## What Elyandra keeps

- conversational/session model;
- model/provider abstraction;
- tool registration ergonomics;
- subagent concepts;
- streaming UX;
- permission/approval UX as defense-in-depth;
- client/server separation where useful.

## What Elyandra loses

- unrestricted shell as a normal capability;
- direct production-database credentials;
- direct root/SSH credentials;
- authority derived from prompt text;
- arbitrary MCP servers inside the trusted boundary.

## Elyandra trust contract

Elyandra receives:
- scoped query APIs;
- typed UI context;
- evidence-search tools;
- graph queries;
- Play proposal/run requests;
- policy explanation queries.

It does not receive:
- policy signing keys;
- execution-grant signing keys;
- worker root credentials.

## Tool model

Every security tool is a typed Ely API, not a raw command string.

Example:
`inspect_asset_connections(asset_id, window)`
not
`shell("tcpdump ...")`.

When raw shell is genuinely needed for a human-controlled lab/debug surface, it exists outside the normal agent execution contract and requires elevated policy.

## Sources

- https://github.com/anomalyco/opencode/blob/dev/LICENSE
- https://github.com/anomalyco/opencode/security/policy
- https://github.com/anomalyco/opencode/security

## Remaining empirical work

Threat-model the exact OpenCode fork/version used for Elyandra and remove/disable unsafe server/tool paths before integration qualification.
