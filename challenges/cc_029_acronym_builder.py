"""Daily Coding Challenge #29 (2025-09-08) - freeCodeCamp.org."""

# Acronym Builder
# Given a string containing one or more words, return an acronym of the words using the
# following constraints:
#
# - The acronym should consist of the first letter of each word capitalized, unless
#   otherwise noted.
# - The acronym should ignore the first letter of these words unless they are the first
#   word of the given string: a, for, an, and, by, and of.
# - The acronym letters should be returned in the order they are given.
# - The acronym should not contain any spaces.
from pytest import mark

_IGNORE_WORDS = frozenset({'a', 'for', 'an', 'and', 'by', 'of'})


def build_acronym(s: str) -> str:
    """Return an acronym of the words in the given string.

    Notes:
    - The input string contains one or more words separated by spaces.
    - The input string does not contain words that start with non-alphabetic characters.

    Args:
        s: A string containing one or more words.

    Returns:
        An acronym of the words in the given string.

    Raises:
        ValueError: If the string contains no words.
    """
    words = s.split()
    if not words:
        msg = "parameter 's' must contain at least one word"
        raise ValueError(msg)

    first, *rest = words
    return first[0].upper() + ''.join(
        word[0].upper() for word in rest if word.lower() not in _IGNORE_WORDS
    )


tests = [
    ('karel', 'K'),
    ('Search Engine Optimization', 'SEO'),
    ('Frequently Asked Questions', 'FAQ'),
    ('National Aeronautics and Space Administration', 'NASA'),
    ('Federal Bureau of Investigation', 'FBI'),
    ('For your information', 'FYI'),
    ('By the way', 'BTW'),
    (
        'An unstoppable herd of waddling penguins overtakes the icy '
        + 'mountains and sings happily',
        'AUHWPOTIMSH',
    ),
]


@mark.parametrize('s, expected', tests)
def test_build_acronym(s: str, expected: str) -> None:
    """Test build_acronym function."""
    assert build_acronym(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(build_acronym(s))
