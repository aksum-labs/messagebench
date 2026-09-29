import pytest

from aksum_messagebench.comparators import compare_fact
from aksum_messagebench.extractors.pacs008_001_08 import Fact


def check(kind, left, right, mode, missing="require-present", normalization="none"):
    return compare_fact(
        Fact(kind, left, ()),
        Fact(kind, right, ()),
        {"comparator": mode, "missing": missing, "normalization": normalization},
    )


@pytest.mark.parametrize(
    "kind,left,right,mode,want",
    [
        ("identifier", ("0001",), ("1",), "exact-identifier", "FAIL"),
        ("identifier", ("0001",), ("0001",), "exact-identifier", "PASS"),
        ("text", (" a",), ("a",), "exact-text", "FAIL"),
        ("text", ("A",), ("a",), "exact-text", "FAIL"),
        ("text", ("ሙከራ",), ("ሙከራ",), "exact-text", "PASS"),
        ("text", ("ሙከራ",), ("test",), "exact-text", "FAIL"),
        ("text", ("é",), ("e\u0301",), "exact-text", "FAIL"),
        ("list", ("a", "b"), ("b", "a"), "multiset", "PASS"),
        ("list", ("a", "a"), ("a",), "multiset", "FAIL"),
        ("list", ("a",), ("a", "a"), "multiset", "FAIL"),
        ("list", ("a", "b"), ("b", "a"), "ordered-list", "FAIL"),
        ("list", ("a", "b"), ("a", "b"), "ordered-list", "PASS"),
        ("money", (("100.00", "ETB"),), (("100.0", "ETB"),), "decimal-and-currency-equal", "PASS"),
        ("money", (("100.00", "ETB"),), (("100.0", "USD"),), "decimal-and-currency-equal", "FAIL"),
        ("money", (("100.01", "ETB"),), (("100.0", "ETB"),), "decimal-and-currency-equal", "FAIL"),
        ("money", (("1", None),), (("1", "ETB"),), "decimal-and-currency-equal", "INDETERMINATE"),
        ("decimal", ("1.00",), ("1.0",), "decimal-equal", "PASS"),
        ("decimal", ("bad",), ("1.0",), "decimal-equal", "INDETERMINATE"),
        ("decimal", ("NaN",), ("1.0",), "decimal-equal", "INDETERMINATE"),
        ("decimal", ("Infinity",), ("1.0",), "decimal-equal", "INDETERMINATE"),
        ("text", ("A",), ("B",), "allowed-regeneration", "PASS"),
        ("text", ("",), ("B",), "allowed-regeneration", "FAIL"),
        ("text", (), (), "exact-text", "INDETERMINATE"),
        ("text", ("a",), (), "exact-text", "FAIL"),
        ("text", (), ("a",), "exact-text", "FAIL"),
        ("text", ("a", "b"), ("a",), "exact-text", "INDETERMINATE"),
        ("text", ("a",), ("a", "b"), "exact-text", "INDETERMINATE"),
        ("text", ("a",), ("a",), "keyed-items", "UNSUPPORTED"),
        ("text", ("a",), ("a",), "decimal-equal", "UNSUPPORTED"),
        ("text", ("a",), ("b",), "presence-equal", "PASS"),
        ("text", ("",), ("b",), "presence-equal", "FAIL"),
    ],
)
def test_semantics(kind, left, right, mode, want):
    assert check(kind, left, right, mode)[0] == want


def test_explicit_normalization():
    assert check("text", ("é",), ("e\u0301",), "exact-text", normalization="NFC")[0] == "PASS"
    assert (
        check("identifier", ("é",), ("e\u0301",), "exact-identifier", normalization="NFC")[0]
        == "UNSUPPORTED"
    )
    assert check("text", ("a",), ("a",), "exact-text", normalization="casefold")[0] == "UNSUPPORTED"


def test_presence_and_types():
    assert check("text", (), (), "exact-text", missing="compare-presence")[0] == "PASS"
    assert Fact("text", ("",), ()).presence == "present-empty"
    assert (
        compare_fact(
            Fact("text", ("1",), ()), Fact("identifier", ("1",), ()), {"comparator": "exact-text"}
        )[0]
        == "UNSUPPORTED"
    )
