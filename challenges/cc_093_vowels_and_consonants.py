"""Daily Coding Challenge #93 (2025-11-11) - freeCodeCamp.org."""

# Vowels and Consonants
# Given a string, return an array with the number of vowels and number of consonants in
# the string.
#
# - Vowels consist of a, e, i, o, u in any case.
# - Consonants consist of all other letters in any case.
# - Ignore any non-letter characters.
#
# For example, given "Hello World", return [3, 7].
from string import ascii_letters

from pytest import mark

_VOWELS = frozenset('aeiouAEIOU')
_CONSONANTS = frozenset(ascii_letters) - _VOWELS


def count(s: str) -> list[int]:
    """Count the number of vowels and consonants in a string.

    Only ASCII letters are considered. Non-letter characters are ignored.

    Args:
        s: The string to count vowels and consonants in.

    Returns:
        A two-element list: the number of vowels, then the number of consonants.
    """
    vowels = consonants = 0
    for char in s:
        if char in _VOWELS:
            vowels += 1
        elif char in _CONSONANTS:
            consonants += 1
    return [vowels, consonants]


tests = [
    ('Hello World', [3, 7]),
    ('JavaScript', [3, 7]),
    ('Python', [1, 5]),
    ('freeCodeCamp', [5, 7]),
    ('Hello, World!', [3, 7]),
    ('The quick brown fox jumps over the lazy dog.', [11, 24]),
]


@mark.parametrize(('s', 'expected'), tests)
def test_count(s: str, expected: list[int]) -> None:
    """Test count function."""
    assert count(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(count(s))
