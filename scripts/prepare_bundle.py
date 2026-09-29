"""Prepare a local offline review bundle. No publication or identity-backed signing."""

import argparse
import email
import hashlib
import json
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--release", type=Path, required=True)
    parser.add_argument("--native", type=Path, required=True)
    parser.add_argument("--archives", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    wheels = args.out / "wheelhouse"
    wheels.mkdir()
    native_manifest = json.loads((args.native / "native-build.json").read_text())
    for name, digest in native_manifest["wheels"].items():
        path = args.native / name
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise SystemExit("Native wheel hash mismatch")
        shutil.copyfile(path, wheels / name)
    requirements = [
        line
        for line in (ROOT / "runtime-lock.txt").read_text().splitlines()
        if not line.lower().startswith("lxml==")
    ]
    requirements.append("pip==26.2.1")
    download = args.out / "download-requirements.txt"
    download.write_text("\n".join(requirements) + "\n")
    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "download",
            "--only-binary=:all:",
            "--no-deps",
            "-r",
            str(download),
            "--dest",
            str(wheels),
        ],
        check=True,
        timeout=300,
    )
    for path in args.release.iterdir():
        if path.is_file():
            shutil.copyfile(path, args.out / path.name)
            if path.suffix == ".whl":
                shutil.copyfile(path, wheels / path.name)
    pins = json.loads((ROOT / "evidence/native-source-pins.json").read_text())
    sources = args.out / "native-sources"
    sources.mkdir()
    for item in pins["archives"]:
        source = args.archives / item["name"]
        if hashlib.sha256(source.read_bytes()).hexdigest() != item["sha256"]:
            raise SystemExit("Native source hash mismatch")
        shutil.copyfile(source, sources / item["name"])
    shutil.copyfile(args.native / "native-build.json", args.out / "native-build.json")
    for name in ["LICENSE", "NOTICE", "GATE_REPORT.md", "RELEASE_READINESS.md", "LIMITATIONS.md"]:
        shutil.copyfile(ROOT / name, args.out / name)
    shutil.copytree(ROOT / "third-party", args.out / "third-party")
    shutil.copyfile(ROOT / "evidence/sbom.cdx.json", args.out / "sbom.cdx.json")
    lock = []
    seen = set()
    for wheel in sorted(wheels.glob("*.whl")):
        with zipfile.ZipFile(wheel) as archive:
            names = [n for n in archive.namelist() if n.endswith(".dist-info/METADATA")]
            if len(names) != 1:
                raise SystemExit("Unexpected wheel metadata")
            metadata = email.message_from_bytes(archive.read(names[0]))
        name, version = metadata["Name"], metadata["Version"]
        if name.lower().replace("_", "-") in seen:
            raise SystemExit("Duplicate distribution wheel")
        seen.add(name.lower().replace("_", "-"))
        lock.append(
            f"{name}=={version} --hash=sha256:{hashlib.sha256(wheel.read_bytes()).hexdigest()}"
        )
    (args.out / "install-requirements.txt").write_text("\n".join(sorted(lock)) + "\n")
    (args.out / "README-BUNDLE.md").write_text(
        "# Offline local review bundle\n\nNot a public or signed release. See GATE_REPORT.md.\n\n"
        "Verify SHA256SUMS, then install on compatible Linux x86_64 / CPython 3.12:\n\n"
        "```sh\nsha256sum -c SHA256SUMS\npython3.12 -m venv review-env\n"
        "review-env/bin/python -m pip install --no-index --find-links wheelhouse "
        "--require-hashes -r install-requirements.txt\n"
        "review-env/bin/messagebench corpus verify\n```\n\n"
        "Expected: 68 recorded classifications match, including intentional failures. "
        "This does not approve defective transformations or attest independent review.\n\n"
        "The sdist contains the complete original source, build scripts and tests. "
        "native-sources contains original lxml/libxml2/libxslt/libiconv archives with "
        "their notices and licenses, including LGPL-2.1 libiconv source. "
        "Use scripts/build_native.py in the sdist to rebuild/relink the native wheel; "
        "its build-only helper patch is documented. No restriction on debugging or "
        "modification of the LGPL library is imposed. Native binary reproducibility "
        "is not claimed. The bundle is platform-specific, not a manylinux portability claim.\n"
    )
    write_checksums(args.out)
    print("Prepared local review bundle:", args.out)


def write_checksums(directory: Path):
    lines = [
        f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(directory).as_posix()}"
        for p in sorted(directory.rglob("*"))
        if p.is_file() and p.name != "SHA256SUMS"
    ]
    (directory / "SHA256SUMS").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
