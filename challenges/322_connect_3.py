# Daily Coding challenge #322 (2026-06-28) - freeCodeCamp.org
# Connect 3
# Given a matrix of strings representing pieces on a game grid, determine if any player
# has three in a row.
#
# - Each cell contains `"R"`, `"Y"`, or `""` (empty string).
# - Three in a row means three consecutive non-empty cells of the same type
#   horizontally, vertically, or diagonally.
#
# Return:
#
# - A flat array with the winner and the coordinates of their three winning cells in the
#   format: `["R", [0,2], [1,3], [2,4]]`. Coordinates are returned top-to-bottom, then
#   left-to-right.
# - An empty array if there is no winner.
# from collections.abc import Generator
from itertools import product

from pytest import mark

# Direction-vector scan, as is is idiomatic for board-game problems and generalises
# more naturally to connect-4 or variable run-lengths.
DIRECTIONS = [(0, 1), (1, 0), (1, 1), (1, -1)]


def connect_three(matrix: list[list[str]]) -> list[str | list[int]]:
    rows, cols = len(matrix), len(matrix[0])
    n = 3
    for r, c in product(range(rows), range(cols)):
        if not (piece := matrix[r][c]):
            continue
        for dr, dc in DIRECTIONS:
            end_r, end_c = r + (n - 1) * dr, c + (n - 1) * dc
            if not (0 <= end_r < rows and 0 <= end_c < cols):
                continue
            coords = [[r + i * dr, c + i * dc] for i in range(n)]
            if all(matrix[nr][nc] == piece for nr, nc in coords):
                return [piece, *coords]
    return []


# # Original solution involving precomputing windows:
# def _windows(rows: int, cols: int, n: int = 3) -> Generator[list[list[int]]]:
#     if n <= cols:
#         for r, c in product(range(rows), range(cols - (n - 1))):
#             yield [[r, c + i] for i in range(n)]
#     if n <= rows:
#         for r, c in product(range(rows - (n - 1)), range(cols)):
#             yield [[r + i, c] for i in range(n)]
#     if n <= rows and n <= cols:
#         for r, c in product(range(rows - (n - 1)), range(cols - (n - 1))):
#             yield [[r + i, c + i] for i in range(n)]
#         for r, c in product(range(rows - (n - 1)), range(n - 1, cols)):
#             yield [[r + i, c - i] for i in range(n)]


# def connect_three(matrix: list[list[str]]) -> list[str | list[int]]:
#     rows, cols = len(matrix), len(matrix[0])
#     for window in _windows(rows, cols):
#         symbols = [matrix[r][c] for r, c in window]
#         if symbols[0] and len(set(symbols)) == 1:
#             return [symbols[0], *window]
#     return []


tests = [
    (
        [['', '', '', ''], ['', '', '', ''], ['', 'Y', '', ''], ['Y', 'R', 'R', 'R']],
        ['R', [3, 1], [3, 2], [3, 3]],
    ),
    (
        [
            ['', '', '', ''],
            ['', 'Y', 'Y', ''],
            ['', 'Y', 'R', 'R'],
            ['', 'Y', 'R', 'R'],
        ],
        ['Y', [1, 1], [2, 1], [3, 1]],
    ),
    (
        [
            ['', '', 'Y', 'R'],
            ['', 'Y', 'R', 'Y'],
            ['', 'R', 'Y', 'R'],
            ['', 'R', 'Y', 'R'],
        ],
        ['R', [0, 3], [1, 2], [2, 1]],
    ),
    (
        [
            ['', 'Y', '', ''],
            ['', 'Y', 'Y', ''],
            ['', 'R', 'R', 'Y'],
            ['R', 'R', 'Y', 'R'],
        ],
        ['Y', [0, 1], [1, 2], [2, 3]],
    ),
    (
        [
            ['Y', 'R', 'R', 'Y'],
            ['R', 'Y', 'Y', 'R'],
            ['Y', 'R', 'R', 'Y'],
            ['R', 'Y', 'Y', 'R'],
        ],
        [],
    ),
]


@mark.parametrize('matrix, expected', tests)
def test_connect_three(
    matrix: list[list[str]], expected: list[str | list[int]]
) -> None:
    assert connect_three(matrix) == expected


if __name__ == '__main__':
    matrix, expected = tests[4]
    print(connect_three(matrix))
