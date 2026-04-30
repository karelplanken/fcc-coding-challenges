# Daily Coding challenge #261 (2026-04-28) - freeCodeCamp.org
# Number Words
# Given an integer from 0 to 99, return its English word representation.
# 0 returns "zero".
# Numbers 1-19 have unique names:
# ("one", "two", ..., "ten", "eleven", ..., "eighteen", "nineteen").
# Multiples of 10 from 20-90 have their own names:
# ("twenty", "thirty", ..., "eighty", "ninety").
# Numbers 21-99 that are not multiples of 10 are written as two words joined by a
# hyphen. For example "forty-two" and "fifty-three".
from types import MappingProxyType

from pytest import mark

ONES = MappingProxyType(
    {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
    }
)

TENS = MappingProxyType(
    {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety',
    }
)


def get_number_words(n: int) -> str:
    if n < 20:
        return ONES[n]

    tens, unit = divmod(n, 10)

    return TENS[tens] if unit == 0 else f'{TENS[tens]}-{ONES[unit]}'


tets = [
    (0, 'zero'),
    (10, 'ten'),
    (19, 'nineteen'),
    (30, 'thirty'),
    (53, 'fifty-three'),
    (7, 'seven'),
    (12, 'twelve'),
    (60, 'sixty'),
    (67, 'sixty-seven'),
    (98, 'ninety-eight'),
]


@mark.parametrize('n, expected', tets)
def test_get_number_words(n: int, expected: str) -> None:
    assert get_number_words(n) == expected


if __name__ == '__main__':
    n, expected = tets[9]
    print(get_number_words(n))
