# Daily Coding challenge #1 (2025-08-11) - freeCodeCamp.org
# Vowel Balance
# Given a string, determine whether the number of vowels in the first half of the
# string is equal to the number of vowels in the second half.

# The string can contain any characters.
# The letters a, e, i, o, and u, in either uppercase or lowercase, are considered
# vowels.
# If there's an odd number of characters in the string, ignore the center character.
from pytest import mark


def is_balanced(s: str) -> bool:
    vowels = 'aeiouAEIOU'
    n = len(s)
    mid = n // 2

    return sum(c in vowels for c in s[:mid]) == sum(
        c in vowels for c in s[mid + n % 2 :]
    )


tests = [
    ('racecar', True),
    ('Lorem Ipsum', True),
    ('Kitty Ipsum', False),
    ('string', False),
    (' ', True),
    ('abcdefghijklmnopqrstuvwxyz', False),
    ('123A#b!E&*456-o.U', True),
]


@mark.parametrize('s, expected', tests)
def test_is_balanced(s: str, expected: bool) -> None:
    assert is_balanced(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(is_balanced(s))
