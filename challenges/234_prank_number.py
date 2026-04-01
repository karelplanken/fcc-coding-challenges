# Daily Coding challenge #234 (2026-04-01) - freeCodeCamp.org
# Prank Number
# Given an array of numbers where all but one number follow a pattern, return a new
# array with the one number that doesn't follow the pattern fixed.

# The pattern will be one of:

# The numbers increase from one to the next by a fixed amount (addition).
# The numbers decrease from one to the next by a fixed amount (subtraction).
# For example, given [2, 4, 7, 8, 10] return [2, 4, 6, 8, 10].
from collections import Counter
from itertools import pairwise

from pytest import mark


def fix_prank_number(arr: list[int]) -> list[int]:
    diffs = [b - a for a, b in pairwise(arr)]
    increment, _ = Counter(diffs).most_common(n=1)[0]
    anchor = next(i for i, diff in enumerate(diffs) if diff == increment)

    return [arr[anchor] + (i - anchor) * increment for i in range(len(arr))]


tests = [
    ([2, 4, 7, 8, 10], [2, 4, 6, 8, 10]),
    ([10, 10, 8, 7, 6], [10, 9, 8, 7, 6]),
    ([12, 24, 36, 48, 61, 72, 84, 96], [12, 24, 36, 48, 60, 72, 84, 96]),
    ([4, 1, -2, -5, -8, -5], [4, 1, -2, -5, -8, -11]),
    ([0, 100, 200, 300, 150, 500], [0, 100, 200, 300, 400, 500]),
    ([400, 425, 400, 375, 350, 325, 300], [450, 425, 400, 375, 350, 325, 300]),
    ([-5, 5, 10, 15, 20], [0, 5, 10, 15, 20]),
]


@mark.parametrize('arr, expected', tests)
def test_solution(arr: list[int], expected: list[int]) -> None:
    assert fix_prank_number(arr) == expected


if __name__ == '__main__':
    arr, expected = tests[0]
    print(fix_prank_number(arr))
