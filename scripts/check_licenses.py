# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
"""Fail on changed pinned dependency metadata or license notices requiring renewed review."""

import hashlib
import importlib.metadata as metadata
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
policy = json.loads((root / "evidence/dependency-license-policy.json").read_text())
expected = {p["name"]: p for p in policy["dependencies"]}
locked = {
    line.split("==")[0].lower().replace("_", "-")
    for line in (root / "dependency-lock.txt").read_text().splitlines()
    if line and not line.startswith("#")
}
if set(expected) != locked:
    raise SystemExit("License policy does not cover the complete dependency lock")
for name, item in expected.items():
    dist = metadata.distribution(name)
    digest = hashlib.sha256((dist.read_text("METADATA") or "").encode()).hexdigest()
    if dist.version != item["version"] or digest != item["metadata_sha256"]:
        raise SystemExit("Dependency metadata requires renewed license review: " + name)
    for notice in item["license_files"]:
        file = dist.locate_file(notice["path"])
        if not file.is_file() or hashlib.sha256(file.read_bytes()).hexdigest() != notice["sha256"]:
            raise SystemExit("Dependency license notice changed: " + name)
print(f"All {len(expected)} pinned distributions match reviewed license metadata/notices.")
print("Native and schema redistribution obligations are additional; see the rights registers.")
