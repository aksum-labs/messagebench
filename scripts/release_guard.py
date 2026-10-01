# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
"""Fail closed before tag release when public platform protections are absent.

Developer/CI tooling only; never imported by the offline MessageBench runtime.
"""

import hashlib
import json
import os
import urllib.error
import urllib.request
from pathlib import Path

REPOSITORY = "aksum-labs/messagebench"
REF = "refs/tags/v0.2.0-rc.1"
TEAM_ID = 19826182
CHECKS = {"checks", "dependencies", "dependency-review", "analyze", "release-controls"}
ACTIONS_APP_ID = 15368


def bind_admin_readback(rulesets, readback):
    """Bind hidden bypass data to an actual reviewed, version-matched App record."""
    if (
        readback.get("repository") != REPOSITORY
        or readback.get("actor") != "aksum-labs-publisher[bot]"
    ):
        raise ValueError("Exact privileged App read-back required")
    saved = {rule["id"]: rule for rule in readback.get("rulesets", [])}
    fields = (
        "id",
        "name",
        "source_type",
        "source",
        "target",
        "enforcement",
        "conditions",
        "rules",
        "created_at",
        "updated_at",
    )
    bound = []
    for rule in rulesets:
        if "bypass_actors" in rule:
            bound.append(rule)
            continue
        previous = saved.get(rule.get("id"))
        if (
            not previous
            or not previous.get("updated_at")
            or "bypass_actors" not in previous
            or any(rule.get(key) != previous.get(key) for key in fields)
        ):
            raise ValueError("Privileged tag read-back is missing or stale")
        bound.append({**rule, "bypass_actors": previous["bypass_actors"]})
    return bound


def validate_main_rules(rulesets):
    """Verify publicly readable full branch policy, including bound bypass evidence."""
    for rule in rulesets:
        if not (
            rule.get("target") == "branch"
            and rule.get("enforcement") == "active"
            and rule.get("bypass_actors") == []
            and rule.get("conditions", {}).get("ref_name")
            == {"include": ["refs/heads/main"], "exclude": []}
        ):
            continue
        rules = {entry["type"]: entry for entry in rule.get("rules", [])}
        if not {"deletion", "non_fast_forward", "required_linear_history"} <= rules.keys():
            continue
        review = rules.get("pull_request", {}).get("parameters", {})
        checks = rules.get("required_status_checks", {}).get("parameters", {})
        expected = {(name, ACTIONS_APP_ID) for name in CHECKS}
        actual = {
            (entry.get("context"), entry.get("integration_id"))
            for entry in checks.get("required_status_checks", [])
        }
        if (
            expected <= actual
            and checks.get("strict_required_status_checks_policy") is True
            and review.get("required_approving_review_count", 0) >= 1
            and all(
                review.get(key) is True
                for key in (
                    "dismiss_stale_reviews_on_push",
                    "require_code_owner_review",
                    "require_last_push_approval",
                    "required_review_thread_resolution",
                )
            )
        ):
            return
    raise ValueError("Complete reviewed main policy is absent")


def validate_release_source(tag, main_sha, source_sha, checks, accepted_prs):
    """Exact accepted source and exact-source green checks; never reuse old green evidence."""
    if (
        not isinstance(source_sha, str)
        or len(source_sha) != 40
        or tag.get("object") != {"type": "commit", "sha": source_sha}
        or main_sha != source_sha
    ):
        raise ValueError("Release must target the exact currently accepted main commit")
    latest = {}
    for check in checks:
        if check.get("app", {}).get("id") == ACTIONS_APP_ID:
            name = check.get("name")
            if name not in latest or check.get("id", 0) > latest[name].get("id", 0):
                latest[name] = check
    passed = {
        check.get("name")
        for check in latest.values()
        if check.get("head_sha") == source_sha
        and check.get("status") == "completed"
        and check.get("conclusion") == "success"
    }
    if not CHECKS <= passed:
        raise ValueError("Required exact-source checks are missing or unsuccessful")
    if not any(
        pr.get("merged") is True
        and pr.get("merge_commit_sha") == source_sha
        and pr.get("base", {}).get("ref") == "main"
        and pr.get("base", {}).get("repo", {}).get("full_name") == REPOSITORY
        for pr in accepted_prs
    ):
        raise ValueError("Release source lacks a normal protected-main PR acceptance record")


def validate_human_acknowledgment(approvals, packet_sha):
    """Check real platform approval plus scoped human attestation, not human expertise itself."""
    marker = "REVIEWER-IDENTITIES-VERIFIED " + packet_sha
    for approval in approvals:
        if (
            approval.get("state") == "approved"
            and approval.get("user", {}).get("type") == "User"
            and isinstance(approval.get("user", {}).get("id"), int)
            and marker in approval.get("comment", "").splitlines()
            and any(env.get("name") == "release-review" for env in approval.get("environments", []))
        ):
            return
    raise ValueError("Accountable human reviewer-authentication acknowledgment is absent")


