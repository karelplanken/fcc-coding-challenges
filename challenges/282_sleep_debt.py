# Daily Coding challenge #282 (2026-05-19) - freeCodeCamp.org
# Sleep Debt
# Given an array of hours slept each night leading up to today, and a target number of
# hours per night, return how many hours of sleep you need tonight to eliminate your
# sleep debt.
# Include tonight's hours in the total time needed to catch up.
# If you've slept enough to cover tonight's target or more, return 0.
from pytest import mark


def sleep_debt(hours_slept: list[int], target_hours: int) -> int:
    return max(0, target_hours * (len(hours_slept) + 1) - sum(hours_slept))


tests = [
    ([6, 6, 6, 6, 6, 6], 8, 20),
    ([6, 7, 8, 4, 8, 6], 7, 10),
    ([10, 10, 9, 10, 9, 11], 9, 4),
    ([8, 7, 6, 7, 6, 8], 6, 0),
    ([8, 9, 10, 9, 10, 7], 7, 0),
]


@mark.parametrize('hours_slept, target_hours, expected', tests)
def test(hours_slept: list[int], target_hours: int, expected: int) -> None:
    assert sleep_debt(hours_slept, target_hours) == expected


if __name__ == '__main__':
    hours_slept, target_hours, expected = tests[4]
    print(sleep_debt(hours_slept, target_hours))
