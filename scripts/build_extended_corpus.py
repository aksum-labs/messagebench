"""Author synthetic cases and their expectations without importing the comparison engine.

Run before verification. This is engineering authorship, not independent review.
"""

import copy
import hashlib
import json
from pathlib import Path

from lxml import etree

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "corpus/extended"
Q = "{urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08}"
BASE = (ROOT / "corpus/positive/identity.source.xml").read_bytes()
CONTRACT = json.loads((ROOT / "contracts/pacs008-extended.json").read_text())
# Authored paths and values, independent of the runtime extractor field table.
SPECS = [
    ("debtor_account", "DbtrAcct/Id/Othr/Id", "0000123400", "123400"),
    ("end_to_end_id", "PmtId/EndToEndId", "INV-2026-000123", "INV-2026-000"),
    ("transaction_id", "PmtId/TxId", "SYNTHETIC-TX-0001", "SYNTHETIC-TX-000"),
    ("instruction_id", "PmtId/InstrId", "INSTRUCTION-0001", "INSTRUCTION-001"),
    ("debtor_account_iban", "DbtrAcct/Id/IBAN", "GB82WEST12345698765432", "GB82WEST12345698765433"),
    ("debtor_account_scheme_code", "DbtrAcct/Id/Othr/SchmeNm/Cd", "BBAN", "CUID"),
    ("debtor_account_scheme_proprietary", "DbtrAcct/Id/Othr/SchmeNm/Prtry", "SYNTHETIC", "CHANGED"),
    ("debtor_account_issuer", "DbtrAcct/Id/Othr/Issr", "FICTIONAL-ISSUER", "DIFFERENT-ISSUER"),
    ("debtor_agent_bic", "DbtrAgt/FinInstnId/BICFI", "AAAAETAA", "BBBBETAA"),
    ("debtor_agent_other_id", "DbtrAgt/FinInstnId/Othr/Id", "FICTIONAL-DEBTOR-AGENT", "CHANGED"),
    ("creditor_account", "CdtrAcct/Id/Othr/Id", "0000888000", "888000"),
    (
        "creditor_account_iban",
        "CdtrAcct/Id/IBAN",
        "GB82WEST12345698765432",
        "GB82WEST12345698765433",
    ),
    ("creditor_account_issuer", "CdtrAcct/Id/Othr/Issr", "SYNTHETIC-ISSUER", "CHANGED-ISSUER"),
    ("creditor_agent_bic", "CdtrAgt/FinInstnId/BICFI", "CCCCETAA", "DDDDETAA"),
    ("debtor_name", "Dbtr/Nm", "ሙከራ", "ሙከ"),
    ("creditor_name", "Cdtr/Nm", "Fictional Recipient", "fictional recipient"),
    ("instructed_amount", "InstdAmt", "1250.500", "1250.51"),
    ("settlement_amount", "IntrBkSttlmAmt", "1250.500", "1250.51"),
]
ORDER = {
    "CdtTrfTxInf": [
        "PmtId",
        "IntrBkSttlmAmt",
        "InstdAmt",
        "ChrgBr",
        "Dbtr",
        "DbtrAcct",
        "DbtrAgt",
        "CdtrAgt",
        "Cdtr",
        "CdtrAcct",
        "RmtInf",
    ],
    "PmtId": ["InstrId", "EndToEndId", "TxId"],
    "FinInstnId": ["BICFI", "Othr"],
    "Othr": ["Id", "SchmeNm", "Issr"],
}


def ensure(node, path):
    for part in path.split("/"):
        child = node.find(Q + part)
        if child is None:
            child = etree.SubElement(node, Q + part)
            order = ORDER.get(etree.QName(node).localname)
            if order:
                node[:] = sorted(node, key=lambda item: order.index(etree.QName(item).localname))
        node = child
    return node


cases = []
OUT.mkdir(exist_ok=True)


def add(name, source, target, failed=(), code=0, rationale=""):
    pair = {}
    for side, root in (("source", source), ("target", target)):
        data = etree.tostring(root, encoding="UTF-8", xml_declaration=True)
        file = name + "." + side + ".xml"
        (OUT / file).write_bytes(data)
        pair[side] = file
        pair[side + "_sha256"] = hashlib.sha256(data).hexdigest()
    cases.append(
        {
            "id": name,
            **pair,
            "expected": {
                "overall": "PASS" if code == 0 else "FAIL" if code == 1 else "INDETERMINATE",
                "exit_code": code,
                "failed_assertions": list(failed),
                "source_xsd": "PASS",
                "target_xsd": "PASS",
            },
            "rationale": rationale,
            "control": name if code == 0 else name.rsplit("-", 1)[0] + "-control",
            "license": "Apache-2.0",
            "provenance": "Original synthetic engineering authoring; no customer data.",
            "reviewers": [],
        }
    )


for field, path, original, changed in SPECS:
    source = etree.fromstring(BASE)
    tx = source[0].find(Q + "CdtTrfTxInf")
    if path.endswith("/IBAN"):
        identifier = ensure(tx, path.rsplit("/", 1)[0])
        identifier[:] = []
    if field == "debtor_account_scheme_code":
        ensure(tx, "DbtrAcct/Id/Othr/SchmeNm")[:] = []
    node = ensure(tx, path)
    node.text = original
    if field == "creditor_account_issuer":
        ensure(tx, "CdtrAcct/Id/Othr/Id").text = "0000888000"
    if field in {"instructed_amount", "settlement_amount"}:
        node.set("Ccy", "ETB")
    target = copy.deepcopy(source)
    target[0].find(
        Q + "CdtTrfTxInf/" + "/".join(Q + part for part in path.split("/"))
    ).text = changed
    name = field.replace("_", "-")
    add(
        name + "-control",
        source,
        source,
        rationale="Identity control with the named field present.",
    )
    if field == "transaction_id":
        add(
            name + "-changed",
            source,
            target,
            code=3,
            rationale="Changed declared association key prevents a reliable pairing.",
        )
    else:
        add(
            name + "-changed",
            source,
            target,
            failed=["PRESERVE-" + field.upper().replace("_", "-")],
            code=1,
            rationale="Schema-valid change to the named explicitly preserved field.",
        )

source = etree.fromstring(BASE)
add("remittance-control", source, source, rationale="Repeated remittance identity control.")
for name, action in [("removed", "remove"), ("duplicated", "duplicate"), ("reordered", "reorder")]:
    target = copy.deepcopy(source)
    remittance = target.find(".//" + Q + "RmtInf")
    if action == "remove":
        remittance.remove(remittance[-1])
    elif action == "duplicate":
        remittance.append(copy.deepcopy(remittance[-1]))
    else:
        remittance.append(remittance[0])
    add(
        "remittance-" + name,
        source,
        target,
        failed=[] if action == "reorder" else ["PRESERVE-REMITTANCE"],
        code=0 if action == "reorder" else 1,
        rationale="Multiset semantics preserve multiplicity while allowing reordering.",
    )

document = {
    "schema_version": "1.0",
    "version": "0.2.0",
    "review_status": "pending-independent-human-review",
    "cases": cases,
}
raw = (json.dumps(document, indent=2) + "\n").encode()
(OUT / "index.json").write_bytes(raw)
(OUT / "expectations-authored.sha256").write_text(hashlib.sha256(raw).hexdigest() + "\n")
print(f"Authored {len(cases)} cases; no oracle was executed.")
