# Daily Coding challenge #195 (2026-02-21) - freeCodeCamp.org
# 2026 Winter Games Day 16: Curling
# Given a 5x5 matrix representing the "house" at the end of a curling round, determine
# which team scores and how many points they score.

# The layout:

# The center cell (index [2, 2]) is the "button".
# The 8 cells directly surrounding the button represent ring 1.
# And the 16 cells on the outer edge of the house represent ring 2.
# In the given matrix:

# "." represents an empty space.
# "R" represents a space with a red stone.
# "Y" represents a space with a yellow stone.
# Scoring rules:

# Only one team can score per round.
# The team with the stone closest to the button scores.
# The scoring team earns 1 point for each of their stones that is closer to the button
# than the opponent's closest stone.
# The lower the ring number, the closer to the center the stone is.
# If both teams' closest stone is the same distance from the center, no team scores.
# Return:

# A string in the format "team: number_of_points". e.g: "R: 2".
# or "No points awarded" if neither team scored any points.
# For example, given:

# [
#   [".", ".", "R", ".", "."],
#   [".", "R", ".", ".", "."],
#   ["Y", ".", ".", ".", "."],
#   [".", "R", ".", ".", "."],
#   [".", ".", ".", ".", "."]
# ]
# Return "R: 2". The two red stones in ring 1 are tied for the closest and are the only
# two stones closer than yellows closest.
# from collections import defaultdict
from pytest import mark


def score_curling(house: list[list[str]]) -> str:
    center = 2
    distances: dict[str, list[int]] = {'R': [], 'Y': []}

    for row_index, row in enumerate(house):
        for col_index, cell in enumerate(row):
            if cell not in distances:
                continue
            ring_distance = max(abs(row_index - center), abs(col_index - center))
            distances[cell].append(ring_distance)

    red_distances = distances['R']
    yellow_distances = distances['Y']

    if not red_distances and not yellow_distances:
        return 'No points awarded'

    red_closest = min(red_distances) if red_distances else float('inf')
    yellow_closest = min(yellow_distances) if yellow_distances else float('inf')

    if red_closest == yellow_closest:
        return 'No points awarded'

    if red_closest < yellow_closest:
        scoring_team = 'R'
        opponent_closest = yellow_closest
    else:
        scoring_team = 'Y'
        opponent_closest = red_closest

    points = sum(distance < opponent_closest for distance in distances[scoring_team])
    return f'{scoring_team}: {points}'


tests = [
    (
        [
            ['.', '.', 'R', '.', '.'],
            ['.', 'R', '.', '.', '.'],
            ['Y', '.', '.', '.', '.'],
            ['.', 'R', '.', '.', '.'],
            ['.', '.', '.', '.', '.'],
        ],
        'R: 2',
    ),
    (
        [
            ['.', '.', 'R', '.', '.'],
            ['.', '.', '.', '.', '.'],
            ['.', '.', 'Y', '.', 'R'],
            ['.', '.', 'Y', 'Y', '.'],
            ['.', 'Y', 'R', 'R', '.'],
        ],
        'Y: 3',
    ),
    (
        [
            ['.', 'R', 'Y', '.', '.'],
            ['Y', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.'],
            ['.', 'Y', 'R', 'Y', '.'],
            ['.', '.', 'R', 'R', '.'],
        ],
        'No points awarded',
    ),
    (
        [
            ['.', 'Y', 'Y', '.', '.'],
            ['Y', '.', '.', 'R', '.'],
            ['.', '.', 'R', '.', '.'],
            ['.', '.', 'R', 'R', '.'],
            ['.', 'Y', 'R', 'Y', '.'],
        ],
        'R: 4',
    ),
    (
        [
            ['Y', 'Y', 'Y', 'Y', 'Y'],
            ['Y', 'R', 'R', 'R', 'Y'],
            ['Y', 'R', 'Y', 'R', 'Y'],
            ['Y', 'R', 'R', 'R', 'Y'],
            ['Y', 'Y', 'Y', 'Y', 'Y'],
        ],
        'Y: 1',
    ),
    (
        [
            ['Y', 'R', 'Y', 'R', 'Y'],
            ['R', '.', '.', '.', 'R'],
            ['Y', '.', '.', '.', 'Y'],
            ['R', '.', '.', '.', 'R'],
            ['Y', '.', '.', 'R', 'Y'],
        ],
        'No points awarded',
    ),
]


@mark.parametrize('house, expected', tests)
def test_score_curling(house: list[list[str]], expected: str) -> None:
    assert score_curling(house) == expected


if __name__ == '__main__':
    house, exepected = tests[0]
    print(score_curling(house))
