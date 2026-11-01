"""Daily Coding Challenge #58 (2025-10-07) - freeCodeCamp.org."""

# Space Week Day 4: Landing Spot
# In day four of Space Week, you are given a matrix of numbers (an array of arrays),
# representing potential landing spots for your rover. Find the safest landing spot
# based on the following rules:
#
# - Each spot in the matrix will contain a number from 0-9, inclusive.
# - Any 0 represents a potential landing spot.
# - Any number other than 0 is too dangerous to land. The higher the number, the more
#   dangerous.
# - The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors,
#   ignore diagonals) have the lowest total danger.
# - Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
# - Return the indices of the safest landing spot. There will always only be one safest
#   spot.
#
# For instance, given:
#
# js
# [
#   [1, 0],
#   [2, 0]
# ]
#
# Return [0, 1], the indices for the 0 in the first array.
from itertools import product

from pytest import mark

_DELTAS = ((-1, 0), (0, 1), (1, 0), (0, -1))


def find_landing_spot(matrix: list[list[int]]) -> list[int]:
    """Find the safest landing spot in a matrix of danger levels.

    The safest spot is the 0 cell whose orthogonal neighbours have the lowest
    total danger. Ties resolve to the first such cell in row-major order.

    Args:
        matrix: Rectangular grid of integers 0-9; 0 marks a landable cell.

    Returns:
        The [row, col] indices of the safest landing spot.

    Raises:
        ValueError: If the matrix is empty or contains no 0 cell.
    """
    if not matrix or not matrix[0]:
        msg = 'matrix must be a non-empty 2D list'
        raise ValueError(msg)

    rows, cols = len(matrix), len(matrix[0])

    def danger(rc: tuple[int, int]) -> int:
        r, c = rc
        return sum(
            matrix[r + dr][c + dc]
            for dr, dc in _DELTAS
            if 0 <= r + dr < rows and 0 <= c + dc < cols
        )

    zeros = ((r, c) for r, c in product(range(rows), range(cols)) if matrix[r][c] == 0)
    best = min(zeros, key=danger, default=None)

    if best is None:
        msg = 'matrix contains no 0 cell'
        raise ValueError(msg)

    row, col = best
    return [row, col]


tests = [
    ([[1, 0], [2, 0]], [0, 1]),
    ([[9, 0, 3], [7, 0, 4], [8, 0, 5]], [1, 1]),
    ([[1, 2, 1], [0, 0, 2], [3, 0, 0]], [2, 2]),
    ([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]], [2, 1]),
]


@mark.parametrize('matrix, expected', tests)
def test_find_landing_spot(matrix: list[list[int]], expected: list[int]) -> None:
    """Test find_landing_spot function."""
    assert find_landing_spot(matrix) == expected


if __name__ == '__main__':
    matrix, expected = tests[0]
    print(find_landing_spot(matrix))
