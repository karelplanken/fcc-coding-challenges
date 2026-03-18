# Daily Coding challenge #220 (2026-03-18) - freeCodeCamp.org
# Largest Number
# Given a string of numbers separated by various punctuation, return the largest number.

# The given string will only contain numbers and separators.
# Separators can be commas (","), exclamation points ("!"), question marks ("?"),
# colons (":"), or semi-colons (";").
import re

from pytest import mark


def largest_number(s: str) -> float:
    return max(map(float, re.split(r'[,!?:;]', s)))


tests = [
    ('1,2', 2),
    ('4;15:60,26?52!0', 60),
    ('-402,-1032!-569:-947;-633?-800!-1012;-402,-723?-8102!-3011', -402),
    ('12;-50,99.9,49.1!-10.1?88?16', 99.9),
]


@mark.parametrize('s, expected', tests)
def test_largest_number(s: str, expected: int) -> None:
    assert largest_number(s) == expected


if __name__ == '__main__':
    s, expected = tests[1]
    print(largest_number(s))
