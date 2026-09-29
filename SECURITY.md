# Security

Status: unpublished engineering release candidate; no supported production releases. Do not submit private
messages, account identifiers, raw customer data or secrets in issues or CI artifacts.

Before publication, Aksum Labs must appoint a security responder and enable GitHub private
vulnerability reporting (or publish a verified private contact). No unverified email address
is invented here. While this checkout is private, report defects through the existing private
review channel with its owner using a minimal synthetic reproduction. Public reporting is
not a substitute for configuring a private channel.

Provide version/commit, synthetic reproduction, expected and observed behavior, impact and
suggested mitigation. Maintainers should acknowledge within 7 days, triage within 14 days,
and coordinate disclosure and patched releases. These are proposed maintenance objectives,
not an assertion that a staffed response process already exists.

See [threat model](docs/threat-model.md), [limitations](LIMITATIONS.md), and
[GitHub private reporting instructions](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/privately-reporting-a-security-vulnerability).
The owner setup plan enables this channel; its actual activation is BLOCKED-BY-HUMAN. Native XML-library vulnerabilities must be
tracked in addition to Python package advisories. Never attach production inputs to scans.
