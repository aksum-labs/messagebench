# Release readiness

**NOT READY — FIX REQUIRED** for publication. Recommended local version: **0.1.0a2**
(Semver spelling 0.1.0-alpha.2). The engineering candidate is available for review.

Exact supported namespaces:
- urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08
- urn:iso:std:iso:20022:tech:xsd:pacs.002.001.10

The 26 exact fields, paths and comparison types are enumerated in docs/fields.md. pacs.008
covers identifiers, account/agent context, names, instructed and settlement amounts and
unstructured remittance. pacs.002 covers message ID, original references, status, reason
codes and reason text. Three contracts declare 31 assertions in total. Coverage remains
scoped; a passing assertion is not complete-document preservation.

Implemented: inspect, compare, corpus verify, suite, report and regression; deterministic
JSON, text, escaped HTML and JUnit; single-item and explicit unique-key batch association;
68 synthetic cases. Cases are not independently reviewed. No external technical review or
independent deployment has occurred. A separate Node.js demonstration exercises file handoff.

Unsupported: camt.053 and all other versions, cross-family/version translation, arbitrary
nested keyed structures, date/time semantics, institutional rules, structured remittance,
whole-document equivalence and production validation. The literal keyed-items comparator
returns UNSUPPORTED; transaction key association is implemented separately. See LIMITATIONS.md.

Security caveats: Linux/CPython 3.12 profile tested; supplied native wheel is platform-specific.
Older native profiles fail closed. No OS sandbox or general vulnerability-free claim.
Licensing: original Apache-2.0, separate XSD terms, native dependency notices and LGPL source
obligations. The camt asset is excluded while its redistribution basis is unresolved.

Permitted positioning: “Aksum MessageBench helps financial-software engineers test whether
message adapters preserve declared payment information. It runs offline on synthetic fixtures
or institution-local files and produces reproducible, scope-labelled results.” Disclose alpha
status and pending independent review. Do not claim approval, certification, national-standard
status, production safety, full preservation, a badge, signed release or independent review.

Before publication, obtain actual fixture/technical/provenance review, appoint real maintainers
and vulnerability responders, configure required reviews/protected releases and run hosted CI.
The owner authorized development continuation, not automatic publication. No repeated approval
request is needed for the remaining local work.

v0.5 criteria are not met: only two message versions and no 60 independently reviewed cases.
v1.0 criteria are not met: no stable public API commitment, 100 reviewed cases, independent
external review/reproduction/use or established public governance.
