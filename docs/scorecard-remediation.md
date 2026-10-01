# Public OpenSSF Scorecard

Status is read from evidence/scorecard-public.json and external/recognition-matrix.json. No score or badge is claimed before an actual public result. The official action is pinned to the resolved v2.4.4 commit and uses publish_results: true, with OIDC restricted to its job. Its workflow has no top-level environment/defaults, no script steps in the Scorecard job and no untrusted pull_request_target.

The official action performs the public scan; its published standard result is recorded separately from local full-check execution. Public action defaults may not enable every check, so a separate full CLI scan is required to account for checks absent from the published result. Never relabel skipped/error checks as passes.

Remediate actual weaknesses: enforced PR review and status checks, force-push restrictions, vulnerability reporting, SHA pins, dependency updates, SAST and authentic provenance. Do not create fake contributors, PRs, downloads or history for metrics. Branch-protection evidence visibility may depend on scanner credentials; distinguish a negative result from an API permission error.

Passing Best Practices badge and Scorecard are separate programs. A prepared application supplies no Badge-Check credit. CII/Best Practices and contributor/history scores may remain limited until real human operation occurs. Native advisory review is separate from the Python audit. An absent packaging/upload operation is not evidence of unsafe packaging.
