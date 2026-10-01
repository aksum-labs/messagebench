# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
import importlib.util
from copy import deepcopy
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]


def script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_review_forms_fail_closed():
    review = script("review_packet")
    packet = review.packet()
    assert review.verify(packet, [])["status"] == "BLOCKED-BY-HUMAN"
    form = {
        "schema_version": "1.0",
        "packet_sha256": "0" * 64,
        "reviewer_handle": "fictional-test-only",
        "reviewer_is_human": False,
        "independent_of_implementation": False,
        "reviewed_at": "",
        "rights_approved": False,
        "scope_approved": False,
        "cases": {},
    }
    with pytest.raises(ValueError):
        review.verify(packet, [form])
    # No fabricated positive human-review records are stored or represented as genuine.


def test_owner_plan_has_protection_and_no_remote_actions():
    owner = script("owner_setup")
    result = owner.plan("EXAMPLE-OWNER/example-repo", ["example-one", "example-two"], [1, 2])
    assert result["branch-protection.json"]["enforce_admins"]
    assert (
        result["branch-protection.json"]["required_pull_request_reviews"][
            "required_approving_review_count"
        ]
        == 2
    )
    assert result["release-environment.json"]["prevent_self_review"]
    assert result["release-environment.json"]["deployment_branch_policy"] == {
        "protected_branches": False,
        "custom_branch_policies": True,
    }
    assert result["release-tag-policy.json"] == {"name": "v0.2.0-rc.1", "type": "tag"}
    for repo, handles, ids in [
        ("bad/repo;cmd", ["a", "b"], [1, 2]),
        ("a/b", ["same", "same"], [1, 2]),
        ("a/b", ["a", "b"], [1, 1]),
    ]:
        with pytest.raises(ValueError):
            owner.plan(repo, handles, ids)


def platform_control_fixture():
    """Synthetic platform data only; does not attest any real review or configuration."""
    return [
        {"full_name": "aksum-labs/messagebench", "private": False},
        {"name": "main", "protected": True},
        {
            "name": "release-review",
            "can_admins_bypass": False,
            "deployment_branch_policy": {
                "protected_branches": False,
                "custom_branch_policies": True,
            },
            "protection_rules": [
                {
                    "type": "required_reviewers",
                    "prevent_self_review": True,
                    "reviewers": [{"type": "Team", "reviewer": {"id": 19826182}}],
                }
            ],
        },
        {
            "branch_policies": [
                {"name": "main", "type": "branch"},
                {"name": "v0.2.0-rc.1", "type": "tag"},
            ]
        },
        [
            {
                "target": "tag",
                "enforcement": "active",
                "bypass_actors": [],
                "conditions": {"ref_name": {"include": ["refs/tags/v*"], "exclude": []}},
                "rules": [{"type": "update"}, {"type": "deletion"}],
            },
            {
                "target": "branch",
                "enforcement": "active",
                "bypass_actors": [],
                "conditions": {"ref_name": {"include": ["refs/heads/main"], "exclude": []}},
                "rules": [
                    {"type": "deletion"},
                    {"type": "non_fast_forward"},
                    {"type": "required_linear_history"},
                    {
                        "type": "pull_request",
                        "parameters": {
                            "dismiss_stale_reviews_on_push": True,
                            "require_code_owner_review": True,
                            "require_last_push_approval": True,
                            "required_review_thread_resolution": True,
                            "required_approving_review_count": 1,
                        },
                    },
                    {
                        "type": "required_status_checks",
                        "parameters": {
                            "strict_required_status_checks_policy": True,
                            "required_status_checks": [
                                {"context": name, "integration_id": 15368}
                                for name in (
                                    "checks",
                                    "dependencies",
                                    "dependency-review",
                                    "analyze",
                                    "release-controls",
                                )
                            ],
                        },
                    },
                ],
            },
        ],
    ]


def test_release_guard_accepts_only_synthetic_complete_controls():
    script("release_guard").validate(*platform_control_fixture())


@pytest.mark.parametrize(
    "defect",
    [
        "wrong-repository",
        "unprotected-main",
        "admin-bypass",
        "no-reviewer",
        "self-review",
        "wildcard-tag",
        "mutable-tag",
        "excluded-tag",
    ],
)
def test_release_guard_rejects_unsafe_platform_controls(defect):
    values = deepcopy(platform_control_fixture())
    if defect == "wrong-repository":
        values[0]["full_name"] = "example/wrong-repository"
    elif defect == "unprotected-main":
        values[1]["protected"] = False
    elif defect == "admin-bypass":
        values[2]["can_admins_bypass"] = True
    elif defect == "no-reviewer":
        values[2]["protection_rules"] = []
    elif defect == "self-review":
        values[2]["protection_rules"][0]["prevent_self_review"] = False
    elif defect == "wildcard-tag":
        values[3]["branch_policies"][1]["name"] = "*"
    elif defect == "mutable-tag":
        values[4][0]["rules"] = [{"type": "update"}]
    elif defect == "excluded-tag":
        values[4][0]["conditions"]["ref_name"]["exclude"] = ["refs/tags/v0.2.0-rc.1"]
    with pytest.raises(ValueError):
        script("release_guard").validate(*values)


