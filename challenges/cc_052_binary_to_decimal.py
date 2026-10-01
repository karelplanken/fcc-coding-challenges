"""Daily Coding Challenge #52 (2025-10-01) - freeCodeCamp.org."""

# Binary to Decimal
# Given a string representing a binary number, return its decimal equivalent as a
# number.
#
# A binary number uses only the digits 0 and 1 to represent any number. To convert
# binary to decimal, multiply each digit by a power of 2 and add them together. Start by
# multiplying the rightmost digit by 2^0, the next digit to the left by 2^1, and so on.
# Once all digits have been multiplied by a power of 2, add the result together.
#
# For example, the binary number 101 equals 5 in decimal because:
#
# mathml
# 1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 4 + 0 + 1 = 5
from pytest import mark


def to_decimal(binary: str) -> int:
    """Convert a string representing a binary number to its integer value.

    Any base-2 literal accepted by ``int(x, 2)`` is valid: an optional sign,
    an optional ``0b`` prefix, underscores between digits, and surrounding
    whitespace. Any other input raises the ``ValueError`` from ``int``.

    Args:
        binary: A string representing a binary number.

    Returns:
        The integer value of the binary number.

    Examples:
        >>> to_decimal('101')
        5
        >>> to_decimal(' 0b1_01 ')
        5
        >>> to_decimal('-101')
        -5
        >>> to_decimal('102')
        Traceback (most recent call last):
            ...
        ValueError: invalid literal for int() with base 2: '102'
    """
    return int(binary, 2)


tests = [
    ('101', 5),
    ('1010', 10),
    ('10010', 18),
    ('1010101', 85),
]


@mark.parametrize('binary, expected', tests)
def test_to_decimal(binary: str, expected: int) -> None:
    """Test to_decimal function."""
    assert to_decimal(binary) == expected


if __name__ == '__main__':
    binary, expected = tests[0]
    print(to_decimal(binary))
