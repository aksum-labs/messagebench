# Prepared release notes — 0.2.0-rc.1

Unpublished release candidate. Python version 0.2.0rc1. These notes are ready for the reviewed release workflow; they are not a release receipt.

MessageBench checks whether externally supplied financial-message file pairs preserve the information promised by a versioned engineering contract. It runs offline, executes no adapter, and produces deterministic, redacted reports with explicit coverage limits.

Supported: pacs.008.001.08 and pacs.002.001.10 only; 27 extractable fields, ten contracts and 38 required assertion declarations. Tested cases are synthetic only. Required UNSUPPORTED or INDETERMINATE blocks overall PASS. Exact tested fields are in docs/fields.md, and unexamined fields are reported.

100 synthetic paired cases; 140 passing tests; 99/102 core semantic branches (97.06%); 40/40 targeted mutants killed; 200 XML documents with matching XSD classifications across lxml and xmlschema; 100,000 parser fuzz iterations and 10,000 contract mutations.

Unsupported: camt.053.001.08 (uncleared joint-contributor redistribution), other exact versions, universal translation, whole-document equivalence, arbitrary executable contracts and adapter execution. No Ethiopian scheme rules, proprietary SWIFT usage guidelines or live-bank data are included.

No NBE/EthSwitch/SWIFT/ISO or foundation approval, certification, production-safety claim or national-standard status. No independent external review is claimed until actual review evidence is authenticated. OIDC signatures prove workflow identity and artifact integrity, not financial correctness.

Read [threat model](../docs/threat-model.md), [rights register](../evidence/rights-register.json), [reproduction guide](../docs/reproduce.md), [security evidence](../SECURITY-EVIDENCE.md), [Scorecard remediation](../docs/scorecard-remediation.md), and [Best Practices application preparation](../docs/openssf-best-practices-submission.md). Badge status is only earned when the official system grants it.

No known assigned vulnerability in MessageBench itself is advertised as fixed in this candidate. Dependency/native review scope is documented separately. No production-support warranty or stable public API is promised.
