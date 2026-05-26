# Daily Coding challenge #289 (2026-05-26) - freeCodeCamp.org
# Sum of Differences
# Given an array of numbers, return the sum of the differences between each number and
# the one that follows it.

# For example, given [1, 3, 4], return 3 (2 + 1).
from collections.abc import Sequence
from itertools import pairwise

from pytest import mark


def sum_of_differences(arr: Sequence[int | float]) -> int | float:
    return sum(b - a for a, b in pairwise(arr))
    # More efficient and simpler solution:
    # return arr[-1] - arr[0]


tests = [
    ([1, 3, 4], 3),
    ([5, -3, 3, 9, 10], 5),
    ([9, 6, 15, -20, 33, 14, 25, 16, -7], -16),
    ([50, 102, -46, 82, -49, 29, 71, 902, -237, 111, -61, 75], 25),
]


@mark.parametrize('arr, expected', tests)
def test_sum_of_differences(arr: Sequence[int | float], expected: int | float) -> None:
    assert sum_of_differences(arr) == expected


if __name__ == '__main__':
    arr, expected = tests[3]
    print(sum_of_differences(arr))
