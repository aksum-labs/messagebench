"""Record Python/native dependencies and asset rights; no network access."""

import ctypes
import hashlib
import importlib.metadata as metadata
import json
import tomllib
from pathlib import Path

from lxml import etree

root = Path(__file__).resolve().parents[1]
runtime = {
    "lxml",
    "jsonschema",
    "attrs",
    "jsonschema-specifications",
    "referencing",
    "rpds-py",
    "typing-extensions",
}
license_policy = {
    item["name"]: item
    for item in json.loads((root / "evidence/dependency-license-policy.json").read_text())[
        "dependencies"
    ]
}
components = []
inventory = []
for dist in sorted(metadata.distributions(), key=lambda d: d.metadata["Name"].lower()):
    name = dist.metadata["Name"]
    normalized = name.lower().replace("_", "-")
    if normalized in {"messagebench", "aksum-messagebench"}:
        continue
    terms = (
        dist.metadata.get("License-Expression")
        or dist.metadata.get("License")
        or "Review package license files"
    )
    item = {
        "name": name,
        "version": dist.version,
        "role": "runtime" if normalized in runtime else "development",
        "license_metadata": terms,
        "source": "https://pypi.org/project/" + name + "/" + dist.version + "/",
        "metadata_sha256": hashlib.sha256((dist.read_text("METADATA") or "").encode()).hexdigest(),
    }
    inventory.append(item)
    components.append(
        {
            "type": "library",
            "bom-ref": normalized,
            "name": name,
            "version": dist.version,
            "scope": "required" if normalized in runtime else "optional",
            "purl": f"pkg:pypi/{normalized}@{dist.version}",
            "properties": [{"name": "aksum:role", "value": item["role"]}],
            "licenses": [{"expression": license_policy[normalized]["license_expression"]}],
        }
    )
native_components = [
    (
        "libxml2",
        ".".join(map(str, etree.LIBXML_VERSION)),
        "https://gitlab.gnome.org/GNOME/libxml2",
        "MIT",
    ),
    (
        "libxslt",
        ".".join(map(str, etree.LIBXSLT_VERSION)),
        "https://gitlab.gnome.org/GNOME/libxslt",
        "MIT",
    ),
]
try:
    iconv_version = ctypes.c_int.in_dll(ctypes.CDLL(etree.__file__), "_libiconv_version").value
except (ValueError, OSError):
    iconv_version = None
if iconv_version is not None:
    native_components.append(
        (
            "libiconv",
            f"{iconv_version >> 8}.{iconv_version & 255}",
            "https://www.gnu.org/software/libiconv/",
            "LGPL-2.1-or-later",
        )
    )
for name, version, source, license in native_components:
    inventory.append(
        {
            "name": name,
            "version": version,
            "role": "native dependency bundled by lxml",
            "source": source,
            "license_metadata": license,
            "vulnerability_scan": "Not covered by pip-audit Python advisory lookup; "
            "native review pending.",
        }
    )
    components.append(
        {
            "type": "library",
            "bom-ref": name,
            "name": name,
            "version": version,
            "scope": "required",
            "purl": f"pkg:generic/{name}@{version}",
            "licenses": [{"license": {"id": license}}],
        }
    )
