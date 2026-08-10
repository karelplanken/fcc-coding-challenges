# Daily Coding challenge #363 (2026-08-08) - freeCodeCamp.org
# Bucket Fill 2
# Given a 2D grid of single-letter color strings and a target color, return the minimum
# number of flood fill "clicks" needed to make the entire grid the target color.
#
# - Each click changes the clicked cell's color and the entire region of connected cells
#   of the same color with the target color.
# - Cells are connected horizontally and vertically (not diagonally).
from collections import deque

from pytest import mark

DELTAS = ((-1, 0), (0, 1), (1, 0), (0, -1))


def bucket_fill(grid: list[list[str]], target_color: str) -> int:
    """Returns the minimum number of clicks required to change the entire grid to
    the target color.

    Each click recolors a full connected region to the target color, so the answer is
    simply the count of connected regions (4-directionally adjacent, same original
    color) that are not already the target color.

    Depends on DELTAS for the four cardinal directions (up, down, left, right).

    Args:
        grid: A 2D list of single-letter color strings.
        target_color: The target color to fill the grid with.

    Returns:
        The minimum number of clicks required to make the entire grid the target color.
    """
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    clicks = 0

    for r0 in range(rows):
        for c0 in range(cols):
            if visited[r0][c0]:
                continue

            color = grid[r0][c0]
            visited[r0][c0] = True
            queue: deque[tuple[int, int]] = deque([(r0, c0)])

            while queue:
                r, c = queue.popleft()
                for dr, dc in DELTAS:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and not visited[nr][nc]
                        and grid[nr][nc] == color
                    ):
                        visited[nr][nc] = True
                        queue.append((nr, nc))

            if color != target_color:
                clicks += 1

    return clicks


tests: list[tuple[list[list[str]], str, int]] = [
    ([['R', 'R'], ['R', 'R']], 'G', 1),
    ([['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']], 'B', 0),
    ([['G', 'Y', 'Y'], ['G', 'Y', 'G'], ['Y', 'Y', 'G']], 'R', 3),
    (
        [
            ['G', 'G', 'P', 'Y'],
            ['O', 'P', 'P', 'P'],
            ['O', 'O', 'P', 'G'],
            ['G', 'O', 'O', 'G'],
        ],
        'P',
        5,
    ),
    (
        [
            ['G', 'G', 'C', 'C', 'O'],
            ['B', 'Y', 'B', 'Y', 'O'],
            ['B', 'J', 'O', 'J', 'B'],
            ['G', 'Y', 'Y', 'Y', 'B'],
            ['G', 'P', 'P', 'G', 'G'],
        ],
        'Y',
        12,
    ),
]


@mark.parametrize('grid, target_color, expected', tests)
def test_bucket_fill(grid: list[list[str]], target_color: str, expected: int) -> None:
    assert bucket_fill(grid, target_color) == expected


if __name__ == '__main__':
    grid, target_color, expected = tests[0]
    print(bucket_fill(grid, target_color))
