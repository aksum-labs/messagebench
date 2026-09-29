"""Bounded exact XSD dateTime comparison; no guessed timezone or calendar."""

import re
from datetime import date
from decimal import Decimal

_PATTERN = re.compile(
    r"([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})"
    r"(\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})?"
)


def instant(value: str) -> tuple[tuple[int, Decimal] | None, str | None]:
    if not isinstance(value, str) or len(value) > 128:
        return None, "DATETIME_RANGE_UNSUPPORTED"
    match = _PATTERN.fullmatch(value)
    if match is None:
        return None, "DATETIME_CALENDAR_OR_LEXICAL_UNSUPPORTED"
    year, month, day, hour, minute, second = map(int, match.group(*range(1, 7)))
    try:
        ordinal = date(year, month, day).toordinal()
    except ValueError:
        return None, "DATETIME_CALENDAR_OR_LEXICAL_UNSUPPORTED"
    fraction = Decimal(match[7] or "0")
    if minute > 59 or second > 59 or hour > 24 or (hour == 24 and (minute or second or fraction)):
        return None, "DATETIME_CALENDAR_OR_LEXICAL_UNSUPPORTED"
    zone = match[8]
    if zone is None:
        return None, "DATETIME_TIMEZONE_UNKNOWN"
    offset = 0
    if zone != "Z":
        zh, zm = int(zone[1:3]), int(zone[4:6])
        if zh > 14 or zm > 59 or (zh == 14 and zm):
            return None, "DATETIME_CALENDAR_OR_LEXICAL_UNSUPPORTED"
        offset = (zh * 3600 + zm * 60) * (1 if zone[0] == "+" else -1)
    # Keep fractions separate: Decimal arithmetic must not round under ambient precision.
    return (ordinal * 86400 + hour * 3600 + minute * 60 + second - offset, fraction), None
