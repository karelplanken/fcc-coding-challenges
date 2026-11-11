"""Daily Coding Challenge #88 (2025-11-06) - freeCodeCamp.org."""

# Weekday Finder
# Given a string date in the format YYYY-MM-DD, return the day of the week.
#
# Valid return days are:
#
# - "Sunday"
# - "Monday"
# - "Tuesday"
# - "Wednesday"
# - "Thursday"
# - "Friday"
# - "Saturday"
#
# Be sure to ignore time zones.
from datetime import date

from pytest import mark

# Indexed by date.weekday(): Monday == 0 ... Sunday == 6.
_WEEKDAYS = (
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
)


def get_weekday(date_string: str) -> str:
    """Return the English day of the week for a date string.

    Args:
        date_string: A date in the format YYYY-MM-DD.

    Returns:
        The weekday name, e.g. 'Thursday', independent of the current locale.

    Raises:
        ValueError: If date_string is not a valid ISO 8601 date.
    """  # noqa: DOC502
    return _WEEKDAYS[date.fromisoformat(date_string).weekday()]


tests = [
    ('2025-11-06', 'Thursday'),
    ('1999-12-31', 'Friday'),
    ('1111-11-11', 'Saturday'),
    ('2112-12-21', 'Wednesday'),
    ('2345-10-01', 'Monday'),
]


@mark.parametrize(('date_string', 'expected'), tests)
def test_get_weekday(date_string: str, expected: str) -> None:
    """Test get_weekday function."""
    assert get_weekday(date_string) == expected


if __name__ == '__main__':
    date_string, expected = tests[0]
    print(get_weekday(date_string))
