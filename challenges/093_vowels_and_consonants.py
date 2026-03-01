# Daily Coding challenge #93 (2025-11-11) - freeCodeCamp.org
# Vowels and Consonants
# Given a string, return an array with the number of vowels and number of consonants in
# the string.

# Vowels consist of a, e, i, o, u in any case.
# Consonants consist of all other letters in any case.
# Ignore any non-letter characters.
# For example, given "Hello World", return [3, 7].
from pytest import mark


# Readable and verbose but efficient:
def count(s: str) -> list[int]:
    # Sticking with a string is perfectly fine here:
    VOWELS = 'aeiouAEIOU'
    # VOWELS = {'a','e', 'i', 'o', 'u','A','E','I','O','U'}

    vowels = consonants = 0

    for char in s:
        if char in VOWELS:
            vowels += 1
        elif char.isalpha():
            consonants += 1

    return [vowels, consonants]


# Concise, less efficient (multiple iterations)
# def count(s: str) -> list[int]:
#     VOWELS = 'aeiouAEIOU'
#     return [
#         sum(1 for char in s if char in VOWELS),
#         sum(1 for char in s if char not in VOWELS and char.isalpha()),
#     ]


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
    assert count(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(count(s))
