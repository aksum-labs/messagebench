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
    manifest = ROOT / "corpus/gate1-index.json"
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
    assert suite(ROOT / "corpus/gate1-index.json", tmp_path, CONTRACT)["exit_code"] == 4


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
    assert len(result["cases"]) == 54
    assert result["exit_code"] == 0
    assert result["independent_review_verified"] is False


def test_status_report_corpus():
    from aksum_messagebench.corpus import verify

    result = verify(ROOT / "corpus/pacs002/index.json", ROOT / "contracts/pacs002-preserve.json")
    assert len(result["cases"]) == 8
    assert result["exit_code"] == 0


def test_suite_report_formats_and_regression(tmp_path):
    from xml.etree import ElementTree

    from aksum_messagebench.reports import canonical_json, render

    value = suite(ROOT / "corpus/gate1-index.json", tmp_path, CONTRACT)
    path = tmp_path / "suite.json"
    path.write_bytes(canonical_json(value))
    loaded = load_result(path)
    assert regression(loaded, loaded)["exit_code"] == 3
    junit = ElementTree.fromstring(render(loaded, "junit"))
    assert int(junit.attrib["errors"]) > 0
    assert b"INDETERMINATE" in render(loaded, "html")
    assert b"identity" in render(loaded, "text")
    value["overall"] = "PASS"
    value["exit_code"] = 0
    path.write_bytes(canonical_json(value))
    with pytest.raises(BenchError, match="REPORT_STATUS_INCONSISTENT"):
        load_result(path)


def test_forged_schema_success_cannot_bypass_required_unknown(tmp_path):
    value = report()
    value["schema_checks"]["source"]["status"] = "FAIL"
    for assertion in value["assertions"]:
        assertion["status"] = "INDETERMINATE"
    path = tmp_path / "forged.json"
    path.write_text(json.dumps(value))
    with pytest.raises(BenchError, match="REPORT_SCHEMA_STATUS_INCONSISTENT"):
        load_result(path)


def test_multi_namespace_contract_selects_actual_source_version(tmp_path):
    contract = json.loads((ROOT / "contracts/pacs002-preserve.json").read_text())
    primary = "urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08"
    contract["source_namespaces"].insert(0, primary)
    contract["target_namespaces"].insert(0, primary)
    path = tmp_path / "contract.json"
    path.write_text(json.dumps(contract))
    fixture = ROOT / "corpus/pacs002/identity.source.xml"
    result = compare(fixture, fixture, path)
    assert result["exit_code"] == 0
    assert (
        result["schema_sha256"]
        == "d14da6304db5178b1afc7d8ed6cc6073e6e1a143fc79d9ba66d3246d4a654e90"
    )


def test_release_corpus_selects_versioned_contracts():
    from aksum_messagebench.corpus import verify

    result = verify(ROOT / "corpus/index.json")
    assert len(result["cases"]) == 100
    assert result["exit_code"] == 0
