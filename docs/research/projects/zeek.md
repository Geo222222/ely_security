# Project Audit — Zeek

**Decision:** Primary passive network-observation engine for V1.  
**License:** BSD-style / permissive.  
**Sovereignty strategy:** separate process + versioned log/event adapter.

## Verified facts

Zeek is a network analysis framework rather than a conventional signature IDS. It converts network traffic into high-level events/logs describing connections and application protocols. The project is BSD licensed.

## Why Ely chooses Zeek

Zeek's architecture aligns with Ely's core epistemic rule: observe richly before deciding what an observation means.

Strong uses:
- connection history;
- DNS;
- TLS;
- HTTP and other protocol metadata;
- file metadata;
- service/protocol discovery;
- relationship reconstruction.

## Ely-owned abstraction

A Zeek adapter maps records into canonical:
- NetworkObservation;
- Flow;
- DomainResolution;
- ProtocolObservation;
- FileObservation;
- ServiceObservation.

The raw Zeek record is retained/referenced for provenance.

## Do not inherit

- UID as global Ely identity;
- Zeek schema names in product APIs;
- Zeek scripts as Ely policy authority;
- assumptions that absence of a Zeek observation means absence of behavior.

## Replacement path

Any passive sensor capable of producing equivalent Ely observations can satisfy the adapter contract. Suricata metadata can cover a subset; future Ely/native sensors are possible.

## Sources

- https://github.com/zeek/zeek
- https://raw.githubusercontent.com/zeek/zeek/master/COPYING

## Remaining empirical work

Measure CPU/event volume and choose which protocol logs are enabled by default for the V1 appliance.
