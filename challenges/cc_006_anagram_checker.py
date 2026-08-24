"""Daily Coding Challenge #6 (2025-08-16) - freeCodeCamp.org."""

# Anagram Checker
# Given two strings, determine if they are anagrams of each other (contain the same
# characters in any order).
#
# - Ignore casing and white space.
from collections import Counter

from pytest import mark


def are_anagrams(str1: str, str2: str) -> bool:
    """Check if two strings are anagrams of each other.

    Args:
        str1: string 1 to compare
        str2: string 2 to compare

    Returns:
        True if the strings are anagrams, False otherwise.
    """
    clean1 = ''.join(str1.split()).lower()
    clean2 = ''.join(str2.split()).lower()
    return Counter(clean1) == Counter(clean2)


tests = [
    ('listen', 'silent', True),
    ('School master', 'The classroom', True),
    ('A gentleman', 'Elegant man', True),
    ('Hello', 'World', False),
    ('apple', 'banana', False),
    ('cat', 'dog', False),
]


@mark.parametrize('str1, str2, expected', tests)
def test_are_anagrams(str1: str, str2: str, expected: bool) -> None:
    """Test are_anagrams function."""
    assert are_anagrams(str1, str2) == expected


if __name__ == '__main__':
    str1, str2, expected = tests[0]
    print(are_anagrams(str1, str2))
