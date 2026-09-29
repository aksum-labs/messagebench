"""Record Python/native dependencies and asset rights; no network access."""

import hashlib
import importlib.metadata as metadata
import json
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
components = []
inventory = []
for dist in sorted(metadata.distributions(), key=lambda d: d.metadata["Name"].lower()):
    name = dist.metadata["Name"]
    normalized = name.lower().replace("_", "-")
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
        }
    )
for name, version, source, license in [
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
]:
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
    "unresolved": ["Independent human asset/provenance review pending with Gate 1."],
}
(root / "evidence/dependency-inventory.json").write_text(json.dumps(inventory, indent=2) + "\n")
(root / "evidence/rights-register.json").write_text(json.dumps(rights_document, indent=2) + "\n")
bom = {
    "bomFormat": "CycloneDX",
    "specVersion": "1.6",
    "version": 1,
    "metadata": {
        "component": {"type": "application", "name": "aksum-messagebench", "version": "0.1.0a1"}
    },
    "components": components,
    "dependencies": [{"ref": "lxml", "dependsOn": ["libxml2", "libxslt"]}],
}
(root / "evidence/sbom.cdx.json").write_text(json.dumps(bom, sort_keys=True, indent=2) + "\n")
lines = [i["name"] + "==" + i["version"] for i in inventory if i["role"] == "runtime"]
(root / "runtime-lock.txt").write_text("\n".join(sorted(lines, key=str.lower)) + "\n")
