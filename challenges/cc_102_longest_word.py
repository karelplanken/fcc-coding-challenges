"""Daily Coding Challenge #102 (2025-11-20) - freeCodeCamp.org."""

# Longest Word
# Given a sentence string, return the longest word in the sentence.
#
# - Words are separated by a single space.
# - Only letters (a-z, case-insensitive) count toward the word's length.
# - If there are multiple words with the same length, return the first one that appears.
# - Return the word as it appears in the given string, with punctuation removed.
import re

from pytest import mark

_NON_LETTER = re.compile(r'[^A-Za-z ]+')


def longest_word(sentence: str) -> str:
    """Return the longest word in a sentence.

    Length counts ASCII letters (a-z, A-Z) only; all other characters are
    stripped from the returned word. Ties go to the word that appears first.

    Args:
        sentence: Words separated by spaces.

    Returns:
        The longest word with non-letters removed, or an empty string if the
        sentence contains no words.
    """
    return max(_NON_LETTER.sub('', sentence).split(), key=len, default='')


tests = [
    ('The quick red fox', 'quick'),
    ('Hello coding challenge.', 'challenge'),
    ('Do Try This At Home.', 'This'),
    ('This sentence... has commas, ellipses, and an exclamation point!', 'exclamation'),
    ('A tie? No way!', 'tie'),
    ("Wouldn't you like to know.", 'Wouldnt'),
]


@mark.parametrize(('sentence', 'expected'), tests)
def test_longest_word(sentence: str, expected: str) -> None:
    """Test longest_word function."""
    assert longest_word(sentence) == expected


if __name__ == '__main__':
    sentence, expected = tests[0]
    print(longest_word(sentence))
