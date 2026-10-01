# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
"""Canonical redacted evidence and escaped local rendering, without timestamps."""

import html
import json
import os
from pathlib import Path
from xml.etree import ElementTree

from . import SCOPE_NOTICE
from .errors import BenchError


def canonical_json(report: dict) -> bytes:
    return (
        json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n"
    ).encode("utf-8")


def render(report: dict, format: str) -> bytes:
    if format == "json":
        return canonical_json(report)
    if format == "text":
        lines = ["MessageBench", "Overall: " + report["overall"]]
        for side, check in report.get("schema_checks", {}).items():
            lines.append(f"{side} XSD: {check['status']} ({check['code']})")
        for check in report.get("assertions", []):
            lines.append(f"{check['status']} {check['id']} ({check['code']})")
        for case in report.get("cases", []):
            lines.append("Case: " + case["id"])
            lines.append(render(case["result"], "text").decode("utf-8").rstrip())
        lines.append(SCOPE_NOTICE)
        return ("\n".join(lines) + "\n").encode("utf-8")
    if format == "html":
        content = html.escape(canonical_json(report).decode("utf-8"))
        return (
            '<!doctype html><html lang="en"><meta charset="utf-8">'
            '<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; '
            "base-uri 'none'; form-action 'none'\"><title>MessageBench evidence</title>"
            "<h1>MessageBench</h1><p>"
            + html.escape(SCOPE_NOTICE)
            + "</p><pre>"
            + content
            + "</pre></html>\n"
        ).encode("utf-8")
    if format == "junit":
        checks = [
            {"id": side + "-schema", **check, "required": True}
            for side, check in report.get("schema_checks", {}).items()
        ]
        checks.extend(report.get("assertions", []))
        for item in report.get("cases", []):
            child = item["result"]
            child_checks = [
                {"id": side + "-schema", **check, "required": True}
                for side, check in child.get("schema_checks", {}).items()
            ] + child.get("assertions", [])
            if not child_checks:
                child_checks = [
                    {
                        "id": "evidence",
                        "required": True,
                        "status": "INDETERMINATE",
                        "code": child.get("code", "INCOMPLETE"),
                    }
                ]
            checks.extend({**check, "id": item["id"] + "/" + check["id"]} for check in child_checks)
        suite = ElementTree.Element("testsuite", name="MessageBench", tests=str(len(checks)))
        failures = errors = skipped = 0
        for check in checks:
            case = ElementTree.SubElement(suite, "testcase", name=check["id"])
            status = check["status"]
            if status == "FAIL":
                failures += 1
                ElementTree.SubElement(case, "failure", message=check["code"])
            elif status != "PASS":
                if check.get("required") and status in {"INDETERMINATE", "UNSUPPORTED"}:
                    errors += 1
                    ElementTree.SubElement(case, "error", message=check["code"])
                else:
                    skipped += 1
                    ElementTree.SubElement(case, "skipped", message=check["code"])
        suite.set("failures", str(failures))
        suite.set("errors", str(errors))
        suite.set("skipped", str(skipped))
        ElementTree.SubElement(suite, "system-out").text = SCOPE_NOTICE
        return ElementTree.tostring(suite, encoding="utf-8", xml_declaration=True) + b"\n"
    raise BenchError("REPORT_FORMAT_UNSUPPORTED", 2)


def write_new(path: Path, data: bytes) -> None:
    """Atomic exclusive file creation relative to a symlink-free directory chain."""
    if os.name != "posix" or ":" in str(path) or ".." in path.parts:
        raise BenchError("OUTPUT_PATH_UNSAFE", 4)
    path = path.absolute()
    directory = None
    descriptor = None
    try:
        directory = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
        for part in path.parts[1:-1]:
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=directory)
            os.close(directory)
            directory = child
        descriptor = os.open(
            path.name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=directory
        )
        with os.fdopen(descriptor, "wb") as output:
            descriptor = None
            output.write(data)
    except FileExistsError:
        raise BenchError("OUTPUT_EXISTS", 2) from None
    except OSError:
        raise BenchError("OUTPUT_ACCESS_REJECTED", 4) from None
    finally:
        if descriptor is not None:
            os.close(descriptor)
        if directory is not None:
            os.close(directory)
