# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
"""Generate an owner-executed GitHub setup plan. Never contact or mutate GitHub."""

import argparse
import json
import re
from pathlib import Path


def plan(repository, maintainers, reviewer_ids):
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
        raise ValueError("Expected OWNER/REPOSITORY")
    if len({h.casefold() for h in maintainers}) < 2 or any(
        not re.fullmatch(r"[A-Za-z0-9-]+", h) for h in maintainers
    ):
        raise ValueError("At least two distinct real maintainer handles required")
    if len(set(reviewer_ids)) < 2 or any(i <= 0 for i in reviewer_ids):
        raise ValueError("At least two distinct real GitHub reviewer IDs required")
    return {
        "repository": repository,
        "repository-settings.json": {
            "description": "Offline preservation-contract tests for financial-message adapters",
            "has_issues": True,
            "has_wiki": False,
            "allow_merge_commit": False,
            "allow_squash_merge": True,
            "allow_rebase_merge": False,
            "delete_branch_on_merge": True,
        },
        "branch-protection.json": {
            "required_status_checks": {"strict": True, "contexts": ["checks", "dependencies"]},
            "enforce_admins": True,
            "required_pull_request_reviews": {
                "dismiss_stale_reviews": True,
                "require_code_owner_reviews": True,
                "required_approving_review_count": 2,
                "require_last_push_approval": True,
            },
            "restrictions": None,
            "required_linear_history": True,
            "allow_force_pushes": False,
            "allow_deletions": False,
            "required_conversation_resolution": True,
        },
        "release-environment.json": {
            "wait_timer": 0,
            "prevent_self_review": True,
            "reviewers": [{"type": "User", "id": i} for i in reviewer_ids],
            "deployment_branch_policy": {
                "protected_branches": False,
                "custom_branch_policies": True,
            },
        },
        "release-main-policy.json": {"name": "main", "type": "branch"},
        "release-tag-policy.json": {"name": "v0.2.0-rc.1", "type": "tag"},
        "release-tag-creation.json": {
            "name": "Reviewed release tag creation",
            "target": "tag",
            "enforcement": "active",
            "conditions": {"ref_name": {"include": ["refs/tags/v*"], "exclude": []}},
            "bypass_actors": [
                {"actor_type": "User", "actor_id": i, "bypass_mode": "always"} for i in reviewer_ids
            ],
            "rules": [{"type": "creation"}],
        },
        "release-tag-immutability.json": {
            "name": "Immutable release tags",
            "target": "tag",
            "enforcement": "active",
            "conditions": {"ref_name": {"include": ["refs/tags/v*"], "exclude": []}},
            "bypass_actors": [],
            "rules": [
                {"type": "update", "parameters": {"update_allows_fetch_and_merge": False}},
                {"type": "deletion"},
            ],
        },
        "topics.json": {
            "names": [
                "iso20022",
                "financial-messaging",
                "testing",
                "offline",
                "payment-infrastructure",
                "python",
                "open-source",
            ]
        },
        "CODEOWNERS": "* " + " ".join("@" + h for h in maintainers) + "\n",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--maintainer", action="append", required=True)
    parser.add_argument("--reviewer-id", type=int, action="append", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    result = plan(args.repo, args.maintainer, args.reviewer_id)
    args.out.mkdir(parents=True, exist_ok=False)
    for name, value in result.items():
        if name == "repository":
            continue
        (args.out / name).write_text(
            value if isinstance(value, str) else json.dumps(value, indent=2) + "\n"
        )
    commands = [
        "# Owner-only handoff; inspect files and approve publication before executing.",
        (
            "# Create/push the public repository only after independent approval. "
            "No command below creates it."
        ),
        "# Commit generated CODEOWNERS to .github/CODEOWNERS through a reviewed PR first.",
        f"gh api --method PATCH repos/{args.repo} --input repository-settings.json",
        f"gh api --method PUT repos/{args.repo}/topics --input topics.json",
        (
            f"gh api --method PUT repos/{args.repo}/branches/main/protection "
            "--input branch-protection.json"
        ),
        (
            f"gh api --method PUT repos/{args.repo}/environments/release-review "
            "--input release-environment.json"
        ),
        (
            f"gh api --method POST repos/{args.repo}/environments/release-review/"
            "deployment-branch-policies --input release-main-policy.json"
        ),
        (
            f"gh api --method POST repos/{args.repo}/environments/release-review/"
            "deployment-branch-policies --input release-tag-policy.json"
        ),
        "# Verify existing policies first; do not create duplicate policies on repeated setup.",
        "# Owner must disable administrator bypass in environment settings and read it back.",
        f"gh api --method PUT repos/{args.repo}/private-vulnerability-reporting",
        (f"gh api --method POST repos/{args.repo}/rulesets --input release-tag-creation.json"),
        (f"gh api --method POST repos/{args.repo}/rulesets --input release-tag-immutability.json"),
        (
            "# Enable RELEASE_PREPARATION_ENABLED and RELEASE_SIGNING_ENABLED "
            "only after authentic reviews"
        ),
        (
            "# and protected release-review configuration. "
            "Workflow dispatch then prepares/signs; it does not publish."
        ),
        f"gh api repos/{args.repo}/branches/main/protection",
        f"gh api repos/{args.repo}/environments/release-review",
        f"gh api repos/{args.repo}/environments/release-review/deployment-branch-policies",
        f"gh api repos/{args.repo}/private-vulnerability-reporting",
    ]
    (args.out / "OWNER_COMMANDS.sh").write_text("\n".join(commands) + "\n")
    print("Prepared owner plan; zero GitHub calls performed.")


if __name__ == "__main__":
    main()
