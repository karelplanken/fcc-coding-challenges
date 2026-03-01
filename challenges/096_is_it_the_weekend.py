# Daily Coding challenge #96 (2025-11-14) - freeCodeCamp.org
# Is It the Weekend?
# Given a date in the format "YYYY-MM-DD", return the number of days left until the
# weekend.

# The weekend starts on Saturday.
# If the given date is Saturday or Sunday, return "It's the weekend!".
# Otherwise, return "X days until the weekend.", where X is the number of days until
# Saturday. If X is 1, use "day" (singular) instead of "days" (plural).
# Make sure the calculation ignores your local timezone.
from datetime import date

from pytest import mark


def days_until_weekend(date_string: str) -> str:
    week_day = date.fromisoformat(date_string).weekday()  # Saturday is 5, Sunday is 6
    if week_day > 4:
        return "It's the weekend!"
    num_of_days = 5 - week_day

    return f'{num_of_days} {"day" if num_of_days == 1 else "days"} until the weekend.'


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
    assert days_until_weekend(date_string) == expected


if __name__ == '__main__':
    date_string, expected = tests[2]
    print(days_until_weekend(date_string))
