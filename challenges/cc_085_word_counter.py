"""Daily Coding Challenge #85 (2025-11-03) - freeCodeCamp.org."""

# Word Counter
# Given a sentence string, return the number of words that are in the sentence.
#
# - Words are any sequence of non-space characters and are separated by a single space.
from pytest import mark


def count_words(sentence: str) -> int:
    r"""Count the words in a sentence.

    A word is a non-empty run of non-space characters. Only the space character
    (U+0020) separates words; other whitespace, such as tabs or newlines, counts
    as part of a word. Leading, trailing, or repeated spaces do not produce empty
    words, so an empty or all-space sentence has zero words.

    Args:
        sentence: The sentence to count words in.

    Returns:
        The number of words in the sentence.

    Examples:
        >>> count_words('Hello world')
        2
        >>> count_words('')
        0
        >>> count_words('   ')
        0
        >>> count_words(' leading and  repeated spaces ')
        4
        >>> count_words('tab\tinside')
        1
    """
    return sum(1 for word in sentence.split(' ') if word)


tests = [
    ('Hello world', 2),
    ('The quick brown fox jumps over the lazy dog.', 9),
    ('I like coding challenges!', 4),
    ('Complete the challenge in JavaScript and Python.', 7),
    ('The missing semi-colon crashed the entire internet.', 7),
]


@mark.parametrize(('sentence', 'expected'), tests)
def test_count_words(sentence: str, expected: int) -> None:
    """Test count_words function."""
    assert count_words(sentence) == expected


if __name__ == '__main__':
    sentence, expected = tests[0]
    print(count_words(sentence))
