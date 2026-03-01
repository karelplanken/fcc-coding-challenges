# Daily Coding challenge #121 (2025-12-09) - freeCodeCamp.org
# Most Frequent
# Given an array of elements, return the element that appears most frequently.

# There will always be a single most frequent element.
from collections import Counter
from typing import TypeVar

from pytest import mark

T = TypeVar('T')

# def most_frequent(arr: list[T]) -> T:
#     count = Counter(arr)
#     return max(count, key=count.get)  # type: ignore[arg-type]


# def most_frequent(arr: list[T]) -> T:
#     count = Counter(arr)
#     most_common_element, _ = count.most_common(1)[0]
#     return most_common_element


def most_frequent(arr: list[T]) -> T:
    return Counter(arr).most_common(1)[0][0]


# def most_frequent(arr: list[T]) -> T:
#     count = Counter(arr)
#     (most_common_element, _), *_ = count.most_common(1)
#     return most_common_element


tests = [
    (['a', 'b', 'a', 'c'], 'a'),
    ([2, 3, 5, 2, 6, 3, 2, 7, 2, 9], 2),
    ([True, False, 'False', 'True', False], False),
    ([40, 20, 70, 30, 10, 40, 10, 50, 40, 60], 40),
]


@mark.parametrize('arr,expected', tests)
def test_most_frequent(arr: list[T], expected: T) -> None:
    assert most_frequent(arr) == expected


if __name__ == '__main__':
    arr, expected = tests[1]
    print(most_frequent(arr))
