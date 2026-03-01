# Daily Coding challenge #117 (2025-12-05) - freeCodeCamp.org
# Symmetric Difference
# Given two arrays, return a new array containing the symmetric difference of them.

# The symmetric difference between two sets is the set of values that appear in either
# set, but not both. Return the values in the order they first appear in the input
# arrays.
from typing import Any

from pytest import mark


def difference(arr1: list[Any], arr2: list[Any]) -> list[Any]:
    set1, set2 = set(arr1), set(arr2)
    # return list(set1.symmetric_difference(set2))  # Doesn't preserve order
    return [item for item in arr1 if item not in set2] + [
        item for item in arr2 if item not in set1
    ]


# def difference(arr1: list[Any], arr2: list[Any]) -> list[Any]:
#     return [
#         *[item for item in arr1 if item not in arr2],
#         *[item for item in arr2 if item not in arr1],
#     ]


tests = [
    ([1, 2, 3], [3, 4, 5], [1, 2, 4, 5]),
    (['a', 'b'], ['c', 'b'], ['a', 'c']),
    ([1, 'a', 2], [2, 'b', 'a'], [1, 'b']),
    ([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 4, 6, 8]),
]


@mark.parametrize('arr1,arr2,expected', tests)
def test_difference(arr1: list[Any], arr2: list[Any], expected: list[Any]) -> None:
    assert difference(arr1, arr2) == expected


if __name__ == '__main__':
    arr1, arr2, expected = tests[0]
    print(difference(arr1, arr2))
