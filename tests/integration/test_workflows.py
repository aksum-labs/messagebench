import copy
import json

import pytest

from aksum_messagebench.assets import data_root
from aksum_messagebench.engine import compare
from aksum_messagebench.errors import BenchError
from aksum_messagebench.workflows import load_result, regression, suite

ROOT = data_root()
CONTRACT = ROOT / "contracts/pacs008-preserve.json"


def test_handoff_missing_and_complete(tmp_path):
    manifest = ROOT / "corpus/index.json"
    result = suite(manifest, tmp_path, CONTRACT)
    assert result["exit_code"] == 3
    assert len(result["cases"]) == 6
    for case in json.loads(manifest.read_text())["cases"]:
        (tmp_path / (case["id"] + ".xml")).write_bytes(
            (manifest.parent / case["source"]).read_bytes()
        )
    result = suite(manifest, tmp_path, CONTRACT)
    assert result["exit_code"] == 0
    assert all(c["result"]["overall"] == "PASS" for c in result["cases"])


def test_handoff_security_precedence(tmp_path):
    (tmp_path / "identity.xml").symlink_to(ROOT / "corpus/positive/identity.target.xml")
    assert suite(ROOT / "corpus/index.json", tmp_path, CONTRACT)["exit_code"] == 4


def report():
    path = ROOT / "corpus/positive/identity.source.xml"
    return compare(path, path, CONTRACT)


def test_report_validation(tmp_path):
    path = tmp_path / "result.json"
    value = report()
    path.write_text(json.dumps(value))
    assert load_result(path) == value
    value["raw_xml"] = "must not be accepted"
    path.write_text(json.dumps(value))
    with pytest.raises(BenchError, match="REPORT_INVALID"):
        load_result(path)


def test_regression_scope_and_improvement():
    before = report()
    after = copy.deepcopy(before)
    assert regression(before, after)["exit_code"] == 0
    after["contract_sha256"] = "a" * 64
    assert regression(before, after)["exit_code"] == 3
    after = copy.deepcopy(before)
    after["assertions"].pop()
    assert regression(before, after)["exit_code"] == 3
    before["exit_code"] = 1
    before["overall"] = "FAIL"
    before["assertions"][0]["status"] = "FAIL"
    assert regression(before, report())["exit_code"] == 0


@pytest.mark.parametrize("mutation", ["status", "coverage", "required"])
def test_report_false_assurance_rejected(tmp_path, mutation):
    value = report()
    if mutation == "status":
        value["assertions"][0]["status"] = "INDETERMINATE"
    elif mutation == "coverage":
        value["coverage"]["source"]["total"] += 1
    else:
        for check in value["assertions"]:
            check["required"] = False
    path = tmp_path / "result.json"
    path.write_text(json.dumps(value))
    with pytest.raises(BenchError):
        load_result(path)


def test_extended_corpus_expectations():
    from aksum_messagebench.corpus import verify

    result = verify(ROOT / "corpus/extended/index.json", ROOT / "contracts/pacs008-extended.json")
    assert len(result["cases"]) == 40
    assert result["exit_code"] == 0
    assert result["independent_review_verified"] is False
