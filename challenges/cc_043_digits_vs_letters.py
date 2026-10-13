"""Daily Coding Challenge #43 (2025-09-22) - freeCodeCamp.org."""

# Digits vs Letters
# Given a string, return "digits" if the string has more digits than letters, "letters"
# if it has more letters than digits, and "tie" if it has the same amount of digits and
# letters.
#
# - Digits consist of 0-9.
# - Letters consist of a-z in upper or lower case.
# - Ignore any other characters.
from string import ascii_letters, digits

from pytest import mark

LETTERS = set(ascii_letters)
DIGITS = set(digits)


def digits_or_letters(s: str) -> str:
    """Determine whether a string has more letters or digits.

    A character counts as a letter if it is a-z or A-Z, and as a digit if
    it is 0-9. All other characters are ignored.

    Args:
        s: The string to analyze.

    Returns:
        'letters' if letters outnumber digits, 'digits' if digits outnumber
        letters, or 'tie' if the counts are equal.

    Raises:
        ValueError: If `s` is empty.
    """
    if not s:
        msg = 'input string cannot be empty'
        raise ValueError(msg)

    diff = sum(1 if char in LETTERS else -1 if char in DIGITS else 0 for char in s)

    return 'letters' if diff > 0 else 'digits' if diff < 0 else 'tie'


tests = [
    ('abc123', 'tie'),
    ('a1b2c3d', 'letters'),
    ('1a2b3c4', 'digits'),
    ('abc123!@#DEF', 'letters'),
    ('H3110 W0R1D', 'digits'),
    ('P455W0RD', 'tie'),
]


@mark.parametrize('s, expected', tests)
def test_digits_or_letters(s: str, expected: str) -> None:
    """Test digits_or_letters function."""
    assert digits_or_letters(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(digits_or_letters(s))
