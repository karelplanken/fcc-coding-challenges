# Daily Coding challenge #325 (2026-07-01) - freeCodeCamp.org
# Lucky Number
# Given a string of a person's first and last name, calculate their lucky number using
# the following rules:
#
# - First and last names are separated by a space
# - Find the vowel and consonant count for each name
# - Multiply the smaller vowel and consonant counts by each other and then by the length
#   of the smaller name
# - Do the same for the two larger counts and the larger name
# - Subtract the smaller value from the larger one to get their lucky number
#
# If the final value is zero (`0`), return `13`.
import math
from string import ascii_lowercase

from pytest import mark

VOWELS = frozenset('aeiou')
CONSONANTS = frozenset(ascii_lowercase) - VOWELS


def analyze_name(name: str) -> tuple[int, int, int]:
    vowels = consonants = 0
    for char in name.lower():
        if char in VOWELS:
            vowels += 1
        elif char in CONSONANTS:
            consonants += 1
    return vowels, consonants, len(name)


def get_lucky_number(name: str) -> int:
    first, last = (analyze_name(n) for n in name.split())
    pairs = list(zip(first, last))
    lucky_number = math.prod(max(pair) for pair in pairs) - math.prod(
        min(pair) for pair in pairs
    )
    return lucky_number if lucky_number else 13


tests = [
    ('John Doe', 21),
    ('Olivia Lewis', 52),
    ('James Wilson', 18),
    ('Elizabeth Hernandez', 81),
    ('Mike Walker', 32),
    ('Chloe Perez', 13),
]


@mark.parametrize('name, expected', tests)
def test_get_lucky_number(name: str, expected: int) -> None:
    assert get_lucky_number(name) == expected


if __name__ == '__main__':
    name, expected = tests[0]
    print(get_lucky_number(name))
