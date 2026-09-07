"""Daily Coding Challenge #27 (2025-09-06) - freeCodeCamp.org."""

# Matrix Rotate
# Given a matrix (an array of arrays), rotate the matrix 90 degrees clockwise and return
# it. For instance, given [[1, 2], [3, 4]], which looks like this:
#
# | 1 | 2 |
# |---|---|
# | 3 | 4 |
#
# You should return [[3, 1], [4, 2]], which looks like this:
#
# | 3 | 1 |
# |---|---|
# | 4 | 2 |
from pytest import mark


def rotate(matrix: list[list[int]]) -> list[list[int]]:
    """Rotate a matrix 90 degrees clockwise.

    Reversing the row order and then transposing (zip) is equivalent to a
    90-degree clockwise rotation: the last row becomes the first column,
    the second-to-last row becomes the second column, and so on.

    Args:
        matrix: A list of lists representing a matrix. Rows may be of any
            equal length; the matrix may be non-square.

    Returns:
        A new matrix representing the input rotated 90 degrees clockwise.
    """
    return [list(row) for row in zip(*reversed(matrix))]


tests = [
    ([[1]], [[1]]),
    ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    ([[0, 1, 0], [1, 0, 1], [0, 0, 0]], [[0, 1, 0], [0, 0, 1], [0, 1, 0]]),
]


@mark.parametrize('matrix, expected', tests)
def test_rotate(matrix: list[list[int]], expected: list[list[int]]) -> None:
    """Test rotate function."""
    assert rotate(matrix) == expected


if __name__ == '__main__':
    matrix, expected = tests[1]
    print(rotate(matrix))
