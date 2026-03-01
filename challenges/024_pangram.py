# Daily Coding challenge #24 (2025-09-03) - freeCodeCamp.org
# Pangram
# Given a word or sentence and a string of lowercase letters, determine if the word or
# sentence uses all the letters from the given set at least once and no other letters.

# Ignore non-alphabetical characters in the word or sentence.
# Ignore letter casing in the word or sentence.
from pytest import mark


def is_pangram(sentence: str, letters: str) -> bool:
    # Extract alphabetic characters and convert to lowercase
    sentence_chars = {char.lower() for char in sentence if char.isalpha()}
    letter_set = set(letters)

    # Check if the sets are identical
    return sentence_chars == letter_set


# Python's set operations are quite rich:
# set1 == set2  # equality
# set1 <= set2  # subset
# set1 >= set2  # superset
# set1 & set2  # intersection
# set1 | set2  # union
# set1 - set2  # difference


tests = [
    ('hello', 'helo', True),
    ('hello', 'hel', False),
    ('hello', 'helow', False),
    ('hello world', 'helowrd', True),
    ('Hello World!', 'helowrd', True),
    ('Hello World!', 'heliowrd', False),
    ('freeCodeCamp', 'frcdmp', False),
    (
        'The quick brown fox jumps over the lazy dog.',
        'abcdefghijklmnopqrstuvwxyz',
        True,
    ),
]


@mark.parametrize('sentence, letters, expected', tests)
def test_is_pangram(sentence: str, letters: str, expected: bool) -> None:
    assert is_pangram(sentence, letters) == expected


if __name__ == '__main__':
    sentence, letters, expected = tests[4]
    print(is_pangram(sentence, letters))
