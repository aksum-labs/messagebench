# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
import pytest

from aksum_messagebench.comparators import compare_fact
from aksum_messagebench.extractors.pacs008_001_08 import Fact
from aksum_messagebench.time_semantics import instant


@pytest.mark.parametrize(
    "left,right,status",
    [
        ("2026-09-29T12:00:00Z", "2026-09-29T15:00:00+03:00", "PASS"),
        ("2026-09-29T24:00:00Z", "2026-09-30T00:00:00Z", "PASS"),
        ("2026-09-29T00:00:00.100Z", "2026-09-29T00:00:00.1Z", "PASS"),
        ("2026-09-29T00:00:00Z", "2026-09-29T00:00:01Z", "FAIL"),
        ("2026-09-29T00:00:00", "2026-09-29T00:00:00", "INDETERMINATE"),
        ("2026-09-29T00:00:00Z", "2026-09-29T00:00:00", "INDETERMINATE"),
        (
            "2026-09-29T00:00:00.123456789012345678901234567890Z",
            "2026-09-29T00:00:00.123456789012345678901234567891Z",
            "FAIL",
        ),
        ("2026-09-29T00:00:00-03:00", "2026-09-29T03:00:00Z", "PASS"),
    ],
)
def test_exact_instants(left, right, status):
    assert (
        compare_fact(
            Fact("datetime", (left,), ()),
            Fact("datetime", (right,), ()),
            {"comparator": "datetime-equal", "missing": "require-present"},
        )[0]
        == status
    )


@pytest.mark.parametrize(
    "value",
    [
        None,
        "x" * 129,
        "-0001-01-01T00:00:00Z",
        "2026-02-30T00:00:00Z",
        "2026-01-01T24:00:01Z",
        "2026-01-01T25:00:00Z",
        "2026-01-01T00:60:00Z",
        "2026-01-01T00:00:60Z",
        "2026-01-01T00:00:00+14:01",
        "2026-01-01T00:00:00+15:00",
        "2026-01-01T00:00:00+01:60",
    ],
)
def test_no_calendar_or_range_guess(value):
    assert instant(value)[1] is not None
