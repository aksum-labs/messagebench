# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
import copy
import json

import pytest

from aksum_messagebench.assets import data_root
from aksum_messagebench.contracts import load_contract
from aksum_messagebench.engine import compare
from aksum_messagebench.errors import BenchError
from aksum_messagebench.workflows import regression, validate_result


def keyed_contract(tmp_path):
    root = data_root()
    doc = json.loads((root / "contracts/pacs008-extended.json").read_text())
    for a in doc["assertions"]:
        if a["cardinality"] == "per-transaction":
            a["item_comparator"] = a["comparator"]
            a["comparator"] = "keyed-items"
    path = tmp_path / "keyed.json"
    path.write_text(json.dumps(doc))
    return path


def test_declared_keyed_comparator(tmp_path):
    contract = keyed_contract(tmp_path)
    base = data_root() / "corpus/extended"
    for case, expected in [
        ("batch-reordered", 0),
        ("batch-amount-swapped", 1),
        ("batch-duplicate-key", 3),
    ]:
        result = compare(base / (case + ".source.xml"), base / (case + ".target.xml"), contract)
        assert result["exit_code"] == expected
        validate_result(result)
        assert all(
            "item_comparator" in a for a in result["assertions"] if a["comparator"] == "keyed-items"
        )
    before = compare(base / "batch-control.source.xml", base / "batch-control.target.xml", contract)
    after = copy.deepcopy(before)
    next(a for a in after["assertions"] if "item_comparator" in a)["item_comparator"] = (
        "presence-equal"
    )
    assert regression(before, after)["exit_code"] == 3


def test_keyed_requires_explicit_semantics(tmp_path):
    path = keyed_contract(tmp_path)
    doc = json.loads(path.read_text())
    del next(a for a in doc["assertions"] if "item_comparator" in a)["item_comparator"]
    path.write_text(json.dumps(doc))
    with pytest.raises(BenchError, match="CONTRACT_INVALID"):
        load_contract(path)
    path = keyed_contract(tmp_path)
    doc = json.loads(path.read_text())
    doc["association"] = {"mode": "single"}
    path.write_text(json.dumps(doc))
    with pytest.raises(BenchError, match="CONTRACT_KEYED_ASSOCIATION_REQUIRED"):
        load_contract(path)
