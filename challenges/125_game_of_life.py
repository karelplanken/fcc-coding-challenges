# Daily Coding challenge #125 (2025-12-13) - freeCodeCamp.org
# Game of Life
# Given a matrix (array of arrays) representing the current state in Conway's Game of
# Life, return the next state of the matrix using these rules:

# Each cell is either 1 (alive) or 0 (dead).
# A cell's neighbors are the up to eight surrounding cells (vertically, horizontally,
# and diagonally).
# Cells on the edges have fewer than eight neighbors.
# Rules for updating each cell:

# Any live cell with fewer than two live neighbors dies (underpopulation).
# Any live cell with two or three live neighbors lives on.
# Any live cell with more than three live neighbors dies (overpopulation).
# Any dead cell with exactly three live neighbors becomes alive (reproduction).
# For example, given:

# [
#   [0, 1, 0],
#   [0, 1, 1],
#   [1, 1, 0]
# ]
# return:

# [
#   [0, 1, 1],
#   [0, 0, 1],
#   [1, 1, 1]
# ]
# Each cell updates according to the number of live neighbors. For instance, [0][0]
# stays dead (2 live neighbors), [0][1] stays alive (2 live neighbors), [0][2] dies
# (3 live neighbors), and so on.
from pytest import mark


def live_or_die(current_state: int, live_neighbors: int) -> int:
    if current_state == 1:
        return 1 if 2 <= live_neighbors <= 3 else 0
    else:
        return 1 if live_neighbors == 3 else 0


def game_of_life(grid: list[list[int]]) -> list[list[int]]:
    rows = len(grid)
    cols = len(grid[0])

    next_state_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            # Count live neighbors by checking all 8 possible directions
            live_neighbors = 0

            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    # Skip the cell itself
                    if dr == 0 and dc == 0:
                        continue

                    # Calculate neighbor position
                    neighbor_row = row + dr
                    neighbor_col = col + dc

                    # Check if neighbor is within bounds
                    if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                        live_neighbors += grid[neighbor_row][neighbor_col]

            next_state_matrix[row][col] = live_or_die(grid[row][col], live_neighbors)

    return next_state_matrix


tests = [
    ([[0, 1, 0], [0, 1, 1], [1, 1, 0]], [[0, 1, 1], [0, 0, 1], [1, 1, 1]]),
    (
        [[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]],
        [[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 1, 1]],
    ),
    ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
    (
        [[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]],
        [[1, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]],
    ),
]


@mark.parametrize('grid, expected', tests)
def test_game_of_life(grid: list[list[int]], expected: list[list[int]]) -> None:
    assert game_of_life(grid) == expected


if __name__ == '__main__':
    grid, expected = tests[0]
    print(game_of_life(grid))
