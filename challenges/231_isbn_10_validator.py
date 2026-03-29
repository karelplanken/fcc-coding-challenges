# Daily Coding challenge #231 (2026-03-29) - freeCodeCamp.org
# ISBN-10 Validator
# Given a string, determine if it's a valid ISBN-10.

# An ISBN-10 consists of hyphens ("-") and 10 other characters. After removing the
# hyphens ("-"):

# The first 9 characters must be digits, and
# The final character may be a digit or the letter "X", which represents the number 10.
# To validate it:

# Multiply each digit (or value) by its position (multiply the first digit by 1, the
# second by 2, and so on).
# Add all the results together.
# If the total is divisible by 11, it's valid.
from pytest import mark


def is_valid_isbn10(s: str) -> bool:
    # Sanitize input:
    chars = s.replace('-', '')

    # Validate length and character requirements:
    if len(chars) != 10 or not all(
        c.isdigit() or (c == 'X' and i == 10) for i, c in enumerate(chars, 1)
    ):
        return False

    # Compute total and check divisibility by 11:
    total = sum((10 if c == 'X' else int(c)) * i for i, c in enumerate(chars, 1))
    return total % 11 == 0


tests = [
    ('0-306-40615-2', True),
    ('0-306-40615-1', False),
    ('0-8044-2957-X', True),
    ('X-306-40615-2', False),
    ('0-6822-2589-4', True),
]


@mark.parametrize('s, expected', tests)
def test_solution(s: str, expected: bool) -> None:
    assert is_valid_isbn10(s) == expected


if __name__ == '__main__':
    s, expected = tests[4]
    print(is_valid_isbn10(s))
