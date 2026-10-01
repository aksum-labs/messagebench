# GitHub hardening and exact read-back

Repository: https://github.com/aksum-labs/messagebench. The owner's 1 October mandate authorizes public source publication. The public project name stays MessageBench; Aksum Labs remains its steward.

Actual configuration and read-back errors are in evidence/github-settings.json. Do not infer visibility, private reporting, rules or environments from prepared YAML or a successful mutation alone. The current company App initially has contents/workflows write and metadata read; Administration and Actions write require owner permission update and installation approval before public actions can be performed without personal attribution.

Configured identity: all source commits use corporate author/committer details. Code uploads use a repository-restricted company App installation token; personal credentials are rejected. The organization-owned secret `messagebench-maintainers` team has one actual member and write access. Its private membership protects the owner's requested public identity boundary; a team does not supply two independent reviewers.

Prepared hardening: main as default; issues/discussions; no wiki; squash-only merge; code owner team; private vulnerability reports; secret scanning/push protection where supported; Dependabot and dependency-review; CodeQL plus Bandit; SHA-pinned actions and read-only defaults; strict status checks and PR review; no force push or deletion; protected release-review environment; immutable version tags and immutable future releases where supported. Apply branch protection after the reviewed bootstrap changes; any temporary bootstrap bypass must be disclosed and removed, not hidden from the assessment.

Human account control: organization MFA requirement is currently false at inspection. Enabling it can affect real members/access and requires owner account readiness; do not invent it as configured. The owner must enroll real maintainers, appoint independent reviewers and configure genuine release approval. Formal release remains gated by authenticated independent review.

Company App API capability errors, missing service support and verification failures are recorded explicitly. The exact configuration tool and payloads are maintained outside the repository; public documentation contains no credentials, private keys or personal identity details.
