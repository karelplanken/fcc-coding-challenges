# Daily Coding challenge #251 (2026-04-18) - freeCodeCamp.org
# Array Sum Finder
# Given an array of numbers and a target number, return the first subset of two or more
# numbers that adds up to the target.

# The "first" subset is the one whose elements have the lowest possible indices,
# prioritizing the earliest index first.
# Each number in the array may only be used once.
# If no valid subset exists, return "Sum not found".
# Return the matching numbers as an array in the order they appear in the original
# array.
from itertools import combinations

from pytest import mark


def find_sum(arr: list[int], target: int) -> list[int] | str:
    # combinations() yields index tuples in lexicographic order, therefore
    # the first match at each size is already the lowest-index combo for that size.
    # So collect one winner per size, then pick the overall best by comparing index
    # tuples.
    best = None
    for size in range(2, len(arr) + 1):  # +1 to include full-array subsets
        for indices in combinations(range(len(arr)), size):
            if sum(arr[i] for i in indices) == target:
                if best is None or indices < best:
                    best = indices
                break  # first hit at this size is the best for this size
    return [arr[i] for i in best] if best else 'Sum not found'


tests = [
    ([1, 2, 3], 6, [1, 2, 3]),
    ([1, 3, 5, 7], 6, [1, 5]),
    ([1, 2, 3, 4, 5], 5, [1, 4]),
    ([1, 2, 3, 4, 5], 6, [1, 2, 3]),
    ([-1, -2, 3, 4], 1, [-1, -2, 4]),
    ([3, 1, 4, 1, 5, 9, 2, 6], 10, [3, 1, 4, 2]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 20, [1, 2, 3, 5, 9]),
    ([7, 9, 4, 2, 5], 10, 'Sum not found'),
]


@mark.parametrize('arr, target, expected', tests)
def test(arr: list[int], target: int, expected: list[int] | str) -> None:
    assert find_sum(arr, target) == expected


if __name__ == '__main__':
    array, target, expected = tests[0]
    print(find_sum(array, target))