def validate(repository, branch, environment, policies, rulesets):
    if repository.get("full_name") != REPOSITORY or repository.get("private") is not False:
        raise ValueError("Exact public repository required")
    if branch.get("name") != "main" or branch.get("protected") is not True:
        raise ValueError("Main branch protection is absent")
    if (
        environment.get("name") != "release-review"
        or environment.get("can_admins_bypass") is not False
        or environment.get("deployment_branch_policy")
        != {"protected_branches": False, "custom_branch_policies": True}
    ):
        raise ValueError("Release environment protection or bypass policy is unsafe")
    reviewers = [
        rule
        for rule in environment.get("protection_rules", [])
        if rule.get("type") == "required_reviewers"
    ]
    if len(reviewers) != 1 or reviewers[0].get("prevent_self_review") is not True:
        raise ValueError("Required review and prevention of self-review are absent")
    if not any(
        entry.get("type") == "Team" and entry.get("reviewer", {}).get("id") == TEAM_ID
        for entry in reviewers[0].get("reviewers", [])
    ):
        raise ValueError("Actual company maintainer team must be a required reviewer")
    actual = {(p.get("name"), p.get("type")) for p in policies.get("branch_policies", [])}
    if actual != {("main", "branch"), ("v0.2.0-rc.1", "tag")}:
        raise ValueError("Only main and the exact release tag may deploy")
    validate_main_rules(rulesets)
    for rule in rulesets:
        condition = rule.get("conditions", {}).get("ref_name", {})
        types = {entry.get("type") for entry in rule.get("rules", [])}
        if (
            rule.get("target") == "tag"
            and rule.get("enforcement") == "active"
            and rule.get("bypass_actors") == []
            and "refs/tags/v*" in condition.get("include", [])
            and condition.get("exclude") == []
            and {"update", "deletion"} <= types
        ):
            return
    raise ValueError("Immutable version tag rules are absent")


def read(path):
    token = os.environ.get("GH_TOKEN")
    if not token:
        raise ValueError("Job-scoped read token is required")
    request = urllib.request.Request(
        "https://api.github.com/repos/" + REPOSITORY + path,
        headers={
            "Authorization": "Bearer " + token,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2026-03-10",
            "User-Agent": "MessageBench-release-control-check",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        raw = response.read(2 * 1024 * 1024 + 1)
    if len(raw) > 2 * 1024 * 1024:
        raise ValueError("Oversized control response")
    return json.loads(raw)


def verify_live_controls():
    """Read and validate platform controls without signing, deploying or publishing."""
    rules = read("/rulesets")
    if not isinstance(rules, list) or len(rules) > 25:
        raise ValueError("Unexpected ruleset collection")
    current = [read("/rulesets/" + str(rule["id"])) for rule in rules]
    readback = json.loads(
        (Path(__file__).resolve().parents[1] / "evidence/tag-rules-admin-readback.json").read_text()
    )
    validate(
        read(""),
        read("/branches/main"),
        read("/environments/release-review"),
        read("/environments/release-review/deployment-branch-policies"),
        bind_admin_readback(current, readback),
    )
    print("Public release control checks passed; this is not independent human review.")


def main():
    if os.environ.get("GITHUB_REPOSITORY") != REPOSITORY or os.environ.get("GITHUB_REF") != REF:
        raise ValueError("Exact repository and reviewed tag required")
    verify_live_controls()
    sha = os.environ.get("GITHUB_SHA")
    tag = read("/git/ref/tags/v0.2.0-rc.1")
    obj = tag.get("object", {})
    if obj.get("type") == "tag":
        obj = read("/git/tags/" + obj["sha"]).get("object", {})
    tag = {"object": {"type": obj.get("type"), "sha": obj.get("sha")}}
    checks = read("/commits/" + str(sha) + "/check-runs?per_page=100")["check_runs"]
    # Reject truncation rather than accepting a potentially incomplete check listing.
    if len(checks) >= 100:
        raise ValueError("Check listing requires a reviewed pagination implementation")
    prs = read("/commits/" + str(sha) + "/pulls?per_page=100")
    accepted = [read("/pulls/" + str(pr["number"])) for pr in prs]
    validate_release_source(tag, read("/branches/main")["commit"]["sha"], sha, checks, accepted)
    packet_bytes = (
        Path(__file__).resolve().parents[1] / "evidence/review-packet.json"
    ).read_bytes()
    approvals = read("/actions/runs/" + str(os.environ.get("GITHUB_RUN_ID")) + "/approvals")
    validate_human_acknowledgment(approvals, hashlib.sha256(packet_bytes).hexdigest())


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError, urllib.error.URLError):
        raise SystemExit(
            "Release blocked: public platform controls unavailable or unsafe"
        ) from None
