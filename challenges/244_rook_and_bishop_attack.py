# Daily Coding challenge #244 (2026-04-11) - freeCodeCamp.org
# Rook and Bishop Attack
# Given a string for the location of a rook on a chess board, and another for the
# location of a bishop, determine if one piece can attack another.

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
# Rooks can move as many squares as they want in a horizontal or vertical direction.
# Bishops can move as many squares as they want in any diagonal direction.
# One piece can attack another if it can move to the location of that piece.
# Return:

# "rook" if the rook can attack the bishop.
# "bishop" if the bishop can attack the rook.
# "neither" if neither piece can attack one another.
from types import MappingProxyType

from pytest import mark

COL_IDX = MappingProxyType({col: idx for idx, col in enumerate('ABCDEFGH', start=1)})


def rook_bishop_attack(rook: str, bishop: str) -> str:
    rook_col, rook_row = rook[0], rook[1]
    bishop_col, bishop_row = bishop[0], bishop[1]

    if rook_col == bishop_col or rook_row == bishop_row:
        return 'rook'

    col_diff = abs(COL_IDX[rook_col] - COL_IDX[bishop_col])
    row_diff = abs(int(rook_row) - int(bishop_row))

    return 'bishop' if col_diff == row_diff else 'neither'


tests = [
    ('A1', 'A5', 'rook'),
    ('C3', 'F6', 'bishop'),
    ('D4', 'D7', 'rook'),
    ('B7', 'H1', 'bishop'),
    ('B3', 'C5', 'neither'),
    ('G3', 'E8', 'neither'),
]


@mark.parametrize('rook, bishop, expected', tests)
def test_solution(rook: str, bishop: str, expected: str) -> None:
    assert rook_bishop_attack(rook, bishop) == expected


if __name__ == '__main__':
    rook, bishop, expected = tests[5]
    print(rook_bishop_attack(rook, bishop))
