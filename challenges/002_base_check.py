# Daily Coding challenge #2 (2025-08-12) - freeCodeCamp.org
# Base Check
# Given a string representing a number, and an integer base from 2 to 36, determine
# whether the number is valid in that base.

# The string may contain integers, and uppercase or lowercase characters.
# The check should be case-insensitive.
# The base can be any number 2-36.
# A number is valid if every character is a valid digit in the given base.
# Example of valid digits for bases:
# Base 2: 0-1
# Base 8: 0-7
# Base 10: 0-9
# Base 16: 0-9 and A-F
# Base 36: 0-9 and A-Z
import string

from pytest import mark

# Pre-computed sets (fastest for multiple calls)
# _VALID_CHARS = string.digits + string.ascii_lowercase
# _BASE_SETS = {base: set(_VALID_CHARS[:base]) for base in range(2, 37)}


def is_valid_number(n: str, base: int) -> bool:
    given = {number.lower() for number in n}
    allowed = {char for char in (string.digits + string.ascii_lowercase)[:base]}
    return not given - allowed


tests = [
    ('10101', 2, True),
    ('10201', 2, False),
    ('76543210', 8, True),
    ('9876543210', 8, False),
    ('9876543210', 10, True),
    ('ABC', 10, False),
    ('ABC', 16, True),
    ('Z', 36, True),
    ('ABC', 20, True),
    ('4B4BA9', 16, True),
    ('5G3F8F', 16, False),
    ('5G3F8F', 17, True),
    ('abc', 10, False),
    ('abc', 16, True),
    ('AbC', 16, True),
    ('z', 36, True),
]


@mark.parametrize('n, base, expected', tests)
def test_is_valid_number(n: str, base: int, expected: bool) -> None:
    assert is_valid_number(n, base) == expected


if __name__ == '__main__':
    n, base, expected = tests[0]
    print(is_valid_number(n, base))