def masked_rule_fixture():
    rule = deepcopy(platform_control_fixture()[4][0])
    rule.update(id=123, updated_at="2026-10-01T00:00:00Z")
    hidden = {k: v for k, v in rule.items() if k != "bypass_actors"}
    record = {
        "repository": "aksum-labs/messagebench",
        "actor": "aksum-labs-publisher[bot]",
        "rulesets": [rule],
    }
    return hidden, record


def test_release_guard_binds_only_matching_privileged_rule_version():
    hidden, record = masked_rule_fixture()
    guard = script("release_guard")
    bound = guard.bind_admin_readback([hidden], record)
    guard.validate(*platform_control_fixture()[:4], bound + platform_control_fixture()[4][1:])


@pytest.mark.parametrize("defect", ["missing-record", "changed-version", "changed-scope", "bypass"])
def test_release_guard_rejects_stale_or_unsafe_privileged_records(defect):
    hidden, record = masked_rule_fixture()
    guard = script("release_guard")
    if defect == "missing-record":
        record["rulesets"] = []
    elif defect == "changed-version":
        hidden["updated_at"] = "2026-10-02T00:00:00Z"
    elif defect == "changed-scope":
        hidden["conditions"]["ref_name"]["include"] = ["refs/tags/other*"]
    elif defect == "bypass":
        record["rulesets"][0]["bypass_actors"] = [{"actor_type": "OrganizationAdmin"}]
    with pytest.raises(ValueError):
        guard.validate(*platform_control_fixture()[:4], guard.bind_admin_readback([hidden], record))


@pytest.mark.parametrize(
    "defect", ["wrong-source", "old-check", "missing-check", "wrong-app", "unmerged"]
)
def test_release_guard_exact_source_checks(defect):
    guard = script("release_guard")
    sha = "a" * 40
    tag = {"object": {"type": "commit", "sha": sha}}
    checks = [
        {
            "name": name,
            "head_sha": sha,
            "status": "completed",
            "conclusion": "success",
            "app": {"id": 15368},
        }
        for name in sorted(guard.CHECKS)
    ]
    prs = [
        {
            "merged": True,
            "merge_commit_sha": sha,
            "base": {"ref": "main", "repo": {"full_name": guard.REPOSITORY}},
        }
    ]
    guard.validate_release_source(tag, sha, sha, checks, prs)
    if defect == "wrong-source":
        tag["object"]["sha"] = "b" * 40
    elif defect == "old-check":
        checks[0]["head_sha"] = "b" * 40
    elif defect == "missing-check":
        checks.pop()
    elif defect == "wrong-app":
        checks[0]["app"]["id"] = 1
    else:
        prs[0]["merged"] = False
    with pytest.raises(ValueError):
        guard.validate_release_source(tag, sha, sha, checks, prs)


@pytest.mark.parametrize(
    "defect", ["absent", "missing-check", "wrong-app", "bypass", "no-codeowners"]
)
def test_release_guard_complete_main_policy(defect):
    guard = script("release_guard")
    rules = deepcopy(platform_control_fixture()[4])
    if defect == "absent":
        rules.pop()
    elif defect == "bypass":
        rules[1]["bypass_actors"] = [{"actor_type": "OrganizationAdmin"}]
    elif defect == "no-codeowners":
        rules[1]["rules"][3]["parameters"]["require_code_owner_review"] = False
    elif defect == "wrong-app":
        rules[1]["rules"][4]["parameters"]["required_status_checks"][0]["integration_id"] = 1
    else:
        rules[1]["rules"][4]["parameters"]["required_status_checks"].pop()
    with pytest.raises(ValueError):
        guard.validate_main_rules(rules)


@pytest.mark.parametrize("defect", ["missing", "bot", "wrong-packet", "other-environment"])
def test_release_guard_real_platform_acknowledgment_shape(defect):
    guard = script("release_guard")
    sha = "a" * 64
    fixture = [
        {
            "state": "approved",
            "user": {"type": "User", "id": 123},
            "comment": "REVIEWER-IDENTITIES-VERIFIED " + sha,
            "environments": [{"name": "release-review"}],
        }
    ]
    # Synthetic shape validation only: no actual reviewer record is manufactured.
    guard.validate_human_acknowledgment(fixture, sha)
    if defect == "missing":
        fixture = []
    elif defect == "bot":
        fixture[0]["user"]["type"] = "Bot"
    elif defect == "wrong-packet":
        fixture[0]["comment"] = "REVIEWER-IDENTITIES-VERIFIED " + "b" * 64
    else:
        fixture[0]["environments"][0]["name"] = "other"
    with pytest.raises(ValueError):
        guard.validate_human_acknowledgment(fixture, sha)


def test_newer_failed_exact_source_check_does_not_reuse_older_success():
    guard = script("release_guard")
    sha = "a" * 40
    checks = [
        {
            "name": name,
            "head_sha": sha,
            "status": "completed",
            "conclusion": "success",
            "app": {"id": 15368},
            "id": 1,
        }
        for name in guard.CHECKS
    ]
    checks.append({**checks[0], "id": 2, "conclusion": "failure"})
    pr = {
        "merged": True,
        "merge_commit_sha": sha,
        "base": {"ref": "main", "repo": {"full_name": guard.REPOSITORY}},
    }
    with pytest.raises(ValueError):
        guard.validate_release_source(
            {"object": {"type": "commit", "sha": sha}}, sha, sha, checks, [pr]
        )
