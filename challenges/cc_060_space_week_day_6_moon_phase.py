"""Daily Coding Challenge #60 (2025-10-09) - freeCodeCamp.org."""

# Space Week Day 6: Moon Phase
# For day six of Space Week, you will be given a date in the format "YYYY-MM-DD" and
# need to determine the phase of the moon for that day using the following rules:
#
# Use a simplified lunar cycle of 28 days, divided into four equal phases:
#
# - "New": days 1 - 7
# - "Waxing": days 8 - 14
# - "Full": days 15 - 21
# - "Waning": days 22 - 28
#
# After day 28, the cycle repeats with day 1, a new moon.
#
# - Use "2000-01-06" as a reference new moon (day 1 of the cycle) to determine the phase
#   of the given day.
# - You will not be given any dates before the reference date.
# - Return the correct phase as a string.
#
# **Note:** Day 1 represents the day of the new moon, meaning 0 days have passed since
# the last new moon.
from datetime import date

from pytest import mark

_REFERENCE_NEW_MOON = date(2000, 1, 6)
_PHASES = ('New', 'Waxing', 'Full', 'Waning')
_PHASE_DAYS = 7
_CYCLE_DAYS = _PHASE_DAYS * len(_PHASES)


def moon_phase(date_string: str) -> str:
    """Determine the phase of the moon for a given date.

    Uses a simplified 28-day lunar cycle of four 7-day phases, counted from the
    reference new moon on 2000-01-06 (cycle day 1).

    Args:
        date_string: An ISO 8601 calendar date, typically "YYYY-MM-DD". Any
            form accepted by `datetime.date.fromisoformat` is allowed (on
            Python 3.11+ this includes "YYYYMMDD" and week dates such as
            "2000-W01-4").

    Returns:
        One of "New", "Waxing", "Full", or "Waning".

    Raises:
        ValueError: If the string is not a valid ISO 8601 date or the date is
            before the reference date 2000-01-06.
    """
    try:
        day = date.fromisoformat(date_string)
    except ValueError as exc:
        msg = f'date must be an ISO 8601 date (e.g. YYYY-MM-DD), got {date_string!r}'
        raise ValueError(msg) from exc

    elapsed = (day - _REFERENCE_NEW_MOON).days
    if elapsed < 0:
        msg = (
            f'date must be on or after {_REFERENCE_NEW_MOON.isoformat()}, '
            f'got {date_string!r}'
        )
        raise ValueError(msg)

    return _PHASES[(elapsed % _CYCLE_DAYS) // _PHASE_DAYS]


tests = [
    ('2000-01-12', 'New'),
    ('2000-01-13', 'Waxing'),
    ('2014-10-15', 'Full'),
    ('2012-10-21', 'Waning'),
    ('2022-12-14', 'New'),
]


@mark.parametrize('date_string, expected', tests)
def test_moon_phase(date_string: str, expected: str) -> None:
    """Test moon_phase function."""
    assert moon_phase(date_string) == expected


if __name__ == '__main__':
    date_string, expected = tests[0]
    print(moon_phase(date_string))
