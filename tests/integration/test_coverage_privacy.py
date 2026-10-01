# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
import json

from lxml import etree

from aksum_messagebench.assets import data_root
from aksum_messagebench.engine import compare
from aksum_messagebench.reports import canonical_json, render

ROOT = data_root()
CONTRACT = ROOT / "contracts/pacs008-preserve.json"
Q = "{urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08}"


def test_explicit_exclusion_does_not_claim_preservation(tmp_path):
    document = json.loads(CONTRACT.read_text())
    document["assertions"] = [
        a for a in document["assertions"] if a["field"] != "transactions.debtor_account"
    ]
    document["exclusions"] = [
        {"field": "transactions.debtor_account", "reason": "Outside this test scope"}
    ]
    contract = tmp_path / "exclusion.json"
    contract.write_text(json.dumps(document))
    result = compare(
        ROOT / "corpus/negative/leading-zero-loss.source.xml",
        ROOT / "corpus/negative/leading-zero-loss.target.xml",
        contract,
    )
    assert result["exit_code"] == 0
    for side in result["coverage"].values():
        assert side["categories"]["explicitly_excluded"]["count"] == 1
        assert side["categories"]["unexamined"]["count"] > 0


def test_extension_scope_is_explicit():
    result = compare(
        ROOT / "corpus/extended/unsupported-extension-change.source.xml",
        ROOT / "corpus/extended/unsupported-extension-change.target.xml",
        ROOT / "contracts/pacs008-extended.json",
    )
    assert result["exit_code"] == 0
    assert result["coverage"]["source"]["categories"]["unsupported"]["count"] == 1
    assert result["coverage"]["target"]["categories"]["unsupported"]["count"] == 1


def test_html_payload_in_message_is_not_reported(tmp_path):
    source = etree.fromstring((ROOT / "corpus/positive/identity.source.xml").read_bytes())
    sentinel = "<script>PRIVATE-SYNTHETIC-SENTINEL</script>"
    source.find(".//" + Q + "Ustrd").text = sentinel
    path = tmp_path / "synthetic.xml"
    path.write_bytes(etree.tostring(source))
    result = compare(path, path, CONTRACT)
    assert result["exit_code"] == 0
    assert b"PRIVATE-SYNTHETIC-SENTINEL" not in canonical_json(result)
    assert b"PRIVATE-SYNTHETIC-SENTINEL" not in render(result, "html")
