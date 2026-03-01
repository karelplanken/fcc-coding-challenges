# Daily Coding challenge #201 (2026-02-27) - freeCodeCamp.org
# Matrix Shift
# Given a matrix (array of arrays) of numbers and an integer, shift all values in the
# matrix by the given amount.

# A positive shift moves values to the right.
# A negative shift moves values to the left.
# Values should wrap:

# Treat the matrix as one continuous sequence of values. When a value moves past the end
# of a row, it continues at the beginning of the next row. When a value moves past the
# last position in the matrix, it wraps to the first position. The same applies in
# reverse when shifting left.
# For example, given:

# [
#   [1, 2, 3],
#   [4, 5, 6]
# ]
# with a shift of 1, move all the numbers to the right one:

# [
#   [6, 1, 2],
#   [3, 4, 5]
# ]
from pytest import mark


def shift_matrix(matrix: list[list[int]], shift: int) -> list[list[int]]:
    rows = len(matrix)
    cols = len(matrix[0])
    total = rows * cols

    # Flatten into a 1D list
    flat = [matrix[r][c] for r in range(rows) for c in range(cols)]

    # Rotate: positive shift moves values right, so we slice from the end
    shift = shift % total
    rotated = flat[-shift:] + flat[:-shift] if shift else flat

    # Reshape back into matrix
    return [rotated[r * cols : (r + 1) * cols] for r in range(rows)]



tests = [
    ([[1, 2, 3], [4, 5, 6]], 1, [[6, 1, 2], [3, 4, 5]]),
    ([[1, 2, 3], [4, 5, 6]], -1, [[2, 3, 4], [5, 6, 1]]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5, [[5, 6, 7], [8, 9, 1], [2, 3, 4]]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -6, [[7, 8, 9], [1, 2, 3], [4, 5, 6]]),
    (
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
        7,
        [[10, 11, 12, 13], [14, 15, 16, 1], [2, 3, 4, 5], [6, 7, 8, 9]],
    ),
    (
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
        -54,
        [[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 1, 2], [3, 4, 5, 6]],
    ),
]


@mark.parametrize('matrix, shift, expected', tests)
def test(matrix: list[list[int]], shift: int, expected: list[list[int]]) -> None:
    assert shift_matrix(matrix, shift) == expected


if __name__ == '__main__':
    matrix, shift, expected = tests[0]
    print(shift_matrix(matrix, shift))
    # shift_matrix(matrix, shift)
