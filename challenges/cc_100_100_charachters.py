"""Daily Coding Challenge #100 (2025-11-18) - freeCodeCamp.org."""

# 100 Characters
# Welcome to the 100th Daily Coding Challenge!
#
# Given a string, repeat its characters until the result is exactly 100 characters long.
# If your repetitions go over 100 characters, trim the extra so it's exactly 100.
from itertools import cycle, islice

from pytest import mark


def one_hundred(chars: str) -> str:
    """Repeat the characters of a string until the result is 100 characters long.

    Args:
        chars: The characters to repeat, in order.

    Returns:
        A string of exactly 100 characters made by cycling through ``chars``,
        or an empty string if ``chars`` is empty.
    """
    return ''.join(islice(cycle(chars), 100))


tests = [
    (
        'One hundred ',
        'One hundred One hundred One hundred One hundred One hundred One hundred One '
        + 'hundred One hundred One ',
    ),
    (
        'freeCodeCamp ',
        'freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp '
        + 'freeCodeCamp freeCodeC',
    ),
    (
        'daily challenges ',
        'daily challenges daily challenges daily challenges daily challenges daily '
        + 'challenges daily challenge',
    ),
    (
        '!',
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',
    ),
]


@mark.parametrize(('chars', 'expected'), tests)
def test_one_hundred(chars: str, expected: str) -> None:
    """Test one_hundred function."""
    assert one_hundred(chars) == expected


if __name__ == '__main__':
    chars, expected = tests[0]
    print(one_hundred(chars))
