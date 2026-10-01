"""Fail closed before tag release when public platform protections are absent.

Developer/CI tooling only; never imported by the offline MessageBench runtime.
"""

import json
import os
import urllib.error
import urllib.request
from pathlib import Path

REPOSITORY = "aksum-labs/messagebench"
REF = "refs/tags/v0.2.0-rc.1"
TEAM_ID = 19826182


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


def main():
    if os.environ.get("GITHUB_REPOSITORY") != REPOSITORY or os.environ.get("GITHUB_REF") != REF:
        raise ValueError("Exact repository and reviewed tag required")
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


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError, urllib.error.URLError):
        raise SystemExit(
            "Release blocked: public platform controls unavailable or unsafe"
        ) from None
