# Daily Coding challenge #87 (2025-11-05) - freeCodeCamp.org
# Matrix Builder
# Given two integers (a number of rows and a number of columns), return a matrix
# (an array of arrays) filled with zeros (0) of the given size.
# For example, given 2 and 3, return:
# [
#   [0, 0, 0],
#   [0, 0, 0]
# ]
from pytest import mark


def build_matrix(rows: int, cols: int) -> list[list[int]]:
    return [[0] * cols for _ in range(rows)]


tests = [
    (2, 3, [[0, 0, 0], [0, 0, 0]]),
    (3, 2, [[0, 0], [0, 0], [0, 0]]),
    (4, 3, [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]),
    (9, 1, [[0], [0], [0], [0], [0], [0], [0], [0], [0]]),
]


@mark.parametrize(('rows', 'cols', 'expected'), tests)
def test_build_matrix(rows: int, cols: int, expected: list[list[int]]) -> None:
    assert build_matrix(rows, cols) == expected


if __name__ == '__main__':
    rows, cols, expected = tests[0]
    print(build_matrix(rows, cols))
