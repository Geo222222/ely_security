# Asset and Identity Resolution

**Status:** Accepted  
**Version:** 1.0

## Principle

An IP address is an observation, not an asset identity.

Ely creates stable Asset identities and links time-bounded observed identifiers to them with evidence and confidence.

## Canonical entities

### Asset
Stable Ely UUIDv7 representing a tracked logical/physical device or compute unit.

### Interface
A network interface associated with an Asset.

### ObservedIdentifier
Typed value with scope and time:
- MAC;
- IP;
- hostname;
- DHCP client identifier;
- mDNS/NetBIOS name;
- endpoint-agent ID;
- certificate/public-key fingerprint;
- cloud/VM/container ID;
- operator-assigned identity.

### IdentityAssertion
Claim linking identifier/interface/asset with:
- evidence refs;
- resolver rule/version;
- confidence;
- valid interval;
- competing candidates.

## Resolution order

Highest-confidence deterministic evidence wins:

1. enrolled Ely Node Agent cryptographic identity;
2. stable hardware/public-key identity with matching history;
3. explicit operator binding;
4. DHCP/client-id + MAC + topology evidence;
5. multi-signal network fingerprint;
6. hostname/IP-only correlation.

Low-confidence correlation never silently merges assets.

## MAC randomization

Randomized/private MACs are expected behavior.

Ely does not label a randomized MAC as malicious by itself.

Resolver can group observations when supported by stronger evidence such as:
- enrolled agent identity;
- device-provided stable key;
- repeated DHCP attributes and behavior;
- explicit operator recognition.

Otherwise the device remains a distinct/uncertain Asset.

## IP lifecycle

`IPAddressAssignment` is temporal:
- address;
- interface;
- network;
- first_seen;
- last_seen;
- valid_from;
- valid_to;
- evidence.

Historical IP reuse never rewrites past relationships.

## Merge and split

Asset merge is a reversible control-plane operation that preserves old IDs as aliases and records evidence/rationale.

Asset split reconstructs future/current identity without deleting historic observations.

Both operations are auditable.

## Asset states

`NEW | KNOWN | CHANGED | SUSPICIOUS | CONTAINED | OFFLINE | RETIRED`

State is derived from explicit facts/findings and policy; it is not a free-form LLM label.

## Confidence

Use bounded numeric confidence internally plus named bands:
- CONFIRMED;
- HIGH;
- MEDIUM;
- LOW;
- UNRESOLVED.

Confidence records method and evidence. It is never displayed without reason.

## Acceptance tests

- DHCP churn retains asset history;
- same IP assigned to two devices at different times does not merge them;
- randomized MAC does not auto-trigger malicious finding;
- enrolled agent identity overrides weak network guesses;
- asset merge/split preserves evidence and graph history.
