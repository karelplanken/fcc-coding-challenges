"""Daily Coding Challenge #44 (2025-09-23) - freeCodeCamp.org."""

# String Mirror
# Given two strings, determine if the second string is a mirror of the first.
#
# - A string is considered a mirror if it contains the same letters in reverse order.
# - Treat uppercase and lowercase letters as distinct.
# - Ignore all non-alphabetical characters.
from pytest import mark


def is_mirror(str1: str, str2: str) -> bool:
    """Determine if str2 is a mirror of str1.

    Letters are compared case-sensitively; any character for which
    ``str.isalpha()`` is False is ignored (Unicode letters count).

    Args:
        str1: The first string.
        str2: The second string.

    Returns:
        True if str2's letters are str1's letters in reverse order.
    """
    return ''.join(filter(str.isalpha, str1)) == ''.join(
        filter(str.isalpha, reversed(str2))
    )


tests = [
    ('helloworld', 'helloworld', False),
    ('Hello World', 'dlroW olleH', True),
    ('RaceCar', 'raCecaR', True),
    ('RaceCar', 'RaceCar', False),
    ('Mirror', 'rorrim', False),
    ('Hello World', 'dlroW-olleH', True),
    ('Hello World', '!dlroW !olleH', True),
]


@mark.parametrize('str1, str2, expected', tests)
def test_is_mirror(str1: str, str2: str, expected: bool) -> None:
    """Test is_mirror function."""
    assert is_mirror(str1, str2) == expected


if __name__ == '__main__':
    str1, str2, expected = tests[1]
    is_mirror(str1, str2)
