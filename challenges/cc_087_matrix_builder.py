"""Daily Coding Challenge #87 (2025-11-05) - freeCodeCamp.org."""

# Matrix Builder
# Given two integers (a number of rows and a number of columns), return a matrix (an
# array of arrays) filled with zeros (0) of the given size.
#
# For example, given 2 and 3, return:
#
# [
#   [0, 0, 0],
#   [0, 0, 0]
# ]
from pytest import mark


def build_matrix(rows: int, cols: int) -> list[list[int]]:
    """Return a matrix of the given size filled with zeros.

    Args:
        rows: The number of rows in the matrix.
        cols: The number of columns in the matrix.

    Returns:
        A list of ``rows`` independent lists, each holding ``cols`` zeros.

    Raises:
        ValueError: If ``rows`` or ``cols`` is negative.
    """
    if rows < 0 or cols < 0:
        msg = f'rows and cols must be non-negative, got rows={rows}, cols={cols}.'
        raise ValueError(msg)
    return [[0] * cols for _ in range(rows)]


tests = [
    (2, 3, [[0, 0, 0], [0, 0, 0]]),
    (3, 2, [[0, 0], [0, 0], [0, 0]]),
    (4, 3, [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]),
    (9, 1, [[0], [0], [0], [0], [0], [0], [0], [0], [0]]),
]


@mark.parametrize(('rows', 'cols', 'expected'), tests)
def test_build_matrix(rows: int, cols: int, expected: list[list[int]]) -> None:
    """Test build_matrix function."""
    assert build_matrix(rows, cols) == expected


if __name__ == '__main__':
    rows, cols, expected = tests[0]
    print(build_matrix(rows, cols))