rights = []
for name, file, source, version, license, status in [
    (
        "pacs.008.001.08 full XSD",
        "schemas/iso/pacs.008.001.08.xsd",
        "https://raw.githubusercontent.com/socrates8300/mx20022/b650c81f60311801f240efea3f9cc6df9adb70f9/schemas/pacs/pacs.008.001.08.xsd",
        "pacs.008.001.08",
        "LicenseRef-SWIFTStandards-2005",
        "Include unmodified and royalty-free with terms retained; sections 2 and 4 permit "
        "supporting software and royalty-free sublicensing; section 3 limitations apply. "
        "Not Apache-2.0.",
    ),
    (
        "pacs.002.001.10 full XSD",
        "schemas/iso/pacs.002.001.10.xsd",
        "https://raw.githubusercontent.com/phoughton/pyiso20022/"
        "cfb785fcc5174b09adee1419eb83743c85c79398/"
        "xsd/payments_clearing_and_settlement/pacs.002/pacs.002.001.10.xsd",
        "pacs.002.001.10",
        "LicenseRef-SWIFTStandards-2005",
        "Include unmodified with retained terms under supporting-software and royalty-free "
        "sublicensing provisions. Not Apache-2.0.",
    ),
    (
        "SWIFTStandards terms",
        "third-party/SWIFTStandards_LIC_OUT_V5.pdf",
        "https://www.iso20022.org/sites/default/files/documents/D7/SWIFTStandards_LIC_OUT_V5_.pdf",
        "September 2005",
        "License text",
        "Include unmodified to convey applicable license terms.",
    ),
    (
        "Apache License 2.0 text",
        "LICENSE",
        "https://www.apache.org/licenses/LICENSE-2.0.txt",
        "2.0",
        "Apache-2.0",
        "Include license notice for original code and fixtures.",
    ),
]:
    digest = hashlib.sha256((root / file).read_bytes()).hexdigest()
    rights.append(
        {
            "name": name,
            "file": file,
            "source": source,
            "version": version,
            "sha256": digest,
            "license_or_terms": license,
            "redistribution_status": status,
            "modified": False,
            "inclusion_decision": "included",
        }
    )
    components.append(
        {
            "type": "file",
            "bom-ref": file,
            "name": name,
            "hashes": [{"alg": "SHA-256", "content": digest}],
        }
    )
rights_document = {
    "reference_date": "2026-09-29",
    "third_party_assets": rights,
    "original_assets": {
        "scope": "Aksum code, contracts, docs, original synthetic fixtures",
        "license": "Apache-2.0",
    },
    "provenance_limits": [
        "Official archive identifies SWIFT as submitter and exact version.",
        "Official direct XSD download returned 403; mirror bytes preserved unchanged.",
        "Second moov-io public mirror has equivalent C14N with blank text and comments removed.",
        "ISO repository terms: https://www.iso20022.org/intellectual-property-rights",
        "No paid ISO publications or proprietary usage guidelines included.",
    ],
    "excluded_assets": [
        "Third-party vendor fixtures",
        "Private Ethiopian scheme rules",
        "Commercial identifier directories",
        "Other prior-art source code",
    ],
    "review_status": "BLOCKED-BY-HUMAN: independent asset/provenance approval only",
    "dependency_license_policy": "evidence/dependency-license-policy.json",
    "dependency_release_hashes": "evidence/dependency-release-hashes.json",
    "native_source_inventory": "evidence/native-source-pins.json",
    "bundle_inventory": (
        "Each review bundle includes bundle-rights-register.json for every wheel/source archive."
    ),
    "camt053_decision": (
        "Excluded; see docs/camt053-asset-review.md. Rights clarification is BLOCKED-BY-HUMAN."
    ),
}
(root / "evidence/dependency-inventory.json").write_text(json.dumps(inventory, indent=2) + "\n")
(root / "evidence/rights-register.json").write_text(json.dumps(rights_document, indent=2) + "\n")
bom = {
    "bomFormat": "CycloneDX",
    "specVersion": "1.6",
    "version": 1,
    "metadata": {
        "component": {
            "type": "application",
            "name": "messagebench",
            "version": tomllib.loads((root / "pyproject.toml").read_text())["project"]["version"],
        }
    },
    "components": components,
    "dependencies": [{"ref": "lxml", "dependsOn": [item[0] for item in native_components]}],
}
(root / "evidence/sbom.cdx.json").write_text(json.dumps(bom, sort_keys=True, indent=2) + "\n")
lines = [i["name"] + "==" + i["version"] for i in inventory if i["role"] == "runtime"]
(root / "runtime-lock.txt").write_text("\n".join(sorted(lines, key=str.lower)) + "\n")
