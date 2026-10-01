# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
"""Author 32 semantic scenarios and expectations without calling the oracle."""

import copy
import hashlib
import json
from pathlib import Path

from lxml import etree

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "corpus/semantic"
OUT.mkdir(exist_ok=True)
Q = "{urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08}"
base = etree.fromstring((ROOT / "corpus/positive/identity.source.xml").read_bytes())
base_contract = json.loads((ROOT / "contracts/pacs008-preserve.json").read_text())
cases = []


def field(tree, path):
    node = tree.find(".//" + "/".join(Q + part for part in path.split("/")))
    assert node is not None, path
    return node


def contract(
    name,
    field_name,
    comparator,
    missing="require-present",
    cardinality="single",
    keyed=False,
    normalization="none",
):
    doc = copy.deepcopy(base_contract)
    doc["id"] = "aksum." + name
    doc["version"] = "0.2.0"
    doc["description"] = "Explicit synthetic engineering semantics for " + name
    doc["association"] = (
        {"mode": "keyed", "keys": ["transactions.transaction_id"]} if keyed else {"mode": "single"}
    )
    doc["assertions"] = [
        {
            "id": "PRESERVE-" + name.upper(),
            "field": field_name,
            "comparator": "keyed-items" if keyed else comparator,
            "cardinality": cardinality,
            "missing": missing,
            "required": True,
            "normalization": normalization,
        }
    ]
    if keyed:
        doc["assertions"][0]["item_comparator"] = comparator
    filename = name + ".json"
    (ROOT / "contracts" / filename).write_text(json.dumps(doc, indent=2) + "\n")
    return filename, doc["assertions"][0]["id"]


def add(name, source, target, spec, status="PASS", control=None):
    filename, rule = spec
    paths = {}
    for side, tree in [("source", source), ("target", target)]:
        raw = etree.tostring(tree, xml_declaration=True, encoding="UTF-8")
        path = OUT / (name + "." + side + ".xml")
        path.write_bytes(raw)
        paths[side] = path.name
        paths[side + "_sha256"] = hashlib.sha256(raw).hexdigest()
    cases.append(
        {
            "id": name,
            **paths,
            "contract": filename,
            "expected": {
                "overall": status,
                "exit_code": {"PASS": 0, "FAIL": 1, "INDETERMINATE": 3}[status],
                "failed_assertions": [rule] if status == "FAIL" else [],
                "source_xsd": "PASS",
                "target_xsd": "PASS",
            },
            "rationale": name.replace("-", " ")
            + " under explicitly declared comparator semantics.",
            "control": control or name,
            "license": "Apache-2.0",
            "provenance": (
                "Original synthetic authoring; expected classifications declared "
                "before oracle execution."
            ),
            "reviewers": [],
        }
    )


def changed(tree, path, value):
    result = copy.deepcopy(tree)
    field(result, path).text = value
    return result


time_spec = contract("pacs008-time", "message.created_at", "datetime-equal")
time_source = changed(base, "GrpHdr/CreDtTm", "2026-09-29T12:00:00Z")
add("time-control", time_source, time_source, time_spec)
for name, value, status in [
    ("offset-equivalent", "2026-09-29T15:00:00+03:00", "PASS"),
    ("offset-negative", "2026-09-29T09:00:00-03:00", "PASS"),
    ("instant-shift", "2026-09-29T12:00:01Z", "FAIL"),
    ("timezone-lost", "2026-09-29T12:00:00", "INDETERMINATE"),
    ("fraction-zero", "2026-09-29T12:00:00.000000Z", "PASS"),
    ("submicro-loss", "2026-09-29T12:00:00.0000001Z", "FAIL"),
]:
    add(
        name,
        time_source,
        changed(time_source, "GrpHdr/CreDtTm", value),
        time_spec,
        status,
        "time-control",
    )
midnight = changed(base, "GrpHdr/CreDtTm", "2026-09-29T24:00:00Z")
add("midnight-control", midnight, midnight, time_spec)
add(
    "midnight-equivalent",
    midnight,
    changed(midnight, "GrpHdr/CreDtTm", "2026-09-30T00:00:00Z"),
    time_spec,
    control="midnight-control",
)
add(
    "calendar-day-shift",
    time_source,
    changed(time_source, "GrpHdr/CreDtTm", "2026-09-30T12:00:00Z"),
    time_spec,
    "FAIL",
    "time-control",
)

