import importlib.util
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
    for repo, handles, ids in [
        ("bad/repo;cmd", ["a", "b"], [1, 2]),
        ("a/b", ["same", "same"], [1, 2]),
        ("a/b", ["a", "b"], [1, 1]),
    ]:
        with pytest.raises(ValueError):
            owner.plan(repo, handles, ids)
