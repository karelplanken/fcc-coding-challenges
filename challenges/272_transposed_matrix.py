# Daily Coding challenge #272 (2026-05-09) - freeCodeCamp.org
# Transposed Matrix
# Given a matrix (an array of arrays), return the transposed version of it.
# To transpose the matrix, swap the rows and columns. E.g: a value at index [0, 1]
# should move to index [1, 0].
# For example, given:
# [
#   [1, 2, 3],
#   [4, 5, 6]
# ]
# Return:
# [
#   [1, 4],
#   [2, 5],
#   [3, 6]
# ]
from collections.abc import Sequence

from pytest import mark


def transpose[T](matrix: Sequence[Sequence[T]]) -> list[list[T]]:
    return [list(column) for column in zip(*matrix)]


tests: list[
    tuple[
        list[list[int] | list[str] | list[bool]],
        list[list[int] | list[str] | list[bool]],
    ]
] = [
    ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
    ([[1, 2], [3, 4], [5, 6]], [[1, 3, 5], [2, 4, 6]]),
    ([[1, 2], [3, 4], [5, 6], [7, 8]], [[1, 3, 5, 7], [2, 4, 6, 8]]),
    (
        [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l']],
        [['a', 'd', 'g', 'j'], ['b', 'e', 'h', 'k'], ['c', 'f', 'i', 'l']],
    ),
    (
        [
            [True, False, True, False],
            [False, True, False, True],
            [True, True, False, False],
            [False, False, True, True],
            [True, False, False, True],
        ],
        [
            [True, False, True, False, True],
            [False, True, True, False, False],
            [True, False, False, True, False],
            [False, True, False, True, True],
        ],
    ),
]


@mark.parametrize('matrix, expected', tests)
def test_transpose(
    matrix: list[list[int] | list[str] | list[bool]],
    expected: list[list[int] | list[str] | list[bool]],
) -> None:
    assert transpose(matrix) == expected


if __name__ == '__main__':
    matrix, expected = tests[4]
    print(transpose(matrix))
