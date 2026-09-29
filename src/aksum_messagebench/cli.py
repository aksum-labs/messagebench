"""Offline CLI. Runtime inputs cannot invoke executables, plugins or downloads."""

import argparse
import sys
from pathlib import Path

from . import SCOPE_NOTICE, __version__
from .assets import data_root
from .corpus import verify
from .engine import compare, inspect_file
from .errors import BenchError
from .reports import canonical_json, render, write_new
from .schema_catalog import Catalog
from .workflows import load_result, regression, suite


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="messagebench", description=__doc__)
    parser.add_argument("--version", action="version", version=__version__)
    commands = parser.add_subparsers(dest="command", required=True)
    inspect = commands.add_parser("inspect")
    inspect.add_argument("input", type=Path)
    inspect.add_argument("--catalog", type=Path)
    cmp = commands.add_parser("compare")
    cmp.add_argument("source", type=Path)
    cmp.add_argument("target", type=Path)
    cmp.add_argument(
        "--contract", type=Path, default=data_root() / "contracts/pacs008-preserve.json"
    )
    cmp.add_argument("--catalog", type=Path)
    cmp.add_argument("--format", choices=["json", "text", "html", "junit"], default="text")
    cmp.add_argument("--out", type=Path)
    corpus = commands.add_parser("corpus")
    sub = corpus.add_subparsers(dest="corpus_command", required=True)
    verification = sub.add_parser("verify")
    verification.add_argument(
        "manifest", type=Path, nargs="?", default=data_root() / "corpus/index.json"
    )
    batch = commands.add_parser("suite")
    batch.add_argument("manifest", type=Path)
    batch.add_argument("--outputs", type=Path, required=True)
    batch.add_argument(
        "--contract", type=Path, default=data_root() / "contracts/pacs008-preserve.json"
    )
    batch.add_argument("--out", type=Path, required=True)
    conversion = commands.add_parser("report")
    conversion.add_argument("input", type=Path)
    conversion.add_argument("--format", choices=["json", "text", "html", "junit"], required=True)
    conversion.add_argument("--out", type=Path, required=True)
    diff = commands.add_parser("regression")
    diff.add_argument("previous", type=Path)
    diff.add_argument("current", type=Path)
    verification.add_argument("--contract", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "compare":
            report = compare(args.source, args.target, args.contract, args.catalog)
            payload = render(report, args.format)
            if args.out:
                write_new(args.out, payload)
            else:
                sys.stdout.buffer.write(payload)
        elif args.command == "suite":
            report = suite(args.manifest, args.outputs, args.contract)
            # Require an existing directory; write_new refuses symlinks and overwrites.
            write_new(args.out / "result.json", canonical_json(report))
            sys.stdout.buffer.write(canonical_json(report))
        elif args.command == "report":
            report = load_result(args.input)
            write_new(args.out, render(report, args.format))
        elif args.command == "regression":
            report = regression(load_result(args.previous), load_result(args.current))
            sys.stdout.buffer.write(canonical_json(report))
        elif args.command == "inspect":
            check, _ = inspect_file(args.input, Catalog(args.catalog))
            report = {
                "overall": check["status"],
                "exit_code": check["exit_code"],
                "schema_checks": {"input": check},
                "limitations": [SCOPE_NOTICE],
            }
            sys.stdout.buffer.write(canonical_json(report))
        else:
            report = verify(args.manifest, args.contract)
            sys.stdout.buffer.write(canonical_json(report))
        return report["exit_code"]
    except BenchError as exc:
        sys.stdout.buffer.write(
            canonical_json(
                {
                    "overall": "INDETERMINATE",
                    "code": exc.code,
                    "exit_code": exc.exit_code,
                    "limitations": [SCOPE_NOTICE],
                }
            )
        )
        return exc.exit_code
    except Exception:
        # Do not expose XML-library tracebacks, filenames or payloads.
        sys.stdout.buffer.write(
            canonical_json(
                {
                    "overall": "INDETERMINATE",
                    "code": "INTERNAL_ERROR",
                    "exit_code": 5,
                    "limitations": [SCOPE_NOTICE],
                }
            )
        )
        return 5
