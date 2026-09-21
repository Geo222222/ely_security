# Supply Chain and Update Architecture

**Status:** Accepted  
**Version:** 1.0

## Build provenance

Every release produces:
- source commit;
- version;
- dependency lockfiles;
- SBOM (SPDX or CycloneDX);
- checksums;
- signed release manifest;
- container/image digests where applicable.

## Dependency policy

- versions pinned/locked;
- automated vulnerability/license inventory;
- major upgrades require dependency-register review;
- security advisories can trigger emergency update process;
- abandoned dependencies are replaced or isolated.

## Third-party security content

Rules, signatures, TI feeds, and model/tool packages are supply-chain inputs.

Every imported bundle records:
- publisher/source;
- version/time;
- hash/signature;
- applicable scope;
- activation state.

No downloaded rule/tool gains execution authority by being downloaded.

## Update channels

- stable;
- candidate/lab;
- offline signed bundle.

Production defaults stable.

## Core update process

1. verify signature/manifest;
2. preflight disk/version compatibility;
3. backup authoritative state;
4. stage binaries/images;
5. run migrations;
6. health qualification;
7. activate;
8. preserve rollback point when schema permits.

## Node update

Node agents support phased rollout and compatibility window.

A compromised/outdated node can be quarantined by policy without preventing the Core from operating.

## Rules/models

Model provider/model changes are separately versioned from product releases.

Detection-rule updates run regression fixtures before activation.

## Acceptance tests

- modified update bundle fails verification;
- SBOM can map a CVE to affected component/version;
- failed migration restores/halts safely;
- untrusted rule bundle cannot execute code;
- offline update path works without Internet.
