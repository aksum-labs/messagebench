# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
"""Author pacs.002 source/output expectations without executing the preservation oracle."""

import copy
import hashlib
import json
from pathlib import Path

from lxml import etree

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "corpus/pacs002"
Q = "{urn:iso:std:iso:20022:tech:xsd:pacs.002.001.10}"
source = etree.fromstring((OUT / "identity.source.xml").read_bytes())
cases = []


def add(name, target, failed=()):
    pair = {}
    for side, node in [("source", source), ("target", target)]:
        raw = etree.tostring(node, encoding="UTF-8", xml_declaration=True)
        filename = name + "." + side + ".xml"
        (OUT / filename).write_bytes(raw)
        pair[side] = filename
        pair[side + "_sha256"] = hashlib.sha256(raw).hexdigest()
    cases.append(
        {
            "id": name,
            **pair,
            "expected": {
                "overall": "FAIL" if failed else "PASS",
                "exit_code": 1 if failed else 0,
                "failed_assertions": list(failed),
                "source_xsd": "PASS",
                "target_xsd": "PASS",
            },
            "rationale": (
                "Explicit status-report preservation mutation or permitted-change control: " + name
            ),
            "control": "identity",
            "license": "Apache-2.0",
            "provenance": "Original synthetic authoring; no institutional records or scheme rules.",
            "reviewers": [],
        }
    )


add("identity", source)
for name, tag, text, rule in [
    ("regenerated-message-id", "MsgId", "NEW-MESSAGE", None),
    ("original-reference-truncated", "OrgnlEndToEndId", "INV-2026-000", "ORIGINAL-END-TO-END-ID"),
    ("original-transaction-changed", "OrgnlTxId", "CHANGED-TX", "ORIGINAL-TRANSACTION-ID"),
    ("status-changed", "TxSts", "ACSC", "STATUS"),
    ("reason-code-changed", "Cd", "AC04", "REASON-CODES"),
]:
    target = copy.deepcopy(source)
    target.find(".//" + Q + tag).text = text
    add(name, target, ["PRESERVE-" + rule] if rule else [])
target = copy.deepcopy(source)
reason = target.find(".//" + Q + "StsRsnInf")
reason.remove(reason[-1])
add("reason-text-removed", target, ["PRESERVE-REASON-TEXT"])
target = copy.deepcopy(source)
reason = target.find(".//" + Q + "StsRsnInf")
reason.append(reason[1])
add("reason-text-reordered", target)
document = {
    "schema_version": "1.0",
    "version": "0.1.0",
    "review_status": "pending-independent-human-review",
    "cases": cases,
}
raw = (json.dumps(document, indent=2) + "\n").encode()
(OUT / "index.json").write_bytes(raw)
(OUT / "expectations-authored.sha256").write_text(hashlib.sha256(raw).hexdigest() + "\n")
print(f"Authored {len(cases)} cases without running MessageBench")
