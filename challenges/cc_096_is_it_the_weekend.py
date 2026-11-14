"""Daily Coding Challenge #96 (2025-11-14) - freeCodeCamp.org."""

# Is It the Weekend?
# Given a date in the format "YYYY-MM-DD", return the number of days left until the
# weekend.
#
# - The weekend starts on Saturday.
# - If the given date is Saturday or Sunday, return "It's the weekend!".
# - Otherwise, return "X days until the weekend.", where X is the number of days until
#   Saturday.
# - If X is 1, use "day" (singular) instead of "days" (plural).
# - Make sure the calculation ignores your local timezone.
from calendar import SATURDAY
from datetime import date

from pytest import mark


def days_until_weekend(date_string: str) -> str:
    """Return the number of days until the weekend for a date string.

    The date is parsed with ``datetime.date.fromisoformat``, so any ISO
    8601 calendar or week date it accepts is valid input, not only the
    extended ``YYYY-MM-DD`` form.

    Args:
        date_string: An ISO 8601 date: extended (``2025-11-14``), basic
            (``20251114``), or week date (``2025-W46-5``).

    Returns:
        The number of days until Saturday, or that it's the weekend.

    Raises:
        ValueError: If ``date_string`` is not a valid ISO 8601 date, or names
            a date that does not exist.

    Examples:
        >>> days_until_weekend('2025-11-14')
        '1 day until the weekend.'
        >>> days_until_weekend('20251114')
        '1 day until the weekend.'
        >>> days_until_weekend('2025-W46-5')
        '1 day until the weekend.'
        >>> days_until_weekend('2025-02-30')  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
            ...
        ValueError: ...
    """  # noqa: DOC502
    days = SATURDAY - date.fromisoformat(date_string).weekday()
    if days <= 0:  # Saturday -> 0, Sunday -> -1
        return "It's the weekend!"
    unit = 'day' if days == 1 else 'days'
    return f'{days} {unit} until the weekend.'


tests = [
    ('2025-11-14', '1 day until the weekend.'),
    ('2025-01-01', '3 days until the weekend.'),
    ('2025-12-06', "It's the weekend!"),
    ('2026-01-27', '4 days until the weekend.'),
    ('2026-09-07', '5 days until the weekend.'),
    ('2026-11-29', "It's the weekend!"),
]


@mark.parametrize(('date_string', 'expected'), tests)
def test_days_until_weekend(date_string: str, expected: str) -> None:
    """Test days_until_weekend function."""
    assert days_until_weekend(date_string) == expected


if __name__ == '__main__':
    date_string, expected = tests[0]
    print(days_until_weekend(date_string))
