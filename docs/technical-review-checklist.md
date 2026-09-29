# External technical review handoff

**Status: BLOCKED-BY-HUMAN.** The implementation author cannot supply independent review.

An external reviewer receives the source archive, offline wheelhouse, corresponding native
sources, SBOM, checksum manifest, build provenance and FINAL_COMPLETION_REPORT.md. Start in a
new directory/environment; verify hashes and install with --no-index and --require-hashes.
Run the reference-loss demonstration, unchanged control, 100-case corpus, differential XSD
checks and the one-command technical checks. Record the actual environment, commands and outputs.

Review these boundaries explicitly:

- Pair preservation versus single-message validity; allowed regeneration and absent values.
- Unique-key association and refusal to guess; timestamp precision and timezone uncertainty.
- Coverage accounting, unknown fields, unsupported extensions and incomplete evidence.
- XML/parser/schema/file quotas; runtime process limits; report redaction and escaping.
- Closed contracts and report consistency; no adapter execution, network runtime or institution probing.
- Native component patches/advisories, source correspondence, LGPL obligations and separate XSD terms.
- Reproducible unsigned artifacts versus authenticated signing/independent reproduction.
- Workflow privilege boundaries, genuine review records, owner settings and forbidden claims.

Return real reviewer identity/affiliation, independence declaration, source commit, packet
hash, findings with severity/reproduction, decisions per acceptance gate, and approval or
requested changes. A maintainer records and resolves findings before publication. Do not call
an author-run fresh environment an independent external reproduction.
