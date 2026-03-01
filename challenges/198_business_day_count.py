# Daily Coding challenge #198 (2026-02-24) - freeCodeCamp.org
# Business Day Count
# Given a start date and an end date, return the number of business days between the
# two.

# Given dates are in the format "YYYY-MM-DD".
# Weekdays are business days (Monday through Friday).
# Weekends are not business days (Saturday and Sunday).
# Include both the start and end dates when counting.
from datetime import date, timedelta

from pytest import mark


def count_business_days(start: str, end: str) -> int:
    start_date = date.fromisoformat(start)
    end_date = date.fromisoformat(end)
    weekend_days = {'Saturday', 'Sunday'}

    return sum(
        1
        for i in range(0, (end_date - start_date).days + 1)
        # if (start_date + timedelta(days=i)).weekday() < 5
        if (start_date + timedelta(days=i)).strftime('%A') not in weekend_days
    )


tests = [
    ('2026-02-24', '2026-02-26', 3),
    ('2026-02-24', '2026-02-28', 4),
    ('2026-02-21', '2026-03-01', 5),
    ('2026-03-08', '2026-03-17', 7),
    ('2026-02-24', '2027-02-24', 262),
]


@mark.parametrize('start, end, expected', tests)
def test(start: str, end: str, expected: int) -> None:
    assert count_business_days(start, end) == expected


if __name__ == '__main__':
    start, end, expected = tests[1]
    print(count_business_days(start, end))
