# MessageBench — technical brief
## Declared preservation at the adapter boundary

MessageBench is an offline toolkit for asking whether financial-message adapters preserved the information they explicitly promised to preserve. Engineers supply source and target files; MessageBench runs no adapter and connects to no financial system. It produces deterministic, privacy-conscious results with visible coverage limits.

### What the demonstration establishes

Two XML messages can both pass an exact XSD while a reference is truncated, a leading zero is removed or a repeated remittance element disappears. The synthetic proof pairs demonstrate these losses. Identity and explicitly permitted message-ID regeneration pass. Schema validators are performing their intended task; MessageBench adds a relationship check rather than replacing them.

### Technical scope

Candidate 0.2.0-rc.1 supports pacs.008.001.08 and pacs.002.001.10. Ten contracts contain 38 required assertion declarations over 27 extractable fields. A required UNSUPPORTED or INDETERMINATE check prevents overall PASS. Coverage distinguishes examined, excluded, unsupported and unexamined information. A PASS covers only listed assertions, never the whole document.

The architecture is bounded local files → secure XML/exact XSD → version-specific facts → typed declarative contract → comparison/coverage → JSON, text, escaped HTML or JUnit. Identifiers stay strings, amounts use Decimal with separate currency semantics, repeated elements retain multiplicity and normalization is explicit. Batch association requires declared unique keys.

### Measured synthetic evidence

100 paired cases; 140 tests; 99/102 selected core semantic branches covered; 40/40 defined targeted mutants killed; two XSD processors agree across 200 documents; 100,000 parser fuzz iterations and 10,000 contract mutations completed. These are automated measurements against curated expectations, not independently reviewed cases or production defect estimates.

## Evaluation, security and practical limits

### How an institution can evaluate it

Clone https://github.com/aksum-labs/messagebench and record the commit. Follow docs/reproduce.md to install the reviewed profile and run corpus verification, differential validation, mutations and security checks. For a local adapter, emit XML files separately and hand them to MessageBench with an explicit contract. Private inputs stay institution-local and must not be attached to issues or CI.

The prepared Linux x86_64 CPython 3.12 bundle can be installed offline. Canonical report bytes contain no timestamp. Hashes bind assets but do not anonymize financial data. Two matching clean unsigned Python builds in one environment establish same-environment equality, not independent reproduction.

### Security posture

Secure parsing disables DTD/entities/XInclude/network resolution; input size, depth, element count, text size and assertion count are bounded. Contracts contain no executable code or unrestricted XPath. Reports omit raw customer fields and escape HTML. There is no server, telemetry, plugin execution or adapter shell command. Limits are not an OS sandbox, and bounded fuzzing is not exhaustive security assurance.

### Performance context

The historical single-host run cycles six small pairs over 1,000 in-process comparisons, including per-pair schema compilation. It measured 80.624 pairs/s, p50 11.741 ms, p95 15.584 ms and peak RSS 40,360 KiB. This is not an SLA, batch-scale benchmark or cross-product performance comparison.

### Rights, review and recognition

Original code and synthetic corpus use Apache-2.0. The two standard XSDs retain separate terms. camt.053.001.08 is excluded because complete joint-contributor redistribution permission was not established. No independent human review, adoption, official endorsement or certification is claimed. Foundation applications and badges must be checked against actual official results in external/recognition-matrix.json.

This engineering artifact does not implement payment operations, sovereign rails, Ethiopian scheme rules or regulatory authority. Public claims are limited to observed tests, exact scope and authenticated evidence. The next substantive step is independent review of semantics, expectations and rights, followed by actual maintainership and constructive upstream use.
