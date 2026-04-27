# Daily Coding challenge #260 (2026-04-27) - freeCodeCamp.org
# Word Score
# Given a word, return its score using a standard letter-value table:

# Letter	Value
# A	1
# B	2
# ...	...
# Z	26
# Upper and lowercase letters have the same value.
import string
from types import MappingProxyType

from pytest import mark

# Solution using a mapping table that burns fast on passing non-alphabetic characters:
LETTER_VALUE_TABLE = MappingProxyType(
    {letter: value for value, letter in enumerate(string.ascii_lowercase, start=1)}
    | {letter: value for value, letter in enumerate(string.ascii_uppercase, start=1)},
)


def get_word_score(word: str) -> int:
    return sum(LETTER_VALUE_TABLE[letter] for letter in word)


# Very short algorithmic solution, but convert also non-alphabetic characters:
# _BASE = ord('a') - 1

# def get_word_score(word: str) -> int:
#     return sum(ord(char.lower()) - _BASE for char in word)


tests = [
    ('hi', 17),
    ('hello', 52),
    ('hippopotamus', 169),
    ('freeCodeCamp', 94),
]


@mark.parametrize('word, expected', tests)
def test_get_word_score(word: str, expected: int) -> None:
    assert get_word_score(word) == expected


if __name__ == '__main__':
    word, expected = tests[0]
    print(get_word_score(word))
