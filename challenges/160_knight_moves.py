# Daily Coding challenge #160 (2026-01-17) - freeCodeCamp.org
# Knight Moves
# Given the position of a knight on a chessboard, return the number of valid squares
# the knight can move to.

# A standard chessboard is 8x8, with columns labeled A through H (left to right) and
# rows labeled 1 through 8 (bottom to top). It looks like this:

# A8 B8 C8 D8 E8 F8 G8 H8
# A7 B7 C7 D7 E7 F7 G7 H7
# A6 B6 C6 D6 E6 F6 G6 H6
# A5 B5 C5 D5 E5 F5 G5 H5
# A4 B4 C4 D4 E4 F4 G4 H4
# A3 B3 C3 D3 E3 F3 G3 H3
# A2 B2 C2 D2 E2 F2 G2 H2
# A1 B1 C1 D1 E1 F1 G1 H1

# A knight moves in an "L" shape: two squares in one direction (horizontal or vertical),
# and one square in the perpendicular direction.

# This means a knight can move to up to eight possible positions, but fewer when near
# the edges of the board. For example, if a knight was at A1, it could only move to B3
# or C2.
from pytest import mark


def knight_moves(position: str) -> int:
    # Convert chess notation to 0-indexed coordinates conforming to matrix notation
    row, col = 8 - int(position[1]), ord(position[0]) - ord('A')

    # All 8 possible knight moves (L-shaped: 2+1 or 1+2)
    moves = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (2, -1), (-2, 1), (2, 1)]

    # Count available fields on board for the knight to move to:
    return sum(1 for dr, dc in moves if 0 <= row + dr < 8 and 0 <= col + dc < 8)


tests = [
    ('A1', 2),
    ('D4', 8),
    ('G6', 6),
    ('B8', 3),
    ('H3', 4),
]


@mark.parametrize('position, expected', tests)
def test_knight_moves(position: str, expected: int) -> None:
    assert knight_moves(position) == expected


if __name__ == '__main__':
    position, expected = tests[4]
    print(knight_moves(position))
