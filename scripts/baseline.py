# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
"""Reproduce the proof offline. Optional reviewed Cognis source is supplied locally."""

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path
from xml.etree import ElementTree

import lxml.etree
import xmlschema

from aksum_messagebench.engine import compare
from aksum_messagebench.reports import canonical_json

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cognis-source", type=Path)
    args = parser.parse_args()
    cognis = None
    cognis_hash = None
    if args.cognis_source:
        # Development-only baseline. Never available through the installed CLI.
        cognis_hash = hashlib.sha256(args.cognis_source.read_bytes()).hexdigest()
        if cognis_hash != "8897194e3728f302bbed68fd816cb6001f75a5c6cb072fb4bfdfdde429ae8d1a":
            raise SystemExit("Only the exact source reviewed for this baseline may run.")
        spec = importlib.util.spec_from_file_location(
            "cognis_reviewed_baseline", args.cognis_source
        )
        cognis = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = cognis
        spec.loader.exec_module(cognis)
    schema_path = ROOT / "schemas/iso/pacs.008.001.08.xsd"
    first = lxml.etree.XMLSchema(lxml.etree.parse(str(schema_path)))
    second = xmlschema.XMLSchema(str(schema_path), allow="local", defuse="always")
    cases = json.loads((ROOT / "corpus/gate1-index.json").read_text())["cases"]
    output = {
        "processors": {
            "lxml": lxml.etree.LXML_VERSION,
            "libxml2": lxml.etree.LIBXML_VERSION,
            "xmlschema": xmlschema.__version__,
        },
        "cognis_source_sha256": cognis_hash,
        "cases": [],
    }
    for case in cases:
        paths = [ROOT / "corpus" / case[side] for side in ("source", "target")]
        row = {"id": case["id"], "inputs": {}}
        for side, path in zip(("source", "target"), paths, strict=True):
            raw = path.read_bytes()
            ElementTree.fromstring(raw)
            result = {
                "parser": "PASS",
                "lxml_xsd": bool(first.validate(lxml.etree.fromstring(raw))),
                "xmlschema_xsd": bool(second.is_valid(raw)),
                "sha256": hashlib.sha256(raw).hexdigest(),
            }
            if cognis:
                report = cognis.validate_string(raw.decode("utf-8"))
                result["cognis_lint_ok"] = report.ok
                result["cognis_codes"] = [f.code for f in report.findings]
            row["inputs"][side] = result
        report = compare(*paths, ROOT / "contracts/pacs008-preserve.json")
        row["messagebench"] = {
            "overall": report["overall"],
            "failed_assertions": [a["id"] for a in report["assertions"] if a["status"] == "FAIL"],
        }
        output["cases"].append(row)
    print(canonical_json(output).decode(), end="")


if __name__ == "__main__":
    main()
