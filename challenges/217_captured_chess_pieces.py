# Daily Coding challenge #217 (2026-03-15) - freeCodeCamp.org
# Captured Chess Pieces
# Given an array of strings representing chess pieces you still have on the board,
# calculate the value of the pieces your opponent has captured.

# In chess, you start with 16 pieces:

# Piece   Abbreviation	 Quantity     Value
# Pawn      "P"             8           1
# Rook      "R"             2           5
# Knight	"N"             2           3
# Bishop	"B"             2           3
# Queen     "Q"             1           9
# King      "K"             1           0
# The given array will only contain the abbreviations above.
# Any of the 16 pieces not included in the given array have been captured.
# Return the total value of all captured pieces, unless...
# If the King has been captured, return "Checkmate".
from dataclasses import dataclass

from pytest import mark


@dataclass
class ChessPiece:
    name: str
    abbreviation: str
    quantity: int
    value: int


PIECES = {
    'P': ChessPiece(name='Pawn', abbreviation='P', quantity=8, value=1),
    'R': ChessPiece(name='Rook', abbreviation='R', quantity=2, value=5),
    'N': ChessPiece(name='Knight', abbreviation='N', quantity=2, value=3),
    'B': ChessPiece(name='Bishop', abbreviation='B', quantity=2, value=3),
    'Q': ChessPiece(name='Queen', abbreviation='Q', quantity=1, value=9),
    'K': ChessPiece(name='King', abbreviation='K', quantity=1, value=0),
}

INITIAL_VALUE = sum(piece.quantity * piece.value for piece in PIECES.values())


def get_captured_value(pieces: list[str]) -> int | str:
    if 'K' not in pieces:
        return 'Checkmate'
    
    remaining_value = sum(PIECES[piece].value for piece in pieces)

    return INITIAL_VALUE - remaining_value


tests = [
    (['P', 'P', 'P', 'P', 'P', 'P', 'R', 'R', 'N', 'B', 'Q', 'K'], 8),
    (['P', 'P', 'P', 'P', 'P', 'R', 'B', 'K'], 26),
    (['K', 'P', 'P', 'N', 'P', 'P', 'R', 'P', 'B', 'P', 'N', 'B'], 16),
    (['P', 'Q', 'N', 'P', 'P', 'B', 'K', 'P', 'R', 'R', 'P', 'P', 'B', 'P'], 4),
    (['P', 'K'], 38),
    (
        [
            'N',
            'P',
            'P',
            'B',
            'K',
            'P',
            'Q',
            'N',
            'P',
            'P',
            'R',
            'R',
            'P',
            'P',
            'P',
            'B',
        ],
        0,
    ),
    (['N', 'P', 'P', 'B', 'P', 'R', 'Q', 'P', 'P', 'P', 'B'], 'Checkmate'),
]


@mark.parametrize('pieces, expected', tests)
def test_get_captured_value(pieces: list[str], expected: int | str) -> None:
    assert get_captured_value(pieces) == expected


if __name__ == '__main__':
    pieces, expected = tests[0]
    print(get_captured_value(pieces))
