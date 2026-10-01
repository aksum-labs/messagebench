# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
import json
import os

import pytest

from aksum_messagebench.contracts import load_contract
from aksum_messagebench.errors import BenchError, aggregate_exit
from aksum_messagebench.input_guard import load_json, read_local
from aksum_messagebench.reports import write_new
from aksum_messagebench.schema_catalog import Catalog


@pytest.mark.parametrize("path", ["https://example.invalid/x", "../secret", "file:///etc/passwd"])
def test_bad_paths(path):
    with pytest.raises(BenchError):
        read_local(path)


def test_symlinks_and_fifo(source, tmp_path):
    link = tmp_path / "link"
    link.symlink_to(source)
    fifo = tmp_path / "fifo"
    os.mkfifo(fifo)
    for path in (link, fifo, tmp_path):
        with pytest.raises(BenchError) as err:
            read_local(path)
        assert err.value.exit_code == 4
    nested = tmp_path / "dir"
    nested.symlink_to(source.parent, target_is_directory=True)
    with pytest.raises(BenchError):
        read_local(nested / source.name)
    with pytest.raises(BenchError):
        write_new(link, b"unchanged")


def test_size_limit(tmp_path):
    p = tmp_path / "large"
    p.write_bytes(b"x" * 11)
    with pytest.raises(BenchError) as err:
        read_local(p, limit=10)
    assert err.value.code == "INPUT_SIZE_LIMIT"


@pytest.mark.parametrize(
    "payload", ['{"a":1,"a":2}', '{"a":NaN}', "[]", "{", '{"a":' + "[" * 40 + "0" + "]" * 40 + "}"]
)
def test_json_rejections(tmp_path, payload):
    path = tmp_path / "bad.json"
    path.write_text(payload)
    with pytest.raises(BenchError):
        load_json(path)


@pytest.mark.parametrize(
    "edit",
    [
        lambda d: d.update(execute="sh"),
        lambda d: d["assertions"][0].update(xpath="//MsgId"),
        lambda d: d["assertions"][0].update(comparator="python"),
        lambda d: d["assertions"].append(d["assertions"][0]),
        lambda d: d.update(assertions=[]),
        lambda d: d.update(assertions=[{**a, "required": False} for a in d["assertions"]]),
        lambda d: d.update(exclusions=[{"field": "message.id", "reason": "conflict"}]),
        lambda d: d.update(association={"mode": "keyed"}),
    ],
)
def test_contract_rejections(change_contract, edit):
    with pytest.raises(BenchError) as err:
        load_contract(change_contract(edit))
    assert err.value.exit_code == 2


def test_tampered_catalog(root, tmp_path):
    data = json.loads((root / "schemas/catalog.json").read_text())
    data["schemas"][0]["sha256"] = "0" * 64
    path = tmp_path / "catalog.json"
    path.write_text(json.dumps(data))
    with pytest.raises(BenchError) as err:
        Catalog(path)
    assert err.value.code == "CATALOG_UNREVIEWED_SCHEMA"


def test_exclusive_output(tmp_path):
    path = tmp_path / "report.json"
    write_new(path, b"first")
    with pytest.raises(BenchError) as err:
        write_new(path, b"second")
    assert err.value.code == "OUTPUT_EXISTS"
    assert path.read_bytes() == b"first"


def test_exit_precedence():
    assert aggregate_exit([1, 3, 2, 4, 5]) == 5
    assert aggregate_exit([1, 3, 2, 4]) == 4
    assert aggregate_exit([1, 3, 2]) == 2
    assert aggregate_exit([1, 3]) == 3
    assert aggregate_exit([0, 1]) == 1
    assert aggregate_exit([0]) == 0
    assert aggregate_exit([]) == 3
