# Daily Coding challenge #339 (2026-07-15) - freeCodeCamp.org
# Array Chunks
# Given an array and a chunk size, return the array split into sub-arrays of that size.
#
# - The last chunk may be smaller if the array doesn't divide evenly.
from collections.abc import Sequence
from itertools import batched

from pytest import mark


def chunk_array[T](arr: Sequence[T], size: int) -> list[list[T]]:
    if size <= 0:
        raise ValueError(f'size must be a positive integer, got {size}')
    return [list(chunk) for chunk in batched(arr, size)]


tests: list[tuple[list[int | str], int, list[list[int | str]]]] = [
    ([1, 2, 3, 4, 5, 6], 3, [[1, 2, 3], [4, 5, 6]]),
    (
        [1, 'two', 3, 'four', 5, 'six', 7, 'eight'],
        2,
        [[1, 'two'], [3, 'four'], [5, 'six'], [7, 'eight']],
    ),
    ([1, 2, 3, 4, 5], 3, [[1, 2, 3], [4, 5]]),
    (['a', 'b', 'c', 'd', 'e'], 1, [['a'], ['b'], ['c'], ['d'], ['e']]),
    ([1, 2, 3], 5, [[1, 2, 3]]),
]


@mark.parametrize('arr, size, expected', tests)
def test_chunk_array(
    arr: list[int | str], size: int, expected: list[list[int | str]]
) -> None:
    assert chunk_array(arr, size) == expected


if __name__ == '__main__':
    arr, size, expected = tests[4]
    print(chunk_array(arr, size))
