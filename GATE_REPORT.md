# Gate report — 0.2.0-rc.1

> Historical engineering acceptance snapshot (29 September 2026). Current publication/security/recognition state is recorded in EXTERNAL_RECOGNITION_COMPLETION_REPORT.md. This historical report is not a current visibility or badge claim.

Current 1 October update: public source/protection, hosted CI and signed candidate are verified. The remaining B/C/F gates are genuine independent review, rights approval and formal release approval. See FINAL_COMPLETION_REPORT_CURRENT.md for all 389 current dispositions. The snapshot below retains its original dated decision.

Release decision: **NOT READY — FIX REQUIRED** for public release. The remaining fixes are
authentic human review/approval and owner-controlled activation, not unfinished implementation.
The technical candidate and offline bundle are complete; nothing has been published.
The owner authorized expansion before independent review. That authorization is not review evidence.

## Technical gates

| Gate | Status | Evidence and boundary |
|---|---|---|
| A central proposition | PASS | Six original paired controls; schema-valid reference truncation, leading-zero loss, removed remittance and currency change detected. Identity and permitted regenerated ID pass. Deterministic golden bytes. |
| B correctness | BLOCKED-BY-HUMAN | All 100 recorded classifications match; required incomplete checks block PASS. The separately required independent review of expectations needs genuine humans. |
| C completeness | BLOCKED-BY-HUMAN | Every one of 38 required assertion declarations has a targeted failing mutation; 40/40 mutants killed; parser security controls pass. Independent corpus approval is a human action. |
| D portability | PASS | Separate Node adapter/file-handoff example tested without modifying the oracle; no adapter execution in the runtime. |
| E differentiation | PASS | Adapter-neutral declared preservation, explicit semantics, coverage and reusable pairs exceed parser/XSD-only scope. Prior-art overlap is documented, not a claim of universal novelty. |
| F release hygiene | BLOCKED-BY-HUMAN | Local checks, build/install, SBOM, locks, rights decisions and workflows prepared. Hosted checks, rights approval, protected settings and signed publication require accountable humans/account ownership. |
| G claim safety | PASS | Exact scope, no endorsement/certification/national-rule/production-safety claims, visible limitations and report disclaimer. |

Gate 1's technical A–H proposition is supported; its independent-review prerequisite remains
BLOCKED-BY-HUMAN. The approved expansion decision is recorded in docs/expansion-decision.md.

## Correctness and measured evidence

- 100 original paired XML cases across pacs.008.001.08 and pacs.002.001.10; 13 additional generated security/workflow scenarios with controls.
- 10 contracts, 38 required assertion declarations, 27 extractable fields. Extraction is not a whole-document preservation claim.
- 140 pytest tests; core semantic branch coverage 99/102 (97.06%). Full coverage is in evidence/coverage.json.
- 40/40 targeted mutants killed. This is a defined mutation campaign, not a whole-program mutation score.
- 200 documents agree across lxml/libxml2 and xmlschema XSD processors.
- 100,000 parser fuzz iterations and 10,000 contract mutations: no unexpected exception/acceptance in the recorded bounded runs.
- Exact baseline results: evidence/baseline.json. Parser and XSD validation intentionally do not compare transformations; this is scope differentiation, not a bug in those validators.
- No known unresolved implementation bug from these checks; no proof of absence of all bugs.

## Security

Threat model, parser/resource rejection, closed contracts, no execution/plugins/network inputs,
privacy-safe reports and escaped HTML are tested. CLI CPU/wall/address-space limits complement
XML quotas. Python API callers own their process limits. No OS-sandbox claim.
All 60 pinned development/runtime distributions are inventoried and license checked. The dated
Python advisory scan is evidence/dependency-audit.json; native libxml2/libxslt/libiconv review is
separate in evidence/native-advisory-review.json and its indexed source evidence. No unresolved
critical/high exploitable finding was identified in the stated scan/review scope. One low Bandit
XML-renderer warning is documented; the renderer creates output and does not parse untrusted XML.
SBOM includes native dependencies. Hashes are provenance metadata, not anonymization.

## Rights

Original code/fixtures: Apache-2.0. Two unmodified SWIFT-origin XSDs retain their notices and
terms; public source/provenance hashes are in the rights register. Native sources and LGPL
relink/rebuild materials accompany the platform bundle. Python distribution licenses are
inventoried individually. The separate GNU libiconv command-line source carries GPL terms;
that program is not linked into the wheel. See bundle-rights-register.json for bundle assets.

camt.053.001.08 is excluded. Joint-contributor redistribution authority was not established
from the reviewed primary sources. Completing support requires authoritative rights clearance;
no uncertain asset or placeholder extractor is shipped. See docs/camt053-asset-review.md.
A qualified independent rights approval is BLOCKED-BY-HUMAN, not fabricated by this report.

## OpenSSF and release

All 67 Passing criteria have evidence/readiness dispositions in docs/openssf-readiness.md.
Seven local Scorecard source checks ran; these are not a full public-repository score. Badge,
public history, authentic maintainer responsiveness, hosted checks and owner settings require
human/account actions. Silver/Gold are future governance outcomes, not achieved badges.

Version 0.2.0-rc.1 is deliberate: three cleared versions and independently reviewed corpus are
not available, so v0.5 is not claimed. v1.0's independent adoption/review/API/governance criteria
are not met. Two clean same-environment unsigned Python builds and an outside-checkout offline
installation are supplied in the final bundle; these do not establish independent reproduction.
See FINAL_COMPLETION_REPORT.md for every original mandate item and docs/reproduce.md for commands.
