"""Pin exact local versioned schemas; no runtime trust expansion or imports."""

import hashlib
from pathlib import Path

from lxml import etree

from .assets import data_root
from .errors import BenchError
from .input_guard import load_json, read_local
from .xml_reader import DenyResolver, parse_xml

NAMESPACE = "urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08"
SCHEMA_HASH = "9bb360555d1981be8635aa3ed295abfe8b2d221d316193434114ad722107dcde"
SCHEMA_HASHES = {
    NAMESPACE: SCHEMA_HASH,
    "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.10": (
        "d14da6304db5178b1afc7d8ed6cc6073e6e1a143fc79d9ba66d3246d4a654e90"
    ),
}


class Catalog:
    def __init__(self, path: Path | None = None):
        self.path = path or data_root() / "schemas/catalog.json"
        try:
            catalog, raw = load_json(self.path)
        except BenchError as exc:
            if exc.exit_code == 3:
                raise BenchError("CATALOG_MISSING", 2) from None
            raise
        self.sha256 = hashlib.sha256(raw).hexdigest()
        if set(catalog) != {"schema_version", "schemas"} or catalog["schema_version"] != "1.0":
            raise BenchError("CATALOG_INVALID", 2)
        entries = catalog["schemas"]
        if not isinstance(entries, list) or not 1 <= len(entries) <= len(SCHEMA_HASHES):
            raise BenchError("CATALOG_INVALID", 2)
        self.schemas: dict[str, etree.XMLSchema] = {}
        for entry in entries:
            if not isinstance(entry, dict):
                raise BenchError("CATALOG_INVALID", 2)
            if not isinstance(entry.get("namespace"), str):
                raise BenchError("CATALOG_INVALID", 2)
            if entry["namespace"] in self.schemas:
                raise BenchError("CATALOG_DUPLICATE_NAMESPACE", 2)
            if set(entry) != {
                "namespace",
                "path",
                "sha256",
                "origin",
                "retrieval",
                "license",
                "modified",
            }:
                raise BenchError("CATALOG_INVALID", 2)
            if (
                entry["namespace"] not in SCHEMA_HASHES
                or entry["sha256"] != SCHEMA_HASHES.get(entry["namespace"])
                or entry["modified"] is not False
                or not isinstance(entry["path"], str)
            ):
                raise BenchError("CATALOG_UNREVIEWED_SCHEMA", 2)
            raw_schema = read_local(entry["path"], root=self.path.parent)
            if hashlib.sha256(raw_schema).hexdigest() != SCHEMA_HASHES[entry["namespace"]]:
                raise BenchError("SCHEMA_HASH_MISMATCH", 2)
            root = parse_xml(raw_schema)
            if root.tag != "{http://www.w3.org/2001/XMLSchema}schema":
                raise BenchError("SCHEMA_ROOT_INVALID", 2)
            if root.get("targetNamespace") != entry["namespace"]:
                raise BenchError("SCHEMA_NAMESPACE_INVALID", 2)
            for name in ("import", "include", "redefine"):
                if root.find("{http://www.w3.org/2001/XMLSchema}" + name) is not None:
                    raise BenchError("SCHEMA_IMPORT_FORBIDDEN", 4)
            # Compile only the constant-hash schema. A deny-all resolver remains in effect.
            parser = etree.XMLParser(resolve_entities=False, load_dtd=False, no_network=True)
            parser.resolvers.add(DenyResolver())
            try:
                self.schemas[entry["namespace"]] = etree.XMLSchema(
                    etree.fromstring(raw_schema, parser)
                )
            except etree.XMLSchemaParseError:
                raise BenchError("SCHEMA_COMPILE_INVALID", 2) from None

    def validate(self, root) -> bool:
        namespace = etree.QName(root).namespace
        return namespace in self.schemas and bool(self.schemas[namespace].validate(root))
