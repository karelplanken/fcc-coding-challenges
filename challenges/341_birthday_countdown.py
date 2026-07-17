# Daily Coding challenge #341 (2026-07-17) - freeCodeCamp.org
# Birthday Countdown
# Given today's date and a birthday, return the number of days until the person's next
# birthday.
#
# - Today's date is given as a string in `"YYYY-MM-DD"` format, with leading zeros, for
#   example: `"2026-07-16"`.
# - The birthday is given as a string in `"M/D"` format, without leading zeros, for
#   example: `"9/7"`.
# - If today is their birthday, return the number of days until their next birthday (not
#   `0`).
# - Leap years should be accounted for.
from calendar import isleap
from datetime import date

from pytest import mark

EXTRA_DATE_LEAP_YEAR = (2, 29)


def days_until_birthday(today: str, birthday: str) -> int:
    month, day = map(int, birthday.split('/'))
    today_dt = date.fromisoformat(today)

    year = today_dt.year
    while True:
        if (month, day) != EXTRA_DATE_LEAP_YEAR or isleap(year):
            candidate = date(year, month, day)
            if candidate > today_dt:
                return (candidate - today_dt).days
        year += 1


tests = [
    ('2026-07-16', '9/7', 53),
    ('2026-07-16', '3/22', 249),
    ('2026-07-16', '7/16', 365),
    ('2024-02-28', '3/1', 2),
    ('2023-04-24', '12/30', 250),
    ('2024-03-01', '2/29', 1460),
    ('2096-03-01', '2/29', 2920),
]


@mark.parametrize('today, birthday, expected', tests)
def test_days_until_birthday(today: str, birthday: str, expected: int) -> None:
    assert days_until_birthday(today, birthday) == expected


if __name__ == '__main__':
    today, birthday, expected = tests[0]
    print(days_until_birthday(today, birthday))
