# Daily Coding challenge #173 (2026-01-30) - freeCodeCamp.org
# Valid Pawn Moves
# Given the position of one of your pawns on a chessboard, return an array of all the
# valid squares it can move to in ascending order.

# A standard chessboard is 8x8, with columns labeled A through H (left to right) and
# rows labeled 1 through 8 (bottom to top). It looks like this:

# A8	B8	C8	D8	E8	F8	G8	H8
# A7	B7	C7	D7	E7	F7	G7	H7
# A6	B6	C6	D6	E6	F6	G6	H6
# A5	B5	C5	D5	E5	F5	G5	H5
# A4	B4	C4	D4	E4	F4	G4	H4
# A3	B3	C3	D3	E3	F3	G3	H3
# A2	B2	C2	D2	E2	F2	G2	H2
# A1	B1	C1	D1	E1	F1	G1	H1
# For this challenge:

# You are the player on the bottom of the board.
# Pawns can only move one square "up".
# Unless the pawn is in the starting row (row 2), then it can move one or two squares
# up.
# For example, given "D4", return ["D5"], the only square your pawn can move to. Given
# "B2", return ["B3", "B4"], because it's on the starting row and needs to be in
# ascending order.
from pytest import mark


def find_pawn_moves(position: str) -> list[str]:
    col, row = position[0], int(position[1])

    if row == 2:  # Starting row - can move 1 or 2 squares
        return [f'{col}3', f'{col}4']

    # Regular move - advance 1 square
    return [f'{col}{row + 1}']


tests = [
    ('D4', ['D5']),
    ('B2', ['B3', 'B4']),
    ('A7', ['A8']),
    ('G2', ['G3', 'G4']),
    ('E3', ['E4']),
]


@mark.parametrize('position, expected', tests)
def test_find_pawn_moves(position: str, expected: list[str]) -> None:
    assert find_pawn_moves(position) == expected


if __name__ == '__main__':
    position, expected = tests[0]
    print(find_pawn_moves(position))
