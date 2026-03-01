# Daily Coding challenge #58 (2025-10-07) - freeCodeCamp.org
# Space Week Day 4: Landing Spot
# In day four of Space Week, you are given a matrix of numbers (an array of arrays),
# representing potential landing spots for your rover. Find the safest landing spot
# based on the following rules:

# Each spot in the matrix will contain a number from 0-9, inclusive.
# Any 0 represents a potential landing spot.
# Any number other than 0 is too dangerous to land. The higher the number, the more
# dangerous.
# The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors,
# ignore diagonals) have the lowest total danger.
# Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
# Return the indices of the safest landing spot. There will always only be one safest
# spot.
# For instance, given:

# [
#   [1, 0],
#   [2, 0]
# ]
# Return [0, 1], the indices for the 0 in the first array.
from collections import namedtuple
from operator import attrgetter

from pytest import mark

LandingSpot = namedtuple('LandingSpot', ['row', 'col', 'total_danger'])

TOTAL_DANGER_GETTER = attrgetter('total_danger')


def find_landing_spot(matrix: list[list[int]]) -> list[int]:
    landing_spots = []

    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                total_danger = 0
                # Two separate loops:
                # for dr in [-1, 1]:
                #     # Calculate horizontal neighbor position
                #     neighbor_row = row + dr
                #     if 0 <= neighbor_row < rows:
                #         total_danger += matrix[neighbor_row][col]

                # for dc in [-1, 1]:
                #     # Calculate vertical neighbor position
                #     neighbor_col = col + dc
                #     # Check if neighbor is within bounds
                #     if 0 <= neighbor_col < cols:
                #         total_danger += matrix[row][neighbor_col]
                # Single loop:
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in directions:
                    neighbor_row, neighbor_col = row + dr, col + dc
                    if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                        total_danger += matrix[neighbor_row][neighbor_col]
                landing_spots.append(
                    LandingSpot(row=row, col=col, total_danger=total_danger)
                )
    print(landing_spots)

    best_landing_spot = min(landing_spots, key=TOTAL_DANGER_GETTER)

    return [best_landing_spot.row, best_landing_spot.col]


tests = [
    ([[1, 0], [2, 0]], [0, 1]),
    ([[9, 0, 3], [7, 0, 4], [8, 0, 5]], [1, 1]),
    ([[1, 2, 1], [0, 0, 2], [3, 0, 0]], [2, 2]),
    ([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]], [2, 1]),
]


@mark.parametrize('matrix, expected', tests)
def test_find_landing_spot(matrix: list[list[int]], expected: list[int]) -> None:
    assert find_landing_spot(matrix) == expected


if __name__ == '__main__':
    matrix, expected = tests[0]
    print(find_landing_spot(matrix))
