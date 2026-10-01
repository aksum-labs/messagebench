# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
"""Explicit connected maintainer action: capture release-file digests for exact pins."""

import concurrent.futures
import hashlib
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def resolve(line):
    name, version = line.split("==")
    url = f"https://pypi.org/pypi/{name}/{version}/json"
    with urllib.request.urlopen(url, timeout=30) as response:
        raw = response.read()
    document = json.loads(raw)
    assert document["info"]["version"] == version
    files = [
        {"filename": f["filename"], "sha256": f["digests"]["sha256"]}
        for f in document["urls"]
        if not f.get("yanked")
    ]
    if not files:
        raise ValueError("No unyanked release files for " + name)
    return line, {"source": url, "response_sha256": hashlib.sha256(raw).hexdigest(), "files": files}


lines = [
    line
    for line in (ROOT / "dependency-lock.txt").read_text().splitlines()
    if line and not line.startswith("#")
]
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    resolved = dict(pool.map(resolve, lines))
locked = []
for line in lines:
    hashes = sorted({f["sha256"] for f in resolved[line]["files"]})
    locked.append(line + " \\\n" + " \\\n".join("    --hash=sha256:" + h for h in hashes))
(ROOT / "dependency-lock-hashed.txt").write_text("\n".join(locked) + "\n")
(ROOT / "evidence/dependency-release-hashes.json").write_text(
    json.dumps(resolved, indent=2, sort_keys=True) + "\n"
)
print("Captured verified-release metadata for", len(resolved), "exact distributions")
