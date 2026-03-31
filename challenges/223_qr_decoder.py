# Daily Coding challenge #223 (2026-03-21) - freeCodeCamp.org
# QR Decoder
# Given a 6x6 matrix (array of arrays), representing a QR code, return the string of
# binary data in the code.

# The QR code may be given in any rotation of 90 degree increments.
# A correctly oriented code has a 2x2 group of 1's (orientation markers) in the
# bottom-left, top-left, and top-right corners.
# The three 2x2 orientation markers are not part of the binary data.
# The binary data is read left-to-right, top-to-bottom (like a book) when the QR code
# is correctly oriented.
# A code will always have exactly one valid orientation.
# For example, given:

# [
#   "110011",
#   "110011",
#   "000000",
#   "000000",
#   "110000",
#   "110001"
# ]
# or given the same code with a different orientation:

# [
#   "110011",
#   "110011",
#   "000000",
#   "000000",
#   "000011",
#   "100011"
# ]
# Return "000000000000000000000001", all the binary data excluding the three 2x2
# orientation markers.
from types import MappingProxyType

from pytest import mark

# Four ways of positioning a square
# 1
# TL TR
# BL
# Required rotation in deg for TL, TR, BL is 0
# 2
# TL TR
#    BR
# Required rotation in deg for TL, TR, BR is -90
# 3
#    TR
# BL BR
# Required rotation in deg for TR, BR, BL is 180
# 4
# TL
# BL BR
# Required rotation in deg for TL, BR, BL is 90

MARKER_CELLS = MappingProxyType(
    {
        'TL': frozenset([(0, 0), (0, 1), (1, 0), (1, 1)]),
        'TR': frozenset([(0, 4), (0, 5), (1, 4), (1, 5)]),
        'BL': frozenset([(4, 0), (4, 1), (5, 0), (5, 1)]),
        'BR': frozenset([(4, 4), (4, 5), (5, 4), (5, 5)]),
    }
)

ALL_MARKER_CELLS = frozenset().union(
    MARKER_CELLS['TL'],
    MARKER_CELLS['TR'],
    MARKER_CELLS['BL']
)


def rotate_0(matrix: list[str]) -> list[list[str]]:
    return [list(row) for row in matrix]


def rotate_90(matrix: list[str]) -> list[list[str]]:
    return [list(reversed(col)) for col in zip(*matrix)]


def rotate_180(matrix: list[str]) -> list[list[str]]:
    return [list(reversed(row)) for row in reversed(matrix)]


def rotate_270(matrix: list[str]) -> list[list[str]]:
    return [list(col) for col in reversed(list(zip(*matrix)))]


# Missing corner → rotation needed to fix orientation
MISSING_TO_ROTATE = MappingProxyType(
    {
        'BR': rotate_0,
        'TR': rotate_90,
        'TL': rotate_180,
        'BL': rotate_270,
    }
)


def find_missing_corner(qr_code: list[str]) -> str:
    return next(
        corner
        for corner, cells in MARKER_CELLS.items()
        if not all(qr_code[r][c] == '1' for r, c in cells)
    )


def decode_qr(qr_code: list[str]) -> str:
    missing_corner = find_missing_corner(qr_code)
    matrix = MISSING_TO_ROTATE[missing_corner](qr_code)
    return ''.join(
        matrix[r][c]
        for r in range(6)
        for c in range(6)
        if (r, c) not in ALL_MARKER_CELLS
    )


tests = [
    (
        ['110011', '110011', '000000', '000000', '110000', '110001'],
        '000000000000000000000001',
    ),
    (
        ['100011', '000011', '000000', '000000', '110011', '110011'],
        '000000000000000000000001',
    ),
    (
        ['110011', '111111', '010000', '110000', '110011', '110100'],
        '001101000011000000110100',
    ),
    (
        ['011011', '101011', '101000', '100010', '110011', '111011'],
        '010001000100010101010110',
    ),
    (
        ['111100', '110001', '100011', '001101', '110011', '110011'],
        '010000100100100101001110',
    ),
]


@mark.parametrize('qr_code, expected', tests)
def test_solution(qr_code: list[str], expected: str) -> None:
    assert decode_qr(qr_code) == expected


if __name__ == '__main__':
    qr_code, expected = tests[4]
    print(decode_qr(qr_code))
