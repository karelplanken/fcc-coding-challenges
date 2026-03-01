# Daily Coding challenge #199 (2026-02-25) - freeCodeCamp.org
# Sequential Difference
# Given an array of numbers, return a new array containing the value needed to get from
# each number to the next number.

# For the last number, use 0 since there is no next number.
# For example, given [1, 2, 4, 7], return [1, 2, 3, 0].
from itertools import pairwise

from pytest import mark


def find_differences(arr: list[int]) -> list[int]:
    return [b - a for a, b in pairwise(arr)] + [0]


tests = [
    ([1, 2, 4, 7], [1, 2, 3, 0]),
    ([10, 15, 19, 22, 24, 25], [5, 4, 3, 2, 1, 0]),
    ([25, 20, 16, 13, 11, 10], [-5, -4, -3, -2, -1, 0]),
    ([0, 1, 2, 2, 3, 3, 4, 5], [1, 1, 0, 1, 0, 1, 1, 0]),
    (
        [1, 2, 5, 12, 34, -15, -1, 41, 113, -222, -99, -40, 10, -18, -6, -2, -1],
        [1, 3, 7, 22, -49, 14, 42, 72, -335, 123, 59, 50, -28, 12, 4, 1, 0],
    ),
]


@mark.parametrize('arr, expected', tests)
def test(arr: list[int], expected: list[int]) -> None:
    assert find_differences(arr) == expected


if __name__ == '__main__':
    arr, expected = tests[0]
    print(arr)
    print(find_differences(arr))
    print(arr)
