# Daily Coding challenge #240 (2026-04-07) - freeCodeCamp.org
# Palindrome Characters
# Given a string, determine if it's a palindrome and return the middle character
# (if it's odd length) or middle two characters (if it's even).

# A palindrome is a string that is the same forward and backward.
# If it's not a palindrome, return "none".
from pytest import mark


def palindrome_locator(s: str) -> str:
    if s != s[::-1]:
        return 'none'

    mid = len(s) // 2
    return s[mid] if len(s) % 2 != 0 else s[mid - 1 : mid + 1]


tests = [
    ('racecar', 'e'),
    ('level', 'v'),
    ('freecodecamp', 'none'),
    ('noon', 'oo'),
    ('11100111', '00'),
]


@mark.parametrize('s, expected', tests)
def test_palindrome_locator(s: str, expected: str) -> None:
    assert palindrome_locator(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(palindrome_locator(s))
