"""Reproduce predeclared parser/configuration/workflow attack cases with positive controls."""

import hashlib
import json
import tempfile
from pathlib import Path

from aksum_messagebench.assets import data_root
from aksum_messagebench.engine import compare
from aksum_messagebench.errors import BenchError
from aksum_messagebench.reports import render
from aksum_messagebench.workflows import suite

ROOT = Path(__file__).resolve().parents[1]
DATA = data_root()
BASE = (DATA / "corpus/positive/identity.source.xml").read_bytes()
CONTRACT = DATA / "contracts/pacs008-preserve.json"
# Expected codes are authored here, independently of execution results.
SPECS = [
    ("foreign-namespace", 3),
    ("unsupported-namespace", 3),
    ("dtd-entity", 4),
    ("remote-entity", 4),
    ("remote-schema", 4),
    ("xinclude", 4),
    ("xml-depth", 4),
    ("oversized-input", 4),
    ("malformed-contract", 2),
    ("missing-output", 3),
    ("html-payload", 0),
    ("excluded-field", 0),
    ("unexamined-field", 0),
]


def run():
    records = []
    with tempfile.TemporaryDirectory(prefix="messagebench-security-corpus-") as folder:
        root = Path(folder)
        source = root / "source.xml"
        target = root / "target.xml"
        source.write_bytes(BASE)
        for name, expected in SPECS:
            target.write_bytes(BASE)
            control = compare(source, target, CONTRACT)
            assert control["exit_code"] == 0
            contract = CONTRACT
            payload = BASE
            if name in {"foreign-namespace", "unsupported-namespace"}:
                payload = BASE.replace(
                    b"urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08",
                    b"urn:foreign"
                    if name == "foreign-namespace"
                    else b"urn:iso:std:iso:20022:tech:xsd:pacs.008.001.09",
                )
            elif name == "dtd-entity":
                payload = b'<!DOCTYPE x [<!ENTITY a "a"><!ENTITY b "&a;&a;">]><x>&b;</x>'
            elif name == "remote-entity":
                payload = b'<!DOCTYPE x SYSTEM "https://example.invalid/external"><x/>'
            elif name == "remote-schema":
                payload = (
                    b'<x xmlns:s="http://www.w3.org/2001/XMLSchema-instance" '
                    b's:schemaLocation="x https://example.invalid/schema"/>'
                )
            elif name == "xinclude":
                payload = b'<x xmlns:i="http://www.w3.org/2001/XInclude"><i:include href="file:///not-read"/></x>'
            elif name == "xml-depth":
                payload = b"<x>" * 65 + b"</x>" * 65
            elif name == "oversized-input":
                payload = b" " * (5 * 1024 * 1024 + 1)
            elif name == "malformed-contract":
                contract = root / "bad.json"
                contract.write_text('{"execute":"not-allowed"}')
            elif name == "html-payload":
                payload = BASE.replace(b"INV-2026-000123", b"&lt;script&gt;alert(1)&lt;/script&gt;")
                source.write_bytes(payload)
            elif name == "excluded-field":
                doc = json.loads(CONTRACT.read_text())
                doc["assertions"] = [
                    a for a in doc["assertions"] if a["field"] != "transactions.end_to_end_id"
                ]
                doc["exclusions"] = [
                    {
                        "field": "transactions.end_to_end_id",
                        "reason": "Explicit synthetic exclusion",
                    }
                ]
                contract = root / "exclude.json"
                contract.write_text(json.dumps(doc))
                payload = BASE.replace(b"INV-2026-000123", b"SYNTHETIC-CHANGED")
            elif name == "unexamined-field":
                payload = BASE.replace(b"2026-09-29T12:00:00Z", b"2026-09-30T12:00:00Z")
                # Use a known unexamined creation timestamp regardless of original lexical value.
                import re

                payload = re.sub(rb"(<CreDtTm>)[^<]+", rb"\g<1>2026-09-30T12:00:00Z", BASE)
            target.write_bytes(payload)
            try:
                if name == "missing-output":
                    outputs = root / "empty"
                    outputs.mkdir()
                    result = suite(DATA / "corpus/gate1-index.json", outputs)
                else:
                    result = compare(source, target, contract)
                actual = result["exit_code"]
                if name == "html-payload":
                    assert b"alert(1)" not in render(result, "html")
                if name == "excluded-field":
                    assert (
                        result["coverage"]["target"]["categories"]["explicitly_excluded"]["count"]
                        > 0
                    )
                if name == "unexamined-field":
                    assert result["coverage"]["target"]["categories"]["unexamined"]["count"] > 0
            except BenchError as exc:
                actual = exc.exit_code
            assert actual == expected, (name, actual, expected)
            records.append(
                {
                    "id": name,
                    "expected_exit": expected,
                    "actual_exit": actual,
                    "control_exit": control["exit_code"],
                    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                    "target_sha256": hashlib.sha256(payload).hexdigest(),
                    "classification_matched": True,
                    "independently_reviewed": False,
                }
            )
            source.write_bytes(BASE)
    return {
        "schema_version": "1.0",
        "cases": records,
        "all_matched": True,
        "scope": (
            "13 safety/workflow scenarios, each with valid positive control; "
            "generated locally, no real inputs."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
