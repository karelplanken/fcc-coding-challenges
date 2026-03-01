# Daily Coding challenge #130 (2025-12-18) - freeCodeCamp.org
# Checkerboard
# Given an array with two numbers, the first being the number of rows and the second
# being the number of columns, return a matrix (an array of arrays) filled with "X"
# and "O" characters of the given size.

# The characters should alternate like a checkerboard.
# The top-left cell must always be "X".
# For example, given [3, 3], return:

# [
#   ["X", "O", "X"],
#   ["O", "X", "O"],
#   ["X", "O", "X"]
# ]
from typing import Any

from pytest import mark


def create_board(dimensions: list[int]) -> list[Any]:
    rows, cols = dimensions
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append('X' if (i + j) % 2 == 0 else 'O')
        board.append(row)
    return board


tests = [
    ([3, 3], [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]),
    ([6, 1], [['X'], ['O'], ['X'], ['O'], ['X'], ['O']]),
    (
        [2, 10],
        [
            ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'],
            ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'],
        ],
    ),
    (
        [5, 4],
        [
            ['X', 'O', 'X', 'O'],
            ['O', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'O'],
            ['O', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'O'],
        ],
    ),
]


@mark.parametrize('dimensions, expected', tests)
def test_create_board(dimensions: list[int], expected: list[Any]) -> None:
    assert create_board(dimensions) == expected


if __name__ == '__main__':
    dimensions, expected = tests[3]
    print(create_board(dimensions))
