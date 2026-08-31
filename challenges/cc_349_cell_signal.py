"""Daily Coding Challenge #349 (2026-07-25) - freeCodeCamp.org."""

# Cell Signal
# Given a grid containing three cell tower readings, determine the location of the
# phone.
#
# - Each cell in the grid is either 0 (no tower) or a positive integer representing the
#   number of cells to the phone, measured in a straight line: horizontal, vertical, or
#   diagonal.
# - Return the [row, col] of the cell that is the correct number of cells from all three
#   towers.
# - There is always exactly one solution.
from collections import Counter

from pytest import mark

DELTAS = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (-1, -1), (0, -1))
TOWERS = 3


def find_signal(grid: list[list[int]]) -> list[int]:
    """Determine the location of the phone based on the signal of three towers. The
    signal of each tower is proportional to the distance of the phone.

    Assumes that:
    - grid is a matrix containing ints >= 0 only
    - a solution exists
    - only one solution exists

    Args:
        grid: A matrix of tower signals.

    Returns:
        The location of the phone as [row, col].

    Raises:
        ValueError: If no solution is found to guarantee valid return.
    """
    rows, cols = len(grid), len(grid[0])
    candidate_coords: list[tuple[int, int]] = []

    def _get_coords(signal: int, row: int, col: int) -> list[tuple[int, int]]:
        deltas = ((dr * signal, dc * signal) for dr, dc in DELTAS)
        coords: list[tuple[int, int]] = []
        for dr, dc in deltas:
            if 0 <= (r := row + dr) < rows and 0 <= (c := col + dc) < cols:
                coords.append((r, c))
        return coords

    for row in range(rows):
        for col in range(cols):
            if (signal := grid[row][col]) > 0:
                candidate_coords.extend(_get_coords(signal, row, col))

    count = Counter(candidate_coords)

    for coord, freq in count.items():
        if freq == TOWERS:
            return [*coord]

    raise ValueError('no solution found')


tests = [
    ([[0, 0, 1], [0, 1, 0], [0, 0, 1]], [1, 2]),
    ([[0, 2, 0], [1, 0, 0], [0, 0, 1]], [2, 1]),
    ([[0, 0, 2, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 1]], [2, 2]),
    (
        [
            [0, 3, 0, 0, 0],
            [0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0],
            [4, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        [3, 4],
    ),
    (
        [
            [3, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 2],
        ],
        [3, 3],
    ),
]


@mark.parametrize('grid, expected', tests)
def test_find_signal(grid: list[list[int]], expected: list[int]) -> None:
    """Test find_signal function."""
    assert find_signal(grid) == expected


if __name__ == '__main__':
    grid, expected = tests[4]
    print(find_signal(grid))
