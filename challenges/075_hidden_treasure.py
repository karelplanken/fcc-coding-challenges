# Daily Coding challenge #75 (2025-10-24) - freeCodeCamp.org
# Hidden Treasure
# Given a 2D array representing a map of the ocean floor that includes a hidden
# treasure, and an array with the coordinates ([row, column]) for the next dive of
# your treasure search, return "Empty", "Found", or "Recovered" using the following
# rules:

# The given 2D array will contain exactly one unrecovered treasure, which will occupy
# multiple cells.
# Each cell in the 2D array will contain one of the following values:
# "-": No treasure.
# "O": A part of the treasure that has not been found.
# "X": A part of the treasure that has already been found.
# If the dive location has no treasure, return "Empty".
# If the dive location finds treasure, but at least one other part of the treasure
# remains unfound, return "Found".
# If the dive location finds the last unfound part of the treasure, return "Recovered".
# For example, given:
# [
#   [ "-", "X"],
#   [ "-", "X"],
#   [ "-", "O"]
# ]
# And [2, 1] for the coordinates of the dive location, return "Recovered" because the
# dive found the last unfound part of the treasure.
from collections import Counter

from pytest import mark


def dive(dive_map: list[list[str]], coordinates: list[int]) -> str:
    row, col = coordinates
    if dive_map[row][col] == '-':
        return 'Empty'

    if dive_map[row][col] == 'X':
        return 'Found'

    count = Counter(value for row in dive_map for value in row)

    return 'Recovered' if count['O'] == 1 else 'Found'


tests = [
    ([['-', 'X'], ['-', 'X'], ['-', 'O']], [2, 1], 'Recovered'),
    ([['-', 'X'], ['-', 'X'], ['-', 'O']], [2, 0], 'Empty'),
    ([['-', 'X'], ['-', 'O'], ['-', 'O']], [1, 1], 'Found'),
    ([['-', '-', '-'], ['X', 'O', 'X'], ['-', '-', '-']], [1, 2], 'Found'),
    ([['-', '-', '-'], ['-', '-', '-'], ['O', 'X', 'X']], [2, 0], 'Recovered'),
    ([['-', '-', '-'], ['-', '-', '-'], ['O', 'X', 'X']], [1, 2], 'Empty'),
]


@mark.parametrize('dive_map, coordinates, expected', tests)
def test_dive(dive_map: list[list[str]], coordinates: list[int], expected: str) -> None:
    assert dive(dive_map, coordinates) == expected


if __name__ == '__main__':
    dive_map, coordinates, expected = tests[0]
    print(dive(dive_map, coordinates))
