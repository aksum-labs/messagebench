# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
import copy
import json

import pytest
from lxml import etree

from aksum_messagebench.assets import data_root
from aksum_messagebench.engine import compare
from aksum_messagebench.extractors.pacs008_001_08 import Q

ROOT = data_root()


def batch():
    root = etree.fromstring((ROOT / "corpus/positive/identity.source.xml").read_bytes())
    body = root[0]
    body.find(Q + "GrpHdr/" + Q + "NbOfTxs").text = "2"
    tx = copy.deepcopy(body.find(Q + "CdtTrfTxInf"))
    tx.find(Q + "PmtId/" + Q + "EndToEndId").text = "SECOND-REF"
    tx.find(Q + "IntrBkSttlmAmt").text = "99.99"
    body.append(tx)
    return root


def run(tmp_path, source, target, keys=None):
    contract = json.loads((ROOT / "contracts/pacs008-preserve.json").read_text())
    contract["association"] = {"mode": "keyed", "keys": keys or ["transactions.end_to_end_id"]}
    cp = tmp_path / "contract.json"
    cp.write_text(json.dumps(contract))
    before, after = tmp_path / "before.xml", tmp_path / "after.xml"
    before.write_bytes(etree.tostring(source))
    after.write_bytes(etree.tostring(target))
    return compare(before, after, cp)


def test_reorder_is_not_loss(tmp_path):
    source = batch()
    target = copy.deepcopy(source)
    target[0].append(target[0][1])
    result = run(tmp_path, source, target)
    assert result["exit_code"] == 0


def test_amount_swap_does_not_hide_loss(tmp_path):
    source = batch()
    target = copy.deepcopy(source)
    amounts = target.findall(".//" + Q + "IntrBkSttlmAmt")
    amounts[0].text, amounts[1].text = amounts[1].text, amounts[0].text
    result = run(tmp_path, source, target)
    assert result["exit_code"] == 1
    assert [a["id"] for a in result["assertions"] if a["status"] == "FAIL"] == [
        "PRESERVE-SETTLEMENT-AMOUNT"
    ]


@pytest.mark.parametrize("mode", ["duplicate", "changed", "unsupported"])
def test_ambiguous_or_unsupported_association_never_passes(tmp_path, mode):
    source = batch()
    target = copy.deepcopy(source)
    refs = target.findall(".//" + Q + "EndToEndId")
    keys = None
    if mode == "duplicate":
        refs[1].text = refs[0].text
    elif mode == "changed":
        refs[1].text = "CHANGED-KEY"
    else:
        keys = ["transactions.remittance"]
    result = run(tmp_path, source, target, keys)
    assert result["exit_code"] == 3
    assert result["schema_checks"]["target"]["status"] == "PASS"
