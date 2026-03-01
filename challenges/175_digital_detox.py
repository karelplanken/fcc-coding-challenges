# Daily Coding challenge #175 (2026-02-01) - freeCodeCamp.org
# Digital Detox
# Given an array of your login logs, determine whether you have met your digital detox
# goal.

# Each log is a string in the format "YYYY-MM-DD HH:mm:ss".

# You have met your digital detox goal if both of the following statements are true:

# You logged in no more than once within any four-hour period.
# You logged in no more than 2 times on any single day.
from collections import Counter
from datetime import datetime, timedelta
from itertools import pairwise

from pytest import mark


def digital_detox(logs: list[str]) -> bool:
    if len(logs) <= 1:
        return True

    # Parse and sort timestamps once
    timestamps = sorted(datetime.fromisoformat(log) for log in logs)

    # Check constraint 1: No more than once within any 4-hour period
    four_hours = timedelta(hours=4)
    if any(curr - prev < four_hours for prev, curr in pairwise(timestamps)):
        return False

    # Check constraint 2: No more than 2 logins per day
    daily_counts = Counter(ts.date() for ts in timestamps)
    if max(daily_counts.values()) > 2:
        return False

    return True


tests = [
    (['2026-02-01 08:00:00', '2026-02-01 12:30:00'], True),
    (['2026-02-01 04:00:00', '2026-02-01 07:30:00'], False),
    (
        [
            '2026-01-31 08:21:30',
            '2026-01-31 14:30:00',
            '2026-02-01 08:00:00',
            '2026-02-01 12:30:00',
        ],
        True,
    ),
    (
        [
            '2026-01-31 10:40:21',
            '2026-01-31 15:19:41',
            '2026-01-31 21:49:50',
            '2026-02-01 09:30:00',
        ],
        False,
    ),
    (
        [
            '2026-02-05 10:00:00',
            '2026-02-01 09:00:00',
            '2026-02-03 22:15:00',
            '2026-02-02 12:10:00',
            '2026-02-02 07:15:00',
            '2026-02-04 09:45:00',
            '2026-02-01 16:50:00',
            '2026-02-03 09:30:00',
        ],
        True,
    ),
    (
        [
            '2026-02-05 10:00:00',
            '2026-02-01 09:00:00',
            '2026-02-03 22:15:00',
            '2026-02-02 12:10:00',
            '2026-02-02 07:15:00',
            '2026-02-04 01:45:00',
            '2026-02-01 16:50:00',
            '2026-02-03 09:30:00',
        ],
        False,
    ),
]


@mark.parametrize('logs, expected', tests)
def test_digital_detox(logs: list[str], expected: bool) -> None:
    assert digital_detox(logs) == expected


if __name__ == '__main__':
    logs, expected = tests[0]
    print(digital_detox(logs))
