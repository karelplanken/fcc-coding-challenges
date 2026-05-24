# Daily Coding challenge #287 (2026-05-24) - freeCodeCamp.org
# Roman Numeral Fixer
# Given a string of malformed Roman numerals, return the value in standard Roman
# numeral notation.
# The input will only use additive notation, so each symbol adds its value to the
# total. As a reminder, here are the symbols and values:
# Symbol	Value
# "I"	1
# "V"	5
# "X"	10
# "L"	50
# "C"	100
# "D"	500
# "M"	1000
# When re-encoding, use the largest possible symbol at each step, using subtractive
# pairs ("IV", "IX", "XL", "XC", "CD", "CM") where needed.
from types import MappingProxyType

from pytest import mark

VALUE_TO_SYMBOL = MappingProxyType({
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
})

SYMBOL_TO_VALUE = MappingProxyType({
    value: key for key, value in VALUE_TO_SYMBOL.items()
})


def parse_malformed_roman_numeral(numeral: str) -> int:
    # Convert to values once
    return sum(SYMBOL_TO_VALUE[char] for char in numeral)


def to_roman(n: int) -> str:
    parts = []
    for value, symbol in VALUE_TO_SYMBOL.items():
        while n >= value:
            parts.append(symbol)
            n -= value
    return ''.join(parts)


def fix_numerals(s: str) -> str:
    n = parse_malformed_roman_numeral(s)
    return to_roman(n)


tests = [
    ('XIIIII', 'XV'),
    ('IIIILX', 'LXIV'),
    ('XXVVVIIIII', 'XL'),
    ('MDCCLXXXXVIIII', 'MDCCXCIX'),
    ('IIIIVVVVXXXXLLLLCCDD', 'MCDLXIV'),
    ('ILCDMIVDIIXLCVCXDL', 'MMCMLXXXIV'),
]


@mark.parametrize('s, expected', tests)
def test_fix_numerals(s: str, expected: str) -> None:
    assert fix_numerals(s) == expected


if __name__ == '__main__':
    s, expected = tests[5]
    print(fix_numerals(s))
