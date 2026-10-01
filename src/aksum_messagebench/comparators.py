# SPDX-FileCopyrightText: 2026 Aksum Labs
# SPDX-License-Identifier: Apache-2.0
"""Typed deterministic comparisons; absence is distinct from an empty value."""

import unicodedata
from collections import Counter
from decimal import Decimal, InvalidOperation

from .extractors.pacs008_001_08 import Fact
from .time_semantics import instant

COMPATIBILITY = {
    "datetime-equal": {"datetime"},
    "exact-text": {"text", "identifier"},
    "exact-identifier": {"identifier", "text"},
    "decimal-equal": {"decimal"},
    "decimal-and-currency-equal": {"money"},
    "presence-equal": {"text", "identifier", "decimal", "money", "list"},
    "ordered-list": {"list"},
    "multiset": {"list"},
    "allowed-regeneration": {"identifier", "text"},
}


def compare_fact(before: Fact, after: Fact, assertion: dict) -> tuple[str, str]:
    mode = assertion["comparator"]
    if mode not in COMPATIBILITY:
        return "UNSUPPORTED", "COMPARATOR_UNSUPPORTED"
    if before.kind != after.kind or before.kind not in COMPATIBILITY[mode]:
        return "UNSUPPORTED", "COMPARATOR_TYPE_UNSUPPORTED"
    normalization = assertion.get("normalization", "none")
    if normalization != "none" and (mode not in {"exact-text", "ordered-list", "multiset"}):
        return "UNSUPPORTED", "NORMALIZATION_TYPE_UNSUPPORTED"
    if normalization not in {"none", "NFC"}:
        return "UNSUPPORTED", "NORMALIZATION_UNSUPPORTED"
    if not before.values or not after.values:
        if before.presence != after.presence:
            return "FAIL", "PRESENCE_CHANGED"
        if assertion["missing"] == "compare-presence":
            return "PASS", "PRESENCE_EQUAL"
        return "INDETERMINATE", "REQUIRED_VALUE_ABSENT"
    if before.kind != "list" and (len(before.values) != 1 or len(after.values) != 1):
        return "INDETERMINATE", "CARDINALITY_AMBIGUOUS"
    if mode == "presence-equal":
        equal = before.presence == after.presence
    elif mode == "allowed-regeneration":
        equal = bool(before.values[0]) and bool(after.values[0])
        return ("PASS", "REGENERATION_PERMITTED") if equal else ("FAIL", "EMPTY_IDENTIFIER")
    elif mode == "datetime-equal":
        left_time, left_error = instant(before.values[0])
        right_time, right_error = instant(after.values[0])
        if left_error or right_error:
            return "INDETERMINATE", left_error or right_error or "DATETIME_UNSUPPORTED"
        equal = left_time == right_time
    elif mode in {"decimal-equal", "decimal-and-currency-equal"}:
        try:
            if mode == "decimal-equal":
                left, right = Decimal(before.values[0]), Decimal(after.values[0])
                same_currency = True
            else:
                left, right = Decimal(before.values[0][0]), Decimal(after.values[0][0])
                same_currency = before.values[0][1] == after.values[0][1]
                if before.values[0][1] is None or after.values[0][1] is None:
                    return "INDETERMINATE", "CURRENCY_ABSENT"
            if not left.is_finite() or not right.is_finite():
                return "INDETERMINATE", "DECIMAL_NONFINITE"
            equal = left == right and same_currency
        except (InvalidOperation, TypeError, ValueError):
            return "INDETERMINATE", "DECIMAL_INVALID"
    else:
        left_values, right_values = before.values, after.values
        if normalization == "NFC":
            left_values = tuple(unicodedata.normalize("NFC", s) for s in left_values)
            right_values = tuple(unicodedata.normalize("NFC", s) for s in right_values)
        equal = (
            Counter(left_values) == Counter(right_values)
            if mode == "multiset"
            else left_values == right_values
        )
    return ("PASS", "PRESERVED") if equal else ("FAIL", "PRESERVATION_CHANGED")
