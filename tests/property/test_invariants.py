# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
import json

from hypothesis import given, settings
from hypothesis import strategies as st

from aksum_messagebench.comparators import compare_fact
from aksum_messagebench.errors import BenchError
from aksum_messagebench.extractors.pacs008_001_08 import Fact
from aksum_messagebench.reports import canonical_json
from aksum_messagebench.xml_reader import Limits, parse_xml


@given(st.lists(st.text(max_size=80), max_size=20))
@settings(max_examples=200, derandomize=True)
def test_multiset_order_and_multiplicity(values):
    assertion = {"comparator": "multiset", "missing": "compare-presence"}
    before = Fact("list", tuple(values), ())
    after = Fact("list", tuple(reversed(values)), ())
    assert compare_fact(before, after, assertion)[0] == "PASS"
    if values:
        lost = Fact("list", tuple(values[:-1]), ())
        assert compare_fact(before, lost, assertion)[0] == "FAIL"


@given(st.text(max_size=100))
@settings(max_examples=200, derandomize=True)
def test_exact_unicode(text):
    assertion = {"comparator": "exact-text", "missing": "compare-presence"}
    before = Fact("text", (text,), ())
    assert compare_fact(before, before, assertion)[0] == "PASS"
    assert compare_fact(before, Fact("text", (text + "x",), ()), assertion)[0] == "FAIL"


@given(st.binary(max_size=4096))
@settings(max_examples=500, derandomize=True, deadline=None)
def test_parser_fuzz_smoke(data):
    try:
        root = parse_xml(data, Limits(size=4096, depth=12, elements=100, text=1024))
        assert root is not None
    except BenchError as error:
        assert error.exit_code in (1, 4)
        assert len(str(error)) < 80


@given(st.dictionaries(st.text(max_size=20), st.text(max_size=80), max_size=10))
@settings(max_examples=200, derandomize=True)
def test_canonical_order(value):
    assert canonical_json(value) == canonical_json(dict(reversed(list(value.items()))))
    assert json.loads(canonical_json(value)) == value


@given(
    st.one_of(
        st.none(), st.integers(), st.text(max_size=150), st.lists(st.text(max_size=10), max_size=5)
    )
)
@settings(max_examples=200, derandomize=True, deadline=None)
def test_contract_fuzz_smoke(value):
    from pathlib import Path
    from tempfile import TemporaryDirectory

    from aksum_messagebench.assets import data_root
    from aksum_messagebench.contracts import load_contract

    document = json.loads((data_root() / "contracts/pacs008-preserve.json").read_text())
    document["assertions"][0]["comparator"] = value
    with TemporaryDirectory() as directory:
        path = Path(directory) / "fuzz.json"
        path.write_text(json.dumps(document))
        try:
            contract = load_contract(path)
            assert isinstance(contract.document["assertions"][0]["comparator"], str)
        except BenchError as error:
            assert error.exit_code in (2, 4)
