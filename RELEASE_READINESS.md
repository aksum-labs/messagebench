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
1. Two genuine independent reviewers inspect the hash-bound packet, expected outcomes and rights; a responsible human authenticates independence and approves publication.
2. Review and merge company-bot PR #7. Main/tag/environment protections, hosted CI and signed candidate are already verified; owner maintains MFA and accountable security response.
3. After review, authorize the exact protected RC tag workflow and human environment approval. The current authentic main snapshot is distinct from that formal release.
4. Approve official badge/account/foundation representations separately. For future camt support, obtain authoritative joint-contributor redistribution clearance first.

Current original 389-item accounting is FINAL_COMPLETION_REPORT_CURRENT.md; the 29 September report is retained as historical evidence.
