# Unsubmitted mx20022 contribution proposal

Status: READY-FOR-OWNER-APPROVAL. Target is a narrow original synthetic pacs.008.001.08 preservation regression, not a MessageBench integration or an allegation of an existing bug.

The patch adds a fixture and two tests to mx20022-parse. One checks lexical leading-zero generic identifiers and duplicate Ethiopic remittance through typed parse/serialize/parse. The other demonstrates observable reference and repeated-item changes in a still-parseable synthetic target. The tests depend only on the upstream model/parser.

Executable evidence: two new Rust tests passed against upstream commit 810cfa2e486745ca3a779c460a7768e1923f860a. Both original and modified inputs pass MessageBench's exact pacs.008.001.08 XSD. These cases complement generic round-trip tests with deliberately significant lexical/multiplicity values. No mx20022 production defect is claimed.

Original additions use Apache-2.0. The inspected repository has no root CONTRIBUTING.md; owner must recheck current submission/rights expectations and provide actual legal contributor attestations before submitting. No fake DCO/CLA or personal public identity is supplied. A company App installed only on MessageBench cannot authorize a public upstream issue/PR on another repository. Do not use the connected personal account to submit without resolving identity and explicit outreach authorization.
