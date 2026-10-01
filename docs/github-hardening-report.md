# GitHub hardening — verified public controls

Actual settings: evidence/github-settings.json. Public main source: ad10253e1d0d9a07282ab78290f024cdbf5a111b; company actor aksum-labs-publisher[bot]. App installation permissions are accepted and networking has recovered.

Verified by App GET read-back: public visibility, main default, issues/discussions, squash-only merging, no wiki, private vulnerability reporting, secret scanning/push protection, Dependabot security updates, read-only default Actions token and no workflow approval permission, immutable-release setting. Main requires strict checks (checks, dependencies, dependency-review, analyze), code-owner review, approval after the last push, stale approval dismissal, linear history and resolved conversations. Administrators are subject to protection; force pushes and deletions are disabled. Version-tag updates/deletion are blocked by an active ruleset with no bypass actors.

The release environment requires the company maintainer team, prevents self-review and administrator bypass, and admits exactly branch main and tag v0.2.0-rc.1. The API accepted can_admins_bypass:false and actual read-back proved it, despite that input not being listed in the inspected documentation. No owner toggle is still requested. Pages workflow deployment and actual HTML are verified at https://aksum-labs.github.io/messagebench/; evidence/github-pages-settings.json records the exact source/body hash and successful deployment run.

Read-only rule endpoints omit bypass_actors. The company App used the necessary administrative scope to capture evidence/tag-rules-admin-readback.json; the release guard compares its identity/version/public fields to current API data before using the recorded bypass list. A change or missing record fails closed. No write-capable App secret is supplied to CI. Actual platform validation: evidence/release-controls-live-verification.json. This does not authenticate human reviewers.

Corporate commit metadata and company-App pushes protect the requested public attribution boundary. The company team is organization-visible; its membership is not public. One team member is not two independent reviewers. No fake review, history or activity was generated.

Organization MFA remains an owner/account-readiness decision. The App registration includes extra permissions; issued tokens are repository-restricted and purpose-scoped. Owner should reduce registered grants after confirming required automation capabilities. Formal release still requires two genuine independent review decisions and protected human approval.

With main protected, final facts and the guard correction are published through a company-bot PR. Human review/merge is intentional; no direct push or bypass is used. Current CI and Scorecard evidence distinguishes main source from that review branch.
