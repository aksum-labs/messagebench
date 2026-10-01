# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
import sys


def run(root, *args):
    env = {**os.environ, "PYTHONPATH": str(root / "src")}
    return subprocess.run(
        [sys.executable, "-m", "aksum_messagebench", *map(str, args)],
        cwd=root,
        env=env,
        capture_output=True,
        timeout=20,
    )


def test_cli_demo_and_safe_errors(root, source, contract, tmp_path):
    result = run(root, "compare", source, root / "corpus/negative/reference-truncated.target.xml")
    assert result.returncode == 1
    assert b"FAIL PRESERVE-END-TO-END-ID" in result.stdout
    assert b"1250.50" not in result.stdout
    result = run(root, "compare", source, source, "--contract", tmp_path / "missing.json")
    assert result.returncode == 2
    result = run(root, "inspect", source)
    assert result.returncode == 0
    result = run(
        root, "compare", source, source, "--out", tmp_path / "out.json", "--format", "json"
    )
    assert result.returncode == 0
    result = run(root, "corpus", "verify")
    assert result.returncode == 0
