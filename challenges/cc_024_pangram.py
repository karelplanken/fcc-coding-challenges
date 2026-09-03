"""Daily Coding Challenge #24 (2025-09-03) - freeCodeCamp.org."""

# Pangram
# Given a word or sentence and a string of lowercase letters, determine if the word or
# sentence uses all the letters from the given set at least once and no other letters.
#
# - Ignore non-alphabetical characters in the word or sentence.
# - Ignore letter casing in the word or sentence.
from pytest import mark


def is_pangram(sentence: str, letters: str) -> bool:
    """Determine if a sentence is a pangram for a given set of letters.

    Args:
        sentence: A word or sentence to check.
        letters: A string of lowercase letters to check against.

    Returns:
        True if the sentence uses all the letters from the given set at least once and
        no other letters, False otherwise.

    Raises:
        ValueError: If the letters string contains non-lowercase or non-alphabetic
            characters.
    """
    if letters and not (letters.islower() and letters.isalpha()):
        msg = f'letters must be a string of lowercase letters: {letters}'
        raise ValueError(msg)

    # Extract alphabetic characters and convert to lowercase
    sentence_letters = {char.lower() for char in sentence if char.isalpha()}
    # Check if the sets are identical
    return sentence_letters == set(letters)


# Alternative approach: represent "which letters are present" as a 32-bit
# integer bitmask instead of a set[str] (one bit per letter of the alphabet).
# Faster and more memory-efficient for repeated comparisons against a fixed
# `letters` set; less readable for a one-off check like this.

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
    """Test is_pangram function."""
    assert is_pangram(sentence, letters) == expected


if __name__ == '__main__':
    sentence, letters, expected = tests[4]
    print(is_pangram(sentence, letters))
