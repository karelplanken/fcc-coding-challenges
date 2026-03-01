# Daily Coding challenge #170 (2026-01-27) - freeCodeCamp.org
# Odd or Even Day
# Given a timestamp (number of milliseconds since the Unix epoch), return:

# "odd" if the day of the month for that timestamp is odd.
# "even" if the day of the month for that timestamp is even.
# For example, given 1769472000000, a timestamp for January 27th, 2026, return "odd"
# because the day number (27) is an odd number.
# Note that the problem description does not specify a timezone, the tests, however,
# require using UTC...
from datetime import datetime, timezone

from pytest import mark


def odd_or_even_day(timestamp: int) -> str:
    day = datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc).day
    return 'even' if day % 2 == 0 else 'odd'


tests = [
    (1769472000000, 'odd'),
    (1769444440000, 'even'),
    (6739456780000, 'odd'),
    (1, 'odd'),
    (86400000, 'even'),
]


@mark.parametrize('timestamp,expected', tests)
def test_odd_or_even_day(timestamp: int, expected: str) -> None:
    assert odd_or_even_day(timestamp) == expected


if __name__ == '__main__':
    timestamp, expected = tests[2]
    print(odd_or_even_day(timestamp))
