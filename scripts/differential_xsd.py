# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
"""Validate every distributable fixture with two independent XSD implementations."""

import hashlib
import json

import xmlschema
from lxml import etree

from aksum_messagebench.assets import data_root
from aksum_messagebench.schema_catalog import Catalog
from aksum_messagebench.xml_reader import parse_xml

root = data_root()
catalog = Catalog()
schemas = {}
for path in sorted((root / "schemas/iso").glob("*.xsd")):
    schema = xmlschema.XMLSchema(path, allow="local", defuse="always")
    schemas[schema.target_namespace] = schema
manifest = json.loads((root / "corpus/index.json").read_text())
results = []
for case in manifest["cases"]:
    for side in ("source", "target"):
        raw = (root / "corpus" / case[side]).read_bytes()
        tree = parse_xml(raw)
        namespace = etree.QName(tree).namespace
        first = catalog.validate(tree)
        second = schemas[namespace].is_valid(raw)
        expected = case["expected"][side + "_xsd"] == "PASS"
        assert first == second == expected, (case["id"], side)
        results.append(
            {
                "case": case["id"],
                "side": side,
                "sha256": hashlib.sha256(raw).hexdigest(),
                "lxml_valid": first,
                "xmlschema_valid": second,
                "expected_valid": expected,
            }
        )
out = {
    "processors": {
        "lxml": etree.LXML_VERSION,
        "libxml2": etree.LIBXML_VERSION,
        "xmlschema": xmlschema.__version__,
    },
    "documents": len(results),
    "all_agree": True,
    "results": results,
    "scope": "All distributable XML-pair fixtures; malicious parser probes are tested separately.",
}
print(json.dumps(out, indent=2, sort_keys=True))
