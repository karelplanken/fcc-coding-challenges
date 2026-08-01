# Daily Coding challenge #356 (2026-08-01) - freeCodeCamp.org
# Magic Square Solver
# Given a 3x3 grid with one missing number (represented as 0), return the missing number
# that completes the magic square, or "impossible" if no valid number exists.
#
# A magic square is a grid where every row, column, and diagonal adds up to the same
# number.
from typing import NamedTuple

from pytest import mark


class HasNoSolution(Exception):
    """Raise this exception when no solution exist for the given grid"""


ROWS = 3
COLS = 3


class Node(NamedTuple):
    row: int
    col: int


AXES: list[list[Node]] = [
    # Rows
    *[[Node(r, c) for c in range(COLS)] for r in range(ROWS)],
    # Columns
    *[[Node(r, c) for r in range(ROWS)] for c in range(COLS)],
    # Diagonal
    [Node(r, c) for r, c in zip(range(ROWS), range(COLS))],
    # Antidiagonal
    [Node(r, c) for r, c in zip(reversed(range(ROWS)), range(COLS))],
]


def get_missing_node(grid: list[list[int]]) -> Node:
    missing_node_candidates = {
        node for nodes in AXES for node in nodes if grid[node.row][node.col] == 0
    }

    candidate_count = len(missing_node_candidates)
    if candidate_count != 1:
        raise ValueError(
            f"Grid must contain exactly one '0' node, found {candidate_count}"
        )

    return missing_node_candidates.pop()


def get_magic_number(grid: list[list[int]], missing_node: Node) -> int:
    sums: list[int] = []

    for nodes in AXES:
        if missing_node not in nodes:
            sums.append(sum(grid[node.row][node.col] for node in nodes))

    if len(set(sums)) != 1:
        raise HasNoSolution('Grid rows and columns do not add up to the same number')

    return sums.pop()


def get_incomplete_axes(missing_node: Node) -> list[list[Node]]:
    incomplete_axes: list[list[Node]] = []

    for nodes in AXES:
        if missing_node in nodes:
            incomplete_axes.append(nodes)

    return incomplete_axes


def get_missing_number(
    grid: list[list[int]], incomplete_axes: list[list[Node]], magic_number: int
) -> int:
    candidates: list[int] = []

    for nodes in incomplete_axes:
        candidates.append(
            magic_number - sum(grid[node.row][node.col] for node in nodes)
        )

    if len(set(candidates)) != 1:
        raise HasNoSolution('No single number satisfies summing to the magic number')

    return candidates.pop()


def solve_magic_square(grid: list[list[int]]) -> int | str:
    try:
        missing_node = get_missing_node(grid)
    except ValueError as error:
        print(error)
        return 'impossible'

    try:
        magic_number = get_magic_number(grid, missing_node)
    except HasNoSolution as error:
        print(error)
        return 'impossible'

    incomplete_axes = get_incomplete_axes(missing_node)

    try:
        missing_number = get_missing_number(grid, incomplete_axes, magic_number)
    except HasNoSolution as error:
        print(error)
        return 'impossible'

    return missing_number


tests: list[tuple[list[list[int]], int | str]] = [
    ([[2, 7, 6], [9, 0, 1], [4, 3, 8]], 5),
    ([[0, 14, 12], [18, 10, 2], [8, 6, 16]], 4),
    ([[12, 17, 16], [19, 0, 10], [14, 13, 18]], 'impossible'),
    ([[15, 35, 31], [43, 27, 11], [23, 19, 0]], 39),
    ([[26, 41, 14], [47, 35, 0], [32, 29, 44]], 'impossible'),
    # Added test cases
    ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 'impossible'),
    ([[2, 3, 5], [4, 1, 5], [4, 6, 0]], 'impossible'),
    ([[5, 2, 8], [7, 4, 4], [3, 9, 0]], 'impossible'),
]


@mark.parametrize('grid, expected', tests)
def test_solve_magic_square(grid: list[list[int]], expected: int | str) -> None:
    assert solve_magic_square(grid) == expected


if __name__ == '__main__':
    grid, expected = tests[5]
    print(solve_magic_square(grid))
