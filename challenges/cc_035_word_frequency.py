"""Daily Coding Challenge #35 (2025-09-14) - freeCodeCamp.org."""

# Word Frequency
# Given a paragraph, return an array of the three most frequently occurring words.
#
# - Words in the paragraph will be separated by spaces.
# - Ignore case in the given paragraph. For example, treat Hello and hello as the same
#   word.
# - Ignore punctuation in the given paragraph. Punctuation consists of commas (,),
#   periods (.), and exclamation points (!).
# - The returned array should have all lowercase words.
# - The returned array should be in descending order with the most frequently occurring
#   word first.
from collections import Counter

from pytest import mark

MAX_WORDS = 3
PUNCTUATION_TO_STRIP = ',.!'
REMOVE_PUNCTUATION = str.maketrans('', '', PUNCTUATION_TO_STRIP)


def get_words(paragraph: str) -> list[str]:
    """Return the three most frequently occurring words in the given paragraph.

    Args:
        paragraph: Text containing words of any case and punctuation.

    Returns:
        A list of maximum three most frequently occurring words in descending order
        and in lowercase. Ties are broken by order of first appearance in the
        paragraph.

    Raises:
        ValueError: If the paragraph is empty.
    """
    if not paragraph:
        msg = 'paragraph must not be empty'
        raise ValueError(msg)

    words = paragraph.translate(REMOVE_PUNCTUATION).lower().split()
    return [word for word, _ in Counter(words).most_common(MAX_WORDS)]


tests = [
    (
        'Coding in Python is fun because coding Python allows for coding '
        + 'in Python easily while coding',
        ['coding', 'python', 'in'],
    ),
    ('I like coding. I like testing. I love debugging!', ['i', 'like', 'coding']),
    (
        'Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!',
        ['debug', 'test', 'deploy'],
    ),
]


@mark.parametrize('paragraph, expected', tests)
def test_get_words(paragraph: str, expected: list[str]) -> None:
    """Test get_words function."""
    assert get_words(paragraph) == expected


if __name__ == '__main__':
    paragraph, expected = tests[0]
    print(get_words(paragraph))
