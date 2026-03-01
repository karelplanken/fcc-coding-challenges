# Daily Coding challenge #158 (2026-01-15) - freeCodeCamp.org
# Array Swap
# Given an array with two values, return an array with the values swapped.

# For example, given ["A", "B"] return ["B", "A"].
from typing import Any

from pytest import mark


def array_swap(arr: list[Any]) -> list[Any]:
    return arr[::-1]


# # Explicit indexing (more verbose, same performance)
# def array_swap(arr: list[Any]) -> list[Any]:
#     return [arr[1], arr[0]]


# # Unpacking (elegant but slightly less clear for this use case)
# def array_swap(arr: list[Any]) -> list[Any]:
#     a, b = arr
#     return [b, a]


tests = [
    (['A', 'B'], ['B', 'A']),
    ([25, 20], [20, 25]),
    ([True, False], [False, True]),
    (['1', 1], [1, '1']),
]


@mark.parametrize('arr, expected', tests)
def test_array_swap(arr: list[Any], expected: list[Any]) -> None:
    assert array_swap(arr) == expected


if __name__ == '__main__':
    arr, expected = tests[0]
    print(array_swap(arr))