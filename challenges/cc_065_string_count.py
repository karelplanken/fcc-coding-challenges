"""Daily Coding Challenge #65 (2025-10-14) - freeCodeCamp.org."""

# String Count
# Given two strings, determine how many times the second string appears in the first.
#
# - The pattern string can overlap in the first string. For example, "aaa" contains "aa"
#   twice. The first two a's and the second two.
from pytest import mark


def count(text: str, parameter: str) -> int:
    """Count occurrences of parameter in text, including overlapping ones.

    Args:
        text: The string to search in.
        parameter: The substring to search for.

    Returns:
        The number of (possibly overlapping) occurrences of parameter in text.

    Raises:
        ValueError: If parameter is an empty string.
    """
    if not parameter:
        msg = 'parameter must be a non-empty string'
        raise ValueError(msg)
    occurrences = 0
    index = text.find(parameter)
    while index != -1:
        occurrences += 1
        index = text.find(parameter, index + 1)
    return occurrences


tests = [
    ('abcdefg', 'def', 1),
    ('hello', 'world', 0),
    ('mississippi', 'iss', 2),
    ('she sells seashells by the seashore', 'sh', 3),
    ('101010101010101010101', '101', 10),
]


@mark.parametrize('text, parameter, expected', tests)
def test_count(text: str, parameter: str, expected: int) -> None:
    """Test count function."""
    assert count(text, parameter) == expected


if __name__ == '__main__':
    text, parameter, expected = tests[0]
    print(count(text, parameter))
