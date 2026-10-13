"""Daily Coding Challenge #50 (2025-09-29) - freeCodeCamp.org."""

# Longest Word
# Given a sentence, return the longest word in the sentence.
#
# - Ignore periods (.) when determining word length.
# - If multiple words are ties for the longest, return the first one that occurs.
from pytest import mark


def get_longest_word(sentence: str) -> str:
    """Finds the longest word in a sentence.

    Args:
        sentence: A sentence containing words separated by whitespace.

    Returns:
        The longest word in the sentence with periods removed. If several
        words tie for the longest, the first one is returned.

    Raises:
        ValueError: If the sentence contains no words once periods are removed.
    """
    words = sentence.replace('.', '').split()
    if not words:
        msg = 'sentence must contain at least one word'
        raise ValueError(msg)
    return max(words, key=len)


tests = [
    ('coding is fun', 'coding'),
    ('Coding challenges are fun and educational.', 'educational'),
    ('This sentence has multiple long words.', 'sentence'),
]


@mark.parametrize('sentence, expected', tests)
def test_get_longest_word(sentence: str, expected: str) -> None:
    """Test get_longest_word function."""
    assert get_longest_word(sentence) == expected


if __name__ == '__main__':
    sentence, expected = tests[0]
    print(get_longest_word(sentence), expected)
