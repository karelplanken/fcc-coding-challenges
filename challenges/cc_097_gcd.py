"""Daily Coding Challenge #97 (2025-11-15) - freeCodeCamp.org."""

# GCD
# Given two positive integers, return their greatest common divisor (GCD).
#
# - The GCD of two integers is the largest number that divides evenly into both numbers
#   without leaving a remainder.
#
# For example, the divisors of 4 are 1, 2, and 4. The divisors of 6 are 1, 2, 3, and 6.
# So given 4 and 6, return 2, the largest number that appears in both sets of divisors.
from pytest import mark


def gcd(x: int, y: int) -> int:
    """Return the greatest common divisor using Euclidean algorithm.

    Args:
        x: first integer
        y: second integer

    Returns:
        The greatest common divisor of ``x`` and ``y``.
    """
    while y != 0:
        x, y = y, x % y
    return x


tests = [
    (4, 6, 2),
    (20, 15, 5),
    (13, 17, 1),
    (654, 456, 6),
    (3456, 4320, 864),
]


@mark.parametrize(('x', 'y', 'expected'), tests)
def test_gcd(x: int, y: int, expected: int) -> None:
    """Test gcd function."""
    assert gcd(x, y) == expected


if __name__ == '__main__':
    # x, y, expected = tests[0]
    # print(gcd(x, y))
    print(gcd(10, 0))
