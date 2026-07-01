# Daily Coding challenge #307 (2026-06-13) - freeCodeCamp.org
# Zoning Regulations
# Given a 2D grid (array of arrays) representing a city's building layout, return the
# coordinates of all buildings that are violating zoning rules.

# Each cell in the grid contains one of the labels from the table below. A building is
# in violation if any of its (up to) 4 neighbors, horizontal or vertical, are a type it
# cannot be adjacent to.

# Label	Type	            Cannot be adjacent to
# "i"	industrial	        "R", "I"
# "A"	Agricultural	    "C"
# "R"	Residential	        "i", "C"
# "I"	Institutional	    "i"
# "C"	Commercial	        "R", "A"
# "" (empty string)	undeveloped	no restrictions
# Return the coordinates of all violating cells as an array of [row, col] pairs, in any
# order. If no violations exist, return an empty array.
from dataclasses import dataclass, field
from itertools import product
from types import MappingProxyType

from pytest import mark


@dataclass(frozen=True)
class Zone:
    label: str
    abbreviation: str
    excluded_zones: frozenset[str] = field(default_factory=frozenset)


ZONES = [
    Zone('industrial', 'i', frozenset({'R', 'I'})),
    Zone('Agricultural', 'A', frozenset({'C'})),
    Zone('Residential', 'R', frozenset({'i', 'C'})),
    Zone('Institutional', 'I', frozenset({'i'})),
    Zone('Commercial', 'C', frozenset({'R', 'A'})),
    Zone('undeveloped', ''),
]

EXCLUDED_NEIGHBORS = MappingProxyType({
    zone.abbreviation: zone.excluded_zones for zone in ZONES
})
DELTAS = ((-1, 0), (1, 0), (0, -1), (0, 1))


def get_zone_violations(grid: list[list[str]]) -> list[list[int]]:
    rows, cols = len(grid), len(grid[0])

    def neighbor_labels(row: int, col: int) -> set[str]:
        return {
            grid[row + dr][col + dc]
            for dr, dc in DELTAS
            if 0 <= row + dr < rows and 0 <= col + dc < cols
        }

    return [
        [row, col]
        for row, col in product(range(rows), range(cols))
        if (excluded := EXCLUDED_NEIGHBORS[grid[row][col]])
        and neighbor_labels(row, col) & excluded
    ]


tests = [
    ([['R', 'C'], ['', 'C']], [[0, 0], [0, 1]]),
    ([['', 'i'], ['', 'R'], ['R', 'I']], [[0, 1], [1, 1]]),
    ([['A', 'i', 'C'], ['A', '', 'C'], ['R', 'R', 'I']], []),
    (
        [['R', 'R', 'C', 'R', 'R'], ['R', 'I', 'C', '', 'A'], ['R', 'R', '', 'i', 'A']],
        [[0, 1], [0, 2], [0, 3]],
    ),
    (
        [
            ['R', 'A', 'A', '', 'i', 'i'],
            ['R', 'I', '', 'C', 'i', 'i'],
            ['R', '', 'C', 'C', 'A', 'A'],
            ['R', 'R', 'C', 'I', 'R', 'R'],
        ],
        [[2, 3], [2, 4], [3, 1], [3, 2]],
    ),
]


@mark.parametrize('grid, expected', tests)
def test_get_zone_violations(grid: list[list[str]], expected: list[list[int]]) -> None:
    assert get_zone_violations(grid) == expected


if __name__ == '__main__':
    grid, expected = tests[2]
    print(get_zone_violations(grid))
