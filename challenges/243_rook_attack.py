# Daily Coding challenge #243 (2026-04-10) - freeCodeCamp.org
# Rook Attack
# Given two strings for the location of two rooks on a chess board, determine if they
# can attack each other.

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
# So if they are on the same row or column, they can attack each other.
from pytest import mark


def rook_attack(rook1: str, rook2: str) -> bool:
    col1, row1 = rook1[0], rook1[1]
    col2, row2 = rook2[0], rook2[1]

    return col1 == col2 or row1 == row2


tests = [
    ('A1', 'A8', True),
    ('B4', 'F4', True),
    ('E3', 'D4', False),
    ('H7', 'F6', False),
]


@mark.parametrize('rook1, rook2, expected', tests)
def test_solution(rook1: str, rook2: str, expected: bool) -> None:
    assert rook_attack(rook1, rook2) == expected


if __name__ == '__main__':
    rook1, rook2, expected = tests[3]
    print(rook_attack(rook1, rook2))
