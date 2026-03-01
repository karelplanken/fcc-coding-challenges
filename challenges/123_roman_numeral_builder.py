# Daily Coding challenge #123 (2025-12-11) - freeCodeCamp.org
# Roman Numeral Builder
# Given an integer, return its equivalent value in Roman numerals.

# Roman numerals use these symbols:

# Symbol	Value
# I	1
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000
# Roman numerals are written from largest to smallest, left to right using the
# following rules:

# Addition is used when a symbol is followed by one of equal or smaller value.
# For example, 18 is written as XVIII (10 + 5 + 1 + 1 + 1 = 18).
# Subtraction is used when a smaller symbol appears before a larger one, to represent
# 4 or 9 in any place value. For example, 19 is written as XIX (10 + (10 - 1)).
# No symbol may be repeated more than three times in a row. Subtraction is used when
# you would otherwise need to write a symbol more than three times in a row. So the
# largest number you can write is 3999.
# Here's one more example:
# given 1464, return "MCDLXIV" (1000 + (500 - 100) + 50 + 10 + (5 - 1)).
from types import MappingProxyType

from pytest import mark

VALUE_TO_SYMBOL = MappingProxyType(
    {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }
)


def to_roman(num: int) -> str:
    result = []

    for value, symbol in VALUE_TO_SYMBOL.items():
        count, num = divmod(num, value)
        if count:
            result.append(symbol * count)

    return ''.join(result)


tests = [
    (18, 'XVIII'),
    (19, 'XIX'),
    (1464, 'MCDLXIV'),
    (2025, 'MMXXV'),
    (3999, 'MMMCMXCIX'),
]


@mark.parametrize('num,expected', tests)
def test_to_roman(num: int, expected: str) -> None:
    assert to_roman(num) == expected


if __name__ == '__main__':
    num, expected = tests[0]
    print(to_roman(num))
