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
            }
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
    guard.validate(*platform_control_fixture()[:4], bound)


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
