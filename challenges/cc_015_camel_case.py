"""Daily Coding Challenge #15 (2025-08-25) - freeCodeCamp.org."""

# camelCase
# Given a string, return its camel case version using the following rules:
#
# - Words in the string argument are separated by one or more characters from the
#   following set: space ( ), dash (-), or underscore (_). Treat any sequence of these
#   as a word break.
# - The first word should be all lowercase.
# - Each subsequent word should start with an uppercase letter, with the rest of it
#   lowercase.
# - All spaces and separators should be removed.
import re

from pytest import mark


def to_camel_case(s: str) -> str:
    """Convert a string to camel case.

    Assumes that `s` contains only letters, spaces, dashes, and underscores.

    Args:
        s: The string to convert.

    Returns:
        The camel case version of the string.
    """
    words: list[str] = re.findall(r'[^\s_-]+', s)
    if not words:
        return ''
    first, *rest = words
    # capitalize() uppercases index 0 and lowercases the rest of each word —
    # unlike title(), it won't re-capitalize after internal punctuation.
    return first.lower() + ''.join(word.capitalize() for word in rest)


tests = [
    ('hello world', 'helloWorld'),
    ('HELLO WORLD', 'helloWorld'),
    ('secret agent-X', 'secretAgentX'),
    ('FREE cODE cAMP', 'freeCodeCamp'),
    (
        'ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and \
            a_parrot_ _named- _squawk',
        'yeOldSeaFaringBuccaneerWithAPegLegAndAParrotNamedSquawk',
    ),
]


@mark.parametrize('s, expected', tests)
def test_to_camel_case(s: str, expected: str) -> None:
    """Test to_camel_case function."""
    assert to_camel_case(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(to_camel_case(s))
