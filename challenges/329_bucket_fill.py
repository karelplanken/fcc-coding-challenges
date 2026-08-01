# Daily Coding challenge #329 (2026-07-05) - freeCodeCamp.org
# Bucket Fill
# Given a 2D grid, a starting position (`[row, col]`), and a new value, replace the
# value at the starting position and all connected cells of the same value with the new
# value.
#
# - Cells are connected if they are adjacent horizontally or vertically (not
#   diagonally).
#
# Return the updated grid.
from collections import deque

from pytest import mark

DELTAS = ((0, -1), (0, 1), (-1, 0), (1, 0))


def bucket_fill(
    grid: list[list[str]], pos: list[int], new_value: str
) -> list[list[str]]:
    rows, cols = len(grid), len(grid[0])
    r0, c0 = pos
    old_value = grid[r0][c0]

    if old_value == new_value:
        return grid  # nothing to do; also avoids the infinite-loop trap

    grid[r0][c0] = new_value
    queue: deque[tuple[int, int]] = deque([(r0, c0)])

    while queue:
        r, c = queue.popleft()
        for dr, dc in DELTAS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == old_value:
                grid[nr][nc] = new_value
                queue.append((nr, nc))

    return grid


tests = [
    ([['R', 'G'], ['R', 'G']], [0, 1], 'B', [['R', 'B'], ['R', 'B']]),
    (
        [['Y', 'G', 'G'], ['Y', 'Y', 'Y'], ['B', 'Y', 'R']],
        [1, 2],
        'B',
        [['B', 'G', 'G'], ['B', 'B', 'B'], ['B', 'B', 'R']],
    ),
    (
        [['O', 'O', 'P'], ['P', 'O', 'O'], ['P', 'P', 'O']],
        [2, 0],
        'R',
        [['O', 'O', 'P'], ['R', 'O', 'O'], ['R', 'R', 'O']],
    ),
    (
        [
            ['T', 'T', 'R', 'T'],
            ['R', 'T', 'R', 'T'],
            ['R', 'T', 'R', 'T'],
            ['T', 'T', 'T', 'T'],
        ],
        [0, 3],
        'Y',
        [
            ['Y', 'Y', 'R', 'Y'],
            ['R', 'Y', 'R', 'Y'],
            ['R', 'Y', 'R', 'Y'],
            ['Y', 'Y', 'Y', 'Y'],
        ],
    ),
    (
        [
            ['G', 'B', 'G', 'B'],
            ['R', 'B', 'B', 'G'],
            ['B', 'G', 'B', 'R'],
            ['B', 'G', 'G', 'B'],
        ],
        [2, 2],
        'G',
        [
            ['G', 'G', 'G', 'B'],
            ['R', 'G', 'G', 'G'],
            ['B', 'G', 'G', 'R'],
            ['B', 'G', 'G', 'B'],
        ],
    ),
]


@mark.parametrize('grid, pos, new_value, expected', tests)
def test_bucket_fill(
    grid: list[list[str]], pos: list[int], new_value: str, expected: list[list[str]]
) -> None:
    assert bucket_fill(grid, pos, new_value) == expected


if __name__ == '__main__':
    grid, pos, new_value, expected = tests[4]
    print(bucket_fill(grid, pos, new_value))
