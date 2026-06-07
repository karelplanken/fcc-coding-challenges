# Daily Coding challenge #301 (2026-06-07) - freeCodeCamp.org
# Last Load
# Given the number of scoops of laundry detergent you have remaining and an array of
# how many scoops you used in each of the previous days, return the number of full days
# of detergent you have remaining.
# Calculate your average daily usage from the usage history and assume that amount of
# usage each day going forward.
from pytest import mark


def last_load_date(scoops: int, usage: list[int]) -> int:
    daily_average = sum(usage) / len(usage)
    return int(scoops / daily_average)


tests = [
    (10, [2, 2, 2, 2, 2, 2, 2], 5),
    (16, [2, 3, 0, 3, 4, 2, 1], 7),
    (33, [5, 0, 4, 3, 3, 2], 11),
    (50, [2, 0, 2, 9, 12, 0, 2], 12),
    (20, [13, 9, 12, 10, 8], 1),
]


@mark.parametrize('scoops, usage, expected', tests)
def test(scoops: int, usage: list[int], expected: int) -> None:
    assert last_load_date(scoops, usage) == expected


if __name__ == '__main__':
    scoops, usage, expected = tests[0]
    print(last_load_date(scoops, usage))
