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
    parser.add_argument(
        "--wheel-cache",
        type=Path,
        help="Reuse cleared local dependency wheels without contacting an index",
    )
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.wheel_cache is not None and not args.wheel_cache.is_dir():
        raise SystemExit("Local wheel cache must be a directory")
    args.out.mkdir(parents=True, exist_ok=False)
    wheels = args.out / "wheelhouse"
    wheels.mkdir()
    native_manifest = json.loads((args.native / "native-build.json").read_text())
    for name, digest in native_manifest["wheels"].items():
        path = args.native / name
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise SystemExit("Native wheel hash mismatch")
        shutil.copyfile(path, wheels / name)
    release_hashes = json.loads((ROOT / "evidence/dependency-release-hashes.json").read_text())
    hashes_by_pin = {
        key.lower().replace("_", "-"): value["files"] for key, value in release_hashes.items()
    }
    requirements = [
        line
        for line in (ROOT / "runtime-lock.txt").read_text().splitlines()
        if not line.lower().startswith("lxml==")
    ]
    requirements.append("pip==26.2.1")
    download = args.out / "download-requirements.txt"
    download.write_text(
        "\n".join(
            pin
            + " "
            + " ".join(
                "--hash=sha256:" + item["sha256"]
                for item in hashes_by_pin[pin.lower().replace("_", "-")]
            )
            for pin in requirements
        )
        + "\n"
    )
    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "download",
            *(
                ["--no-index", "--find-links", str(args.wheel_cache.resolve())]
                if args.wheel_cache is not None
                else []
            ),
            "--only-binary=:all:",
            "--require-hashes",
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
    for name in [
        "LICENSE",
        "NOTICE",
        "GATE_REPORT.md",
        "RELEASE_READINESS.md",
        "LIMITATIONS.md",
        "FINAL_COMPLETION_REPORT.md",
    ]:
        shutil.copyfile(ROOT / name, args.out / name)
    shutil.copytree(ROOT / "third-party", args.out / "third-party")
    shutil.copyfile(ROOT / "evidence/sbom.cdx.json", args.out / "sbom.cdx.json")
    license_policy = {
        i["name"]: i
        for i in json.loads((ROOT / "evidence/dependency-license-policy.json").read_text())[
            "dependencies"
        ]
    }
    bundle_rights = []
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
        normalized = name.lower().replace("_", "-")
        bundle_rights.append(
            {
                "name": name,
                "version": version,
                "file": "wheelhouse/" + wheel.name,
                "sha256": hashlib.sha256(wheel.read_bytes()).hexdigest(),
                "source": "Aksum original source"
                if normalized in {"messagebench", "aksum-messagebench"}
                else "https://pypi.org/project/" + name + "/" + version + "/",
                "license_or_terms": "Apache-2.0"
                if normalized in {"messagebench", "aksum-messagebench"}
                else license_policy[normalized]["license_expression"],
                "modified": normalized == "lxml",
                "redistribution_status": (
                    "Included with package notices; "
                    "lxml native licenses/source obligations additional."
                ),
                "inclusion_decision": "offline review bundle",
            }
        )
        lock.append(
            f"{name}=={version} --hash=sha256:{hashlib.sha256(wheel.read_bytes()).hexdigest()}"
        )
    native_licenses = {
        "libiconv": "LGPL-2.1-or-later AND GPL-3.0-or-later",
        "libxml2": "MIT",
        "libxslt": "MIT",
        "lxml": "BSD-3-Clause",
    }
    for item in pins["archives"]:
        component = item["name"].split("-")[0]
        bundle_rights.append(
            {
                "name": item["name"],
                "source": item["source"],
                "sha256": item["sha256"],
                "version": item["name"].split("-", 1)[1].split(".tar")[0],
                "license_or_terms": native_licenses[component],
                "modified": False,
                "redistribution_status": (
                    "Original source and license notices included; rebuild/relink recipe supplied."
                ),
                "inclusion_decision": "native-sources/" + item["name"],
            }
        )
    (args.out / "bundle-rights-register.json").write_text(
        json.dumps(
            {
                "assets": bundle_rights,
                "additional_native_wheel_terms": (
                    "The lxml wheel includes libxml2/libxslt MIT "
                    "and libiconv LGPL-2.1-or-later; corresponding source archives "
                    "and build helper "
                    "are included."
                ),
                "schema_terms": "See the source rights register and retained SWIFTStandards terms.",
            },
            indent=2,
        )
        + "\n"
    )
    (args.out / "install-requirements.txt").write_text("\n".join(sorted(lock)) + "\n")
    (args.out / "README-BUNDLE.md").write_text(
        "# Offline engineering artifact bundle\n\n"
        "A bundle alone is not a reviewed release. Check its exact workflow/ref, "
        "attached signature and review status; signatures do not establish "
        "independent review or production safety. See RELEASE_READINESS.md.\n\n"
        "Verify SHA256SUMS, then install on compatible Linux x86_64 / CPython 3.12:\n\n"
        "```sh\nsha256sum -c SHA256SUMS\npython3.12 -m venv review-env\n"
        "review-env/bin/python -m pip install --no-index --find-links wheelhouse "
        "--require-hashes -r install-requirements.txt\n"
        "review-env/bin/messagebench corpus verify\n```\n\n"
        "Expected: 100 recorded classifications match, including intentional failures. "
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