keyed_spec = contract(
    "pacs008-keyed-amount",
    "transactions.settlement_amount",
    "decimal-and-currency-equal",
    cardinality="per-transaction",
    keyed=True,
)
batch = etree.fromstring((ROOT / "corpus/extended/batch-control.source.xml").read_bytes())
add("keyed-control", batch, batch, keyed_spec)
for name, filename, status in [
    ("keyed-reorder", "batch-reordered", "PASS"),
    ("keyed-swap", "batch-amount-swapped", "FAIL"),
    ("keyed-duplicate", "batch-duplicate-key", "INDETERMINATE"),
]:
    target = etree.fromstring((ROOT / f"corpus/extended/{filename}.target.xml").read_bytes())
    add(name, batch, target, keyed_spec, status, "keyed-control")
missing = copy.deepcopy(batch)
node = field(missing, "PmtId/TxId")
node.getparent().remove(node)
add("keyed-missing", batch, missing, keyed_spec, "INDETERMINATE", "keyed-control")
add(
    "keyed-regenerated-id",
    batch,
    changed(batch, "GrpHdr/MsgId", "SYNTHETIC-NEW-ID"),
    keyed_spec,
    control="keyed-control",
)

nfc = contract(
    "pacs008-name-nfc",
    "transactions.debtor_name",
    "exact-text",
    cardinality="per-transaction",
    normalization="NFC",
)
exact = contract(
    "pacs008-name-exact", "transactions.debtor_name", "exact-text", cardinality="per-transaction"
)
name_source = changed(base, "Dbtr/Nm", "Café")
add("nfc-control", name_source, name_source, nfc)
add(
    "nfc-equivalent",
    name_source,
    changed(name_source, "Dbtr/Nm", "Cafe\u0301"),
    nfc,
    control="nfc-control",
)
add("nfc-changed", name_source, changed(name_source, "Dbtr/Nm", "Cafe"), nfc, "FAIL", "nfc-control")
add("exact-name-control", name_source, name_source, exact)
for name, value in [
    ("nfd-not-normalized", "Cafe\u0301"),
    ("name-whitespace", "Café "),
    ("name-case", "CAFÉ"),
    ("name-script-change", "ሙከራ"),
]:
    add(
        name,
        name_source,
        changed(name_source, "Dbtr/Nm", value),
        exact,
        "FAIL",
        "exact-name-control",
    )

presence = contract(
    "pacs008-name-presence",
    "transactions.debtor_name",
    "presence-equal",
    missing="compare-presence",
    cardinality="per-transaction",
)
absent = copy.deepcopy(base)
node = field(absent, "Dbtr/Nm")
node.getparent().remove(node)
add("presence-absent-control", absent, absent, presence)
add("presence-present-control", base, base, presence)
add("presence-added", absent, base, presence, "FAIL", "presence-absent-control")
add("presence-removed", base, absent, presence, "FAIL", "presence-present-control")

ordered = contract(
    "pacs008-remittance-ordered",
    "transactions.remittance",
    "ordered-list",
    cardinality="per-transaction",
)
multiset = contract(
    "pacs008-remittance-multiset",
    "transactions.remittance",
    "multiset",
    cardinality="per-transaction",
)
add("ordered-control", base, base, ordered)
rev = copy.deepcopy(base)
node = field(rev, "RmtInf")
node[:] = list(reversed(node))
add("ordered-reversed", base, rev, ordered, "FAIL", "ordered-control")
add("multiset-reversed", base, rev, multiset)
dup = copy.deepcopy(base)
node = field(dup, "RmtInf")
node.append(copy.deepcopy(node[0]))
add("multiset-duplicated", base, dup, multiset, "FAIL", "multiset-reversed")
assert len(cases) == 32
manifest = {
    "schema_version": "1.0",
    "version": "0.2.0",
    "review_status": "pending-independent-human-review",
    "cases": cases,
}
raw = (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode()
(OUT / "index.json").write_bytes(raw)
(OUT / "expectations-authored.sha256").write_text(
    hashlib.sha256(raw).hexdigest() + "  index.json\n"
)
print("Authored 32 classifications without calling the oracle")
