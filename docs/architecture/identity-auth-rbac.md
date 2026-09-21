# Identity, Authentication, and RBAC

**Status:** Accepted  
**Version:** 1.0

## Identity domains

Ely separates:
- human User;
- ServiceIdentity;
- NodeIdentity;
- AgentSession;
- external/provider credential.

They are never represented by the same credential type.

## Human authentication

V1 local product supports:
1. WebAuthn/passkey as preferred authentication;
2. Argon2id-hashed password fallback;
3. recovery codes;
4. optional TOTP.

No plaintext/reversible password storage.

Multi-site/product phase adds OIDC federation without replacing Ely's internal user/role IDs.

## Sessions

- secure HttpOnly/SameSite cookies for browser;
- bounded lifetime;
- rotation on privilege change;
- CSRF protection for state-changing browser requests;
- re-authentication for high-impact approvals when policy requires it.

## Roles

Baseline roles:

### Owner
Workspace governance, policies, enrollment, all approvals.

### Administrator
Infrastructure/config/user administration subject to policy.

### Analyst
Observe, investigate, manage findings/investigations.

### Responder
Analyst + approved defensive Plays.

### Assessor
Explicit ASSESS capability, still target-scope constrained.

### Observer
Read-only product visibility.

Roles map to capabilities; policy uses capabilities, not hard-coded role names.

## Separation of duties

High-impact actions can require:
- capability;
- correct operating mode;
- target authorization;
- explicit approval.

A role alone never bypasses these.

## Service/node identity

Nodes use client certificates issued after one-time enrollment.

Service-to-service identity is mTLS/local service credential, not shared API keys.

## Tenant boundary

Every persistent domain row includes workspace ownership directly or through an immutable parent.

Authorization queries always bind workspace context server-side.

Cross-workspace access is denied before object existence is disclosed.

## Audit

Authentication, role changes, enrollment, certificate revocation, approvals, and session elevation are audit events.

## Acceptance tests

- stolen observer token cannot approve;
- changing user's role invalidates/refreshes active privilege;
- revoked node certificate cannot reconnect;
- ID guessing cannot reveal another workspace;
- passkey/recovery flows are auditable without logging secrets.
