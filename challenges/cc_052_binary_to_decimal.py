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
    """Convert a binary string to its decimal equivalent.

    Uses Horner's method: scan left to right, doubling the running total (a left shift)
    and adding each bit. Equivalent to summing bit * 2**k, without computing powers.

    Args:
        binary: A non-empty string consisting only of '0' and '1'.

    Returns:
        The decimal equivalent of the binary number.

    Raises:
        ValueError: If the binary string is empty or contains any characters other than
            '0' or '1'.
    """
    if not binary or binary.strip('01'):
        msg = f'invalid binary string: {binary!r}'
        raise ValueError(msg)

    result = 0
    for bit in binary:
        result = (result << 1) | (bit == '1')

    return result


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
