# Daily Coding challenge #242 (2026-04-09) - freeCodeCamp.org
# Next Bingo Number
# Given a bingo number, return the next bingo number sequentially.

# A bingo number is a single letter followed by a number in its range according to
# this chart:

# Letter	Number Range
# "B"	1-15
# "I"	16-30
# "N"	31-45
# "G"	46-60
# "O"	61-75
# For example, given "B10", return "B11", the next bingo number. If given the last
# bingo number, return "B1".

# # First solution: Concise solution for  small utility/coding challenge:
# from types import MappingProxyType

# from pytest import mark

# NUMBER_TO_LETTER = MappingProxyType(
#     {
#         **{i: 'B' for i in range(1, 16)},
#         **{i: 'I' for i in range(16, 31)},
#         **{i: 'N' for i in range(31, 46)},
#         **{i: 'G' for i in range(46, 61)},
#         **{i: 'O' for i in range(61, 76)},
#     }
# )

# MAX_NUMBER = max(NUMBER_TO_LETTER)


# def get_next_bingo_number(n: str) -> str:
#     next_bingo_number = (int(n[1:]) + 1) % MAX_NUMBER or MAX_NUMBER
#     return f'{NUMBER_TO_LETTER[next_bingo_number]}{next_bingo_number}'


# Second solution: Production bingo application, domain matters:
from dataclasses import dataclass
from types import MappingProxyType

from pytest import mark


@dataclass(frozen=True)
class BingoNumber:
    letter: str
    min_number: int
    max_number: int
    next_letter: str


BINGO_NUMBERS = MappingProxyType(
    {
        'B': BingoNumber('B', 1, 15, 'I'),
        'I': BingoNumber('I', 16, 30, 'N'),
        'N': BingoNumber('N', 31, 45, 'G'),
        'G': BingoNumber('G', 46, 60, 'O'),
        'O': BingoNumber('O', 61, 75, 'B'),
    }
)


def get_next_bingo_number(n: str) -> str:
    letter, number = n[0], int(n[1:])
    current = BINGO_NUMBERS[letter]

    if number < current.max_number:
        return f'{letter}{number + 1}'

    next_letter = BINGO_NUMBERS[current.next_letter]
    return f'{next_letter.letter}{next_letter.min_number}'


tests = [
    ('B10', 'B11'),
    ('N33', 'N34'),
    ('I30', 'N31'),
    ('G60', 'O61'),
    ('O75', 'B1'),
    ('O74', 'O75'),
]


@mark.parametrize('n, expected', tests)
def test_get_next_bingo_number(n: str, expected: str) -> None:
    assert get_next_bingo_number(n) == expected


if __name__ == '__main__':
    n, expected = tests[5]
    print(get_next_bingo_number(n))
