"""Build a pinned local lxml wheel; optional downloads are a developer build step only.

The MessageBench package never imports this script or downloads dependencies.
"""

import argparse
import hashlib
import importlib.metadata
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--archives", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--download", action="store_true")
    args = parser.parse_args()
    pins = json.loads((ROOT / "evidence/native-source-pins.json").read_text())
    for name, version in pins["build_python_dependencies"].items():
        if importlib.metadata.version(name) != version:
            raise SystemExit(
                "Install exact native-build dependencies first: " + name + "==" + version
            )
    args.archives.mkdir(parents=True, exist_ok=True)
    for item in pins["archives"]:
        path = args.archives / item["name"]
        if not path.exists() and args.download:
            subprocess.run(
                [
                    "curl",
                    "--fail",
                    "--location",
                    "--max-time",
                    "600",
                    "--output",
                    str(path),
                    item["source"],
                ],
                check=True,
                timeout=610,
            )
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != item["sha256"]:
            raise SystemExit("Missing or hash-mismatched native source: " + item["name"])
    args.out.mkdir(parents=True, exist_ok=False)
    with tempfile.TemporaryDirectory(prefix="messagebench-native-") as temporary:
        work = Path(temporary)
        with tarfile.open(args.archives / "lxml-6.1.3.tar.gz") as archive:
            archive.extractall(work, filter="data")
        source = work / "lxml-6.1.3"
        (source / "libs").mkdir(exist_ok=True)
        for item in pins["archives"]:
            if not item["name"].startswith("lxml-"):
                shutil.copyfile(args.archives / item["name"], source / "libs" / item["name"])
        # Upstream resolves a directory listing even with pinned versions and local archives.
        # The build-only patch bypasses that unnecessary network lookup. Runtime is unchanged.
        helper = source / "buildlibxml.py"
        original = helper.read_text()
        needle = "def http_find_latest_version_directory(url, version=None):\n"
        if original.count(needle) != 1:
            raise SystemExit("Native build helper changed; review patch")
        modified = original.replace(
            needle,
            needle + "    if version:\n"
            "        return urljoin(url, '.'.join(version.split('.')[:2]) + '/')\n",
        )
        helper.write_text(modified)
        environment = {
            **os.environ,
            "CFLAGS": "-O2 -fPIC",
            "CXXFLAGS": "-O2 -fPIC",
            "STATIC_DEPS": "true",
            "WITHOUT_ZLIB": "true",
            "LIBICONV_VERSION": "1.19",
            "LIBXML2_VERSION": "2.15.4",
            "LIBXSLT_VERSION": "1.1.45",
        }
        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "wheel",
                "--no-index",
                "--no-deps",
                "--no-build-isolation",
                "--wheel-dir",
                str(args.out.absolute()),
                str(source),
            ],
            env=environment,
            check=True,
            timeout=900,
        )
        manifest = {
            "sources": pins,
            "build_helper_original_sha256": hashlib.sha256(original.encode()).hexdigest(),
            "build_helper_modified_sha256": hashlib.sha256(modified.encode()).hexdigest(),
            "patch": "Pinned version directory bypass; no runtime lxml changes.",
            "unsigned_native_reproducibility_claimed": False,
            "wheels": {
                p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in args.out.glob("*.whl")
            },
        }
        (args.out / "native-build.json").write_text(json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    main()
