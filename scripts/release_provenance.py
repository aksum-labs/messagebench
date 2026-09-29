"""Attach unsigned source/input provenance to an already built local review bundle."""

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

from prepare_bundle import write_checksums

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--bundle", type=Path, required=True)
args = parser.parse_args()
bundle = args.bundle
build = json.loads((bundle / "build-evidence.json").read_text())
if build["source_dirty"] is not False or not build["unsigned_artifacts_identical"]:
    raise SystemExit("Clean matching source builds required")


if (
    subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT).decode().strip()
    != build["source_commit"]
):
    raise SystemExit("Source commit changed since build")
if subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT).strip():
    raise SystemExit("Provenance requires clean source inputs")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


for name, digest in build["runs"][0].items():
    if sha(bundle / name) != digest:
        raise SystemExit("Release artifact hash mismatch")
inputs = [
    ROOT / "dependency-lock.txt",
    ROOT / "dependency-lock-hashed.txt",
    ROOT / "runtime-lock.txt",
    ROOT / "corpus/index.json",
    ROOT / "schemas/catalog.json",
    *sorted((ROOT / "contracts").glob("*.json")),
    *sorted((ROOT / "schemas/iso").glob("*.xsd")),
]
result = {
    "kind": "unsigned-local-build-provenance",
    "source_commit": build["source_commit"],
    "source_clean_at_build": True,
    "toolchain": {
        "python": build["python"],
        "platform": build["platform"],
        "source_date_epoch": build["source_date_epoch"],
    },
    "inputs": {str(p.relative_to(ROOT)): sha(p) for p in inputs},
    "artifacts": build["runs"][0],
    "native_build_manifest_sha256": sha(bundle / "native-build.json"),
    "sbom_sha256": sha(bundle / "sbom.cdx.json"),
    "same_environment_unsigned_builds_identical": True,
    "independent_reproduction": False,
    "identity_signature": None,
    "publication": False,
}
(bundle / "provenance.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
write_checksums(bundle)
print("Unsigned provenance generated; no identity or approval implied.")
