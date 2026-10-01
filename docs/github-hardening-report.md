# GitHub hardening — actual settings and remaining enforcement

Repository: https://github.com/aksum-labs/messagebench. Public source at commit `2bb62cb1e0dcbbb91d265bb824eda274cbd9b217` was published through the organization-owned App. The App permission update and installation approval succeeded; they are no longer owner blockers.

Actual read-back is in evidence/github-settings.json. Verified: public visibility; main default; description/topics; issues/discussions; no wiki; squash-only merge; private vulnerability reporting; secret scanning and push protection; default Actions token read-only and unable to approve PRs; immutable-release setting enabled. Dependabot configuration, CodeQL, dependency review and SHA-pinned workflows are public and successful hosted evidence is in evidence/hosted-recognition.json.

The company team has write access and is organization-visible (GitHub closed visibility), allowing CODEOWNERS. Its membership is not public. GitHub returned no CODEOWNERS errors after this change. One actual member is not two independent reviewers. Corporate author/committer metadata and company-bot pushes protect the owner's requested public attribution boundary; account ownership is not an anonymity guarantee to GitHub.

## Controls not yet enforced

Last App read-back: no main branch protection (404), no tag rulesets; release-review environment exists but has no reviewer protection. A successful initial environment creation is not approval enforcement. Dependabot security updates report disabled; configuration for scheduled updates is separate. Do not describe these controls as enabled.

Prepared operator commands are configure/protect/verify in the outside-repository recognition_github.py tool. Main protection requests strict checks checks, dependencies, dependency-review and analyze, one code-owner approval, stale approval dismissal, approval after last push, admin enforcement, no force push or deletion, linear history and resolved conversations. Version tags use an immutable update/deletion ruleset. Required release environment reviewers must be read back, with self-review and admin bypass prevented.

Current execution environment rejects company-App networking with temporary DNS failure. The read-only connected GitHub integration can inspect hosted evidence but cannot administer the repository, and personal-account writes would violate the requested publication identity. Therefore final local evidence upload and remaining settings are BLOCKED-BY-EXTERNAL-PARTY, not falsely labeled configured. Re-enable company-App networking, publish the prepared changes before enforcement, apply settings, read them back and rerun CI/Scorecard for the exact new commit.

Organization MFA was false at inspection. Owner must establish real maintainer MFA readiness and policy. App registration currently has extra permissions; every token issued for this task is restricted to MessageBench and requested permissions. Owner should reduce the registered App grant to the documented actual scope. Neither MFA nor globally narrow App registration is claimed.

Formal release and independent review remain genuine human gates. No approval bypass, forged review or fake maintenance history is authorized.

Follow-up release audit: exact Selected branches and tags policies for main and v0.2.0-rc.1 are prepared. A new tag-release guard checks actual public controls before each privileged stage, with nine additional synthetic control tests (149 local tests total). Actual platform enforcement is still unverified because company-App networking is blocked. See docs/release-publication.md and evidence/local-release-preparation.json.
