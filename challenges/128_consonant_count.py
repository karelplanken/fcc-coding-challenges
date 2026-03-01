# Daily Coding challenge #128 (2025-12-16) - freeCodeCamp.org
# Consonant Count
# Given a string and a target number, determine whether the string contains exactly the
# target number of consonants.

# Consonants are all alphabetic characters except "a", "e", "i", "o", and "u" in any
# case.
# Ignore digits, punctuation, spaces, and other non-letter characters when counting.
import string

from pytest import mark

VOWELS = set('aeiouAEIOU')
CONSONANTS = set(string.ascii_letters) - VOWELS


def has_consonant_count(text: str, target: int) -> bool:
    return sum(char in CONSONANTS for char in text) == target


tests = [
    ('helloworld', 7, True),
    ('eieio', 5, False),
    ('freeCodeCamp Rocks!', 11, True),
    ('Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.', 24, False),
    ('Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.', 23, True),
]


@mark.parametrize('text, target, expected', tests)
def test_has_consonant_count(text: str, target: int, expected: bool) -> None:
    assert has_consonant_count(text, target) == expected


if __name__ == '__main__':
    text, target, expected = tests[4]
    has_consonant_count(text, target)
