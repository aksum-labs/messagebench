# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
import hashlib
import json

import pytest
from lxml import etree

from aksum_messagebench.corpus import verify
from aksum_messagebench.engine import compare
from aksum_messagebench.reports import canonical_json


def test_preimplementation_expectations(root):
    digest = (root / "evidence/expectations-preimplementation.sha256").read_text().split()[0]
    assert hashlib.sha256((root / "corpus/gate1-index.json").read_bytes()).hexdigest() == digest
    result = verify(root / "corpus/gate1-index.json")
    assert len(result["cases"]) == 6
    assert result["exit_code"] == 0
    assert result["independent_review_verified"] is False


def test_all_pairs_deterministic(root, contract):
    cases = json.loads((root / "corpus/gate1-index.json").read_text())["cases"]
    for case in cases:
        before = root / "corpus" / case["source"]
        after = root / "corpus" / case["target"]
        first = compare(before, after, contract)
        assert canonical_json(first) == canonical_json(compare(before, after, contract))
        assert first["overall"] == case["expected"]["overall"]
        for side in ("source", "target"):
            coverage = first["coverage"][side]
            assert sum(c["count"] for c in coverage["categories"].values()) == coverage["total"]
            assert coverage["categories"]["unexamined"]["count"] > 0


def test_regeneration_is_contract_specific(source, contract, root, change_contract):
    after = root / "corpus/positive/message-id-regenerated.target.xml"
    assert compare(source, after, contract)["overall"] == "PASS"
    strict = change_contract(lambda d: d["assertions"][0].update(comparator="exact-identifier"))
    assert compare(source, after, strict)["overall"] == "FAIL"


def test_missing_output(source, contract, tmp_path):
    result = compare(source, tmp_path / "missing.xml", contract)
    assert result["exit_code"] == 3
    assert result["overall"] != "PASS"


@pytest.mark.parametrize(
    "edit,want",
    [
        (lambda d: d["assertions"][0].update(field="message.unknown"), 3),
        (lambda d: d["assertions"][1].update(comparator="decimal-equal"), 3),
        (lambda d: d["assertions"][1].update(cardinality="single"), 3),
        (lambda d: d.update(source_namespaces=["urn:unsupported"]), 3),
        (
            lambda d: d.update(association={"mode": "keyed", "keys": ["transactions.unknown_key"]}),
            3,
        ),
    ],
)
def test_unavailable_required_check_blocks_pass(source, change_contract, edit, want):
    result = compare(source, source, change_contract(edit))
    assert result["exit_code"] == want
    assert result["overall"] != "PASS"


def test_batch_never_positionally_paired(source, contract, tmp_path):
    root = etree.fromstring(source.read_bytes())
    tx = root[0][-1]
    root[0].append(etree.fromstring(etree.tostring(tx)))
    root[0][0][2].text = "2"
    target = tmp_path / "batch.xml"
    target.write_bytes(etree.tostring(root))
    result = compare(target, target, contract)
    assert result["schema_checks"]["target"]["status"] == "PASS"
    assert result["exit_code"] == 3


def test_prefix_metamorphism(source, contract, tmp_path):
    xml = source.read_bytes().decode()
    # Re-serialize under an arbitrary prefix without changing expanded QNames.
    tree = etree.fromstring(xml.encode())
    ns = etree.QName(tree).namespace
    replacement = etree.Element(tree.tag, nsmap={"mx": ns})
    replacement.extend(list(tree))
    target = tmp_path / "prefix.xml"
    target.write_bytes(etree.tostring(replacement))
    assert compare(source, target, contract)["overall"] == "PASS"


def test_invalid_schema_and_security_precedence(source, contract, tmp_path):
    bad = tmp_path / "bad.xml"
    bad.write_bytes(source.read_bytes().replace(b"<NbOfTxs>1</NbOfTxs>", b""))
    result = compare(source, bad, contract)
    assert result["exit_code"] == 1
    assert result["schema_checks"]["target"]["code"] == "XSD_INVALID"
    bad.write_bytes(b'<!DOCTYPE x SYSTEM "file:///etc/passwd"><x/>')
    assert compare(tmp_path / "missing", bad, contract)["exit_code"] == 4


def test_report_privacy(source, contract):
    encoded = canonical_json(compare(source, source, contract))
    for value in [
        b"Fictional Payer",
        b"0000123400",
        b"1250.50",
        b"INV-2026-000123",
        "ሙከራ".encode(),
        b"<Document",
    ]:
        assert value not in encoded
