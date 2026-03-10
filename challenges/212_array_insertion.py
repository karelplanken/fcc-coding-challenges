# Daily Coding challenge #212 (2026-03-10) - freeCodeCamp.org
# Array Insertion
# Given an array, a value to insert into the array, and an index to insert the value at,
# return a new array with the value inserted at the specified index.
from collections.abc import Sequence

from pytest import mark

type Row = tuple[list[int | str], int | str, int, list[int | str]]


def insert_into_array(
    arr: Sequence[int | str], value: int | str, index: int
) -> list[int | str]:
    new_arr = list(arr)
    new_arr.insert(index, value)
    return new_arr


tests: list[Row] = [
    ([2, 4, 8, 10], 6, 2, [2, 4, 6, 8, 10]),
    (['the', 'quick', 'fox'], 'brown', 2, ['the', 'quick', 'brown', 'fox']),
    ([], 0, 0, [0]),
    ([0, 1, 1, 2, 3, 8, 13], 5, 5, [0, 1, 1, 2, 3, 5, 8, 13]),
]


@mark.parametrize('arr, value, index, expected', tests)
def test_insert_into_array(
    arr: list[int | str], value: int | str, index: int, expected: list[int | str]
) -> None:
    assert insert_into_array(arr, value, index) == expected


if __name__ == '__main__':
    arr, value, index, expected = tests[0]
    print(insert_into_array(arr, value, index))
