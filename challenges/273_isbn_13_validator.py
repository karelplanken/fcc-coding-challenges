# Daily Coding challenge #273 (2026-05-10) - freeCodeCamp.org
# ISBN-13 Validator
# Given a string, determine if it is a valid ISBN-13 number.

# A valid ISBN-13:

# Contains only digits and hyphens
# Has exactly 13 digits after removing hyphens
# Passes the following check:
# Multiply each digit by 1 or 3, alternating (multiply the first digit by 1, the second
# by 3, the third by 1, and so on).
# The sum of the results must be divisible by 10.
from collections.abc import Callable

from pytest import mark

RULES: list[Callable[[str], bool]] = [
    lambda digits: all(char.isdecimal() for char in digits),
    lambda digits: len(digits) == 13,
    lambda digits: (
        sum(int(digit) * (1 if i % 2 == 0 else 3) for i, digit in enumerate(digits))
        % 10
        == 0
    ),
]


def is_valid_isbn_13(s: str) -> bool:
    digits = s.replace('-', '')
    return all(rule(digits) for rule in RULES)


tests = [
    ('9780306406157', True),
    ('97803064061570', False),
    ('978-0-13-595705-9', True),
    ('978-030-64061A-4', False),
    ('9-7-8-0-1-3-4-7-5-7-5-9-9', True),
]


@mark.parametrize('s, expected', tests)
def test_is_valid_isbn_13(s: str, expected: bool) -> None:
    assert is_valid_isbn_13(s) == expected


if __name__ == '__main__':
    s, expected = tests[4]
    print(is_valid_isbn_13(s))
