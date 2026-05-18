# Daily Coding challenge #281 (2026-05-18) - freeCodeCamp.org
# Bingo Range
# Given a bingo letter, return the number range associated with that letter.

# Letter	Number Range
# "B"	1-15
# "I"	16-30
# "N"	31-45
# "G"	46-60
# "O"	61-75
# Return an array with all numbers in the range from smallest to largest.
from types import MappingProxyType

from pytest import mark

# Data-driven
# Explicit lookup table: verbose but instantly readable
LETTER_RANGE = MappingProxyType({
    'B': (1, 16),
    'I': (16, 31),
    'N': (31, 46),
    'G': (46, 61),
    'O': (61, 76),
})


def get_bingo_range(letter: str) -> list[int]:
    return list(range(*LETTER_RANGE[letter]))


# Logic-driven
# Derives ranges from letter position and a fixed range size:
# concise but requires a moment to parse
# BINGO_LETTERS = 'BINGO'
# RANGE_SIZE = 15


# def get_bingo_range(letter: str) -> list[int]:
#     index = BINGO_LETTERS.index(letter)
#     start = index * RANGE_SIZE + 1
#     return list(range(start, start + RANGE_SIZE))


tests = [
    ('B', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
    ('I', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),
    ('N', [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]),
    ('G', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]),
    ('O', [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]),
]


@mark.parametrize('letter, expected', tests)
def test(letter: str, expected: list[int]) -> None:
    assert get_bingo_range(letter) == expected


if __name__ == '__main__':
    letter, expected = tests[0]
    print(get_bingo_range(letter))
