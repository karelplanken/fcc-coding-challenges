# Daily Coding challenge #208 (2026-03-06) - freeCodeCamp.org
# Trail Traversal
# Given an array of strings representing your trail map, return a string of the moves
# needed to get to your goal.

# The given strings will contain the values:

# "C": Your current location
# "G": Your goal
# "T": Traversable parts of the trail
# "-": Untraversable parts of the map
# Return a string with the moves needed to follow the trail from your location to your
# goal where:

# "R" is a move right

# "D" is a move down

# "L" is a move left

# "U" is a move up

# There will always be a single continuous trail, without any branching, from your
# current location to your goal.

# Each trail location will have a maximum of two traversable locations touching it.

# For example, given:

# [
#   "-CT--",
#   "--T--",
#   "--TT-",
#   "---T-",
#   "---G-"
# ]
# Return "RDDRDD".
from dataclasses import dataclass
from types import MappingProxyType

from pytest import mark


@dataclass(frozen=True, slots=True)
class Coord:
    row: int
    col: int

    def __add__(self, other: 'Coord') -> 'Coord':
        return Coord(self.row + other.row, self.col + other.col)


MOVES: MappingProxyType[str, Coord] = MappingProxyType(
    {
        'U': Coord(-1, 0),
        'D': Coord(1, 0),
        'L': Coord(0, -1),
        'R': Coord(0, 1),
    }
)

REVERSE: MappingProxyType[str, str] = MappingProxyType(
    {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
)


def navigate_trail(trail_map: list[str]) -> str:
    rows, cols = len(trail_map), len(trail_map[0])

    pos = next(
        Coord(r, c)
        for r, row in enumerate(trail_map)
        for c, cell in enumerate(row)
        if cell == 'C'
    )

    def neighbours(p: Coord) -> list[tuple[str, Coord]]:
        return [
            (direction, nxt)
            for direction, delta in MOVES.items()
            if (nxt := p + delta) and 0 <= nxt.row < rows and 0 <= nxt.col < cols
        ]

    path: list[str] = []
    came_from: str | None = None

    while True:
        for direction, nxt in neighbours(pos):
            if direction == came_from:
                continue
            match trail_map[nxt.row][nxt.col]:
                case 'T':
                    path.append(direction)
                    came_from = REVERSE[direction]
                    pos = nxt
                    break
                case 'G':
                    return ''.join(path + [direction])


tests = [
    (['-CT--', '--T--', '--TT-', '---T-', '---G-'], 'RDDRDD'),
    (['-----', '--TTG', '--T--', '--T--', 'CTT--'], 'RRUUURR'),
    (['-C----', 'TT----', 'T-----', 'TTTTT-', '----G-'], 'DLDDRRRRD'),
    (['--------', '-CTTT---', '----T---', '---GT---', '--------'], 'RRRDDL'),
    (['TTTTTTT-', 'T-----T-', 'T-----T-', 'TTTT--TG', '---C----'], 'ULLLUUURRRRRRDDDR'),
]


@mark.parametrize('map, expected', tests)
def test(map: list[str], expected: str) -> None:
    assert navigate_trail(map) == expected


if __name__ == '__main__':
    map, expected = tests[4]
    print(navigate_trail(map))
