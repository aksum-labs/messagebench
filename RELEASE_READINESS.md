# Release readiness

**NOT READY — FIX REQUIRED.** Working version: **0.1.0a1**, a local review artifact.
Not a public alpha, not v0.5, not v1.0. The requested full implementation remains unfinished
because the mandatory independent fixture-review gate has not been satisfied.

Namespace supported: `urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08`.
Fields: group message ID (regeneration permitted), debtor other-account ID, end-to-end ID,
unstructured remittance list, interbank settlement amount and currency. Exact paths and
semantics: README.md and docs/contracts.md. Only explicitly single-transaction association.

Unsupported: all other message versions; keyed batches; cross-message/version equivalence;
timezone/calendar reasoning; account context/scheme/issuer; IBAN alternative; instructed
amount; structured remittance; institutional/scheme usage profiles. Other content remains
unexamined/unsupported. No full-document preservation, business validity or production claim.
Standalone suite/report/regression commands are not implemented; compare has four report formats.

Security: tested conservative parser/file/contract policy, redacted reports; no OS sandbox.
Python advisory scan is not native-library assurance. Native advisory review and independent
technical review remain open. Rights: original code/fixtures Apache-2.0; schema separately
licensed under royalty-free SWIFTStandards terms, with unmodified pinned-mirror provenance.
Full asset/provenance human review is pending.

Publicly supportable statement after accurately disclosing proof status:
“Aksum MessageBench helps financial-software engineers test whether message adapters preserve
declared payment information. It runs offline on synthetic fixtures or institution-local files
and produces reproducible, scope-labelled results.”

Do not claim official Ethiopian conformance, regulator/vendor approval, certification,
production safety, a national standard, independent review, a public release, a security badge,
complete preservation, or v0.5/v1.0 completion. No external reviewer or independent adapter
user has reproduced this work yet. There are six author-reviewed cases, not 60 or 100.

Before publication: satisfy initial review gate, finish the chosen version's functionality
and corpus criteria, run native security/rights review, establish real maintainers/private
reporting, protected CI/releases, independent approval, verifiable signing and release checks.
v1.0 additionally requires stable API, 100 reviewed cases, independent external technical
review/use and governance. None is implied by the local package build.
