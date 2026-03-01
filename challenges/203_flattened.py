# Daily Coding challenge #203 (2026-03-01) - freeCodeCamp.org
# Flattened
# Given an array, determine if it is flat.

# An array is flat if none of its elements are arrays.
from typing import Any

from pytest import mark


def is_flat(arr: list[Any]) -> bool:
    return not any(isinstance(item, list) for item in arr)


tests: list[tuple[list[Any], bool]] = [
    ([1, 2, 3, 4], True),
    ([1, [2, 3], 4], False),
    ([1, 0, False, True, 'a', 'b'], True),
    (['a', [0], 'b', True], False),
    ([1, [2, [3, [4, [5]]]], 6], False),
]


@mark.parametrize('arr, expected', tests)
def test(arr: list[Any], expected: bool) -> None:
    assert is_flat(arr) == expected


if __name__ == '__main__':
    arr, expected = tests[0]
    print(is_flat(arr))
