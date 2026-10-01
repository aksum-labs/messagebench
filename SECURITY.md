# Security

Status: public engineering release candidate; no production-support warranty or reviewed formal release.

Report a suspected vulnerability through [GitHub private vulnerability reporting](https://github.com/aksum-labs/messagebench/security/advisories/new). The private reporting channel is enabled and was read back through the company App. Do not put private messages, account identifiers, raw customer data or secrets in issues, reports or CI artifacts.

Provide the exact version/commit, a minimal synthetic reproduction, expected and observed behavior, impact and suggested mitigation. The company maintainer team receives the repository's private reports. Maintainers should acknowledge within 7 days, triage within 14 days and coordinate disclosure and patched releases. These are response objectives, not evidence of staffed response history; an accountable human must operate the process.

See the [threat model](docs/threat-model.md), [limitations](LIMITATIONS.md), [security evidence](SECURITY-EVIDENCE.md) and [private reporting instructions](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/privately-reporting-a-security-vulnerability). Native XML-library advisories must be reviewed separately from Python pip-audit. Never attach production inputs to scans.
