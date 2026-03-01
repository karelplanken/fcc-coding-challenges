# Daily Coding challenge #132 (2025-12-20) - freeCodeCamp.org
# Purge Most Frequent
# Given an array of values, remove all occurrences of the most frequently occurring
# element and return the resulting array.

# If multiple values are tied for most frequent, remove all of them.
# Do not change any of the other elements or their order.
from collections import Counter
from typing import Any

from pytest import mark


def purge_most_frequent(arr: list[Any]) -> list[Any]:
    if not arr:
        return []

    count = Counter(arr)
    max_freq = max(count.values())

    return [item for item in arr if count[item] != max_freq]


tests = [
    ([1, 2, 2, 3], [1, 3]),
    (
        ['a', 'b', 'd', 'b', 'c', 'd', 'c', 'd', 'c', 'd'],
        ['a', 'b', 'b', 'c', 'c', 'c'],
    ),
    (
        ['red', 'blue', 'green', 'red', 'blue', 'green', 'blue'],
        ['red', 'green', 'red', 'green'],
    ),
    ([5, 5, 5, 5], []),
]


@mark.parametrize('arr, expected', tests)
def test_purge_most_frequent(arr: list[Any], expected: list[Any]) -> None:
    assert purge_most_frequent(arr) == expected


if __name__ == '__main__':
    arr, expected = tests[0]
    # print(purge_most_frequent(arr))
    print(purge_most_frequent([1, 2, 2, 2, 3, 4, 5, 5, 5]))
