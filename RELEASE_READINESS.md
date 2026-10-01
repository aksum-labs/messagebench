# Release readiness — 0.2.0-rc.1

**Engineering candidate: complete. Source published 1 October 2026 at ad10253; candidate signed/attested through the hosted snapshot workflow. Independent review and formal release approval: BLOCKED-BY-HUMAN.**
Recommended engineering candidate: Semver 0.2.0-rc.1, Python 0.2.0rc1. No formal reviewed public release was made. Current hosted/security/recognition state is in EXTERNAL_RECOGNITION_COMPLETION_REPORT.md.

Exact supported namespaces:
- `urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08`
- `urn:iso:std:iso:20022:tech:xsd:pacs.002.001.10`

The 27 exact supported fields and their extraction paths/types are listed in docs/fields.md.
Ten versioned contracts exercise 38 required assertion declarations. The 100 synthetic pairs
have pre-recorded outcomes, successful automated checks and a hash-bound human-review packet.
They have not been independently reviewed. No outside institution's use is claimed.

Unsupported features: camt.053.001.08 (rights exclusion), other versions, arbitrary XPath/code,
universal translation, full-document equivalence, scheme business rules, live connectivity,
adapter execution, automatic timezone/calendar guesses and heuristic transaction matching.
Unknown required information blocks overall PASS. Unexamined fields are reported explicitly.
Linux is the verified file-safety/process profile; unsupported platform protections fail closed.

Security caveats: resource limits are not an OS sandbox; bounded tests are not an exhaustive
security proof; institution-local files can be sensitive, and hashes are not anonymization.
The offline wheel bundle is Linux x86_64 CPython 3.12 specific. Native wheel reproducibility
is not claimed. Native license notices, original sources and relink/rebuild instructions are
included. See rights register and camt exclusion rationale; human legal approval is not asserted.

Approved positioning:
“MessageBench helps financial-software engineers test whether message adapters preserve
declared payment information. It runs offline on synthetic fixtures or institution-local files
and produces reproducible, scope-labelled results.”

Disclose the candidate status, exact supported scope and absence of independent review.
Do not claim NBE/EthSwitch/SWIFT/ISO approval or certification, production safety, national
standard status, complete-document preservation, an unmeasured Scorecard score or an unearned badge. Actual public Scorecard is 7.1/10 at ad10253; no Best Practices badge exists.
Every result states: “Pass means only the listed assertions passed for these inputs and versions.”

Human-only release actions:
1. Two genuine independent reviewers inspect the hash-bound packet, expected outcomes and rights;
   a responsible human authenticates identities/independence and approves publication.
2. Actual repository hardening/hosted CI is recorded in evidence/github-settings.json and
   EXTERNAL_RECOGNITION_COMPLETION_REPORT.md. Owner supplies accountable independent reviewers
   and any still-missing MFA/environment reviewer controls.
3. Owners enable the protected OIDC signing job and verify its exact identity before publication;
   create public repository/release and submit any badge application only with authorization.
4. For camt support, obtain authoritative joint-contributor redistribution clearance first.

v0.5 criteria are not satisfied (third version and reviewed corpus). v1.0 criteria are not
satisfied (external review, outside use, stable public API and governance). Preparation is complete;
these real-world human facts cannot be manufactured by automation.
