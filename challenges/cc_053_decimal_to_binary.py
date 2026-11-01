"""Daily Coding Challenge #53 (2025-10-02) - freeCodeCamp.org."""

# Decimal to Binary
# Given a non-negative integer, return its binary representation as a string.
#
# A binary decimal uses only the digits 0 and 1 to represent any decimal. To convert a
# decimal decimal to binary, repeatedly divide the decimal by 2 and record the
# remainder.
# Repeat until the decimal is zero. Read the remainders last recorded to first. For
# example, to convert 12 to binary:
#
# mathml
# 12 ÷ 2 = 6 remainder 0
# 6 ÷ 2 = 3 remainder 0
# 3 ÷ 2 = 1 remainder 1
# 1 ÷ 2 = 0 remainder 1
#
# 12 in binary is 1100.
from pytest import mark


def to_binary(decimal: int) -> str:
    """Convert a non-negative integer to its binary string representation.

    Args:
        decimal: A non-negative integer.

    Returns:
        The binary string representation of the input integer.

    Raises:
        ValueError: If the input integer is negative.
    """
    if decimal < 0:
        msg = f'input must be a non-negative integer, got {decimal}'
        raise ValueError(msg)

    if decimal == 0:
        return '0'

    # format(decimal, 'b') is the production answer (linear, runs in C);
    # the challenge asks for the algorithm, so it is implemented manually.
    digits: list[str] = []
    while decimal:
        digits.append('1' if decimal & 1 else '0')
        decimal >>= 1

    return ''.join(reversed(digits))


tests = [
    (5, '101'),
    (12, '1100'),
    (50, '110010'),
    (99, '1100011'),
]


@mark.parametrize('decimal, expected', tests)
def test_to_binary(decimal: int, expected: str) -> None:
    """Test to_binary function."""
    assert to_binary(decimal) == expected


if __name__ == '__main__':
    binary, expected = tests[0]
    print(to_binary(binary))
