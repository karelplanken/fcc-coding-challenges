# Daily Coding challenge #232 (2026-03-30) - freeCodeCamp.org
# Due Date
# Given a date string, return the date 9 months in the future.

# The given and return strings have the format "YYYY-MM-DD".
# If the month nine months into the future doesn't contain the original day number,
# return the last day of that month.
from calendar import monthrange
from datetime import date

from pytest import mark

MONTHS_TO_ADD = 9
MONTHS_PER_YEAR = 12


def get_due_date(date_str: str) -> str:
    dt = date.fromisoformat(date_str)

    if dt.month + MONTHS_TO_ADD > MONTHS_PER_YEAR:
        years_to_add, target_month = divmod(dt.month + MONTHS_TO_ADD, MONTHS_PER_YEAR)
    else:
        target_month = dt.month + MONTHS_TO_ADD
        years_to_add = 0

    target_year = dt.year + years_to_add
    _, max_days_month = monthrange(target_year, target_month)
    # Handle cases where the target month has fewer days than the original day:
    days = min(dt.day, max_days_month)

    return date(target_year, target_month, days).isoformat()


tests = [
    ('2025-03-30', '2025-12-30'),
    ('2025-04-27', '2026-01-27'),
    ('2025-05-29', '2026-02-28'),
    ('2026-06-30', '2027-03-30'),
    ('2026-10-11', '2027-07-11'),
]


@mark.parametrize('date_str, expected', tests)
def test_solution(date_str: str, expected: str) -> None:
    assert get_due_date(date_str) == expected


if __name__ == '__main__':
    date_str, expected = tests[2]
    print(get_due_date(date_str))
