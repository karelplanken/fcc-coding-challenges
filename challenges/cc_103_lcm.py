"""Daily Coding Challenge #103 (2025-11-21) - freeCodeCamp.org."""

# LCM
# Given two integers, return the least common multiple (LCM) of the two numbers.
#
# The LCM of two numbers is the smallest positive integer that is a multiple of both
# numbers. For example, given 4 and 6, return 12 because:
#
# - Multiples of 4 are 4, 8, 12 and so on.
# - Multiples of 6 are 6, 12, 18 and so on.
# - 12 is the smallest number that is a multiple of both.
from pytest import mark


def _gcd(a: int, b: int) -> int:
    """Return the greatest common divisor using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Return the least common multiple of two integers.

    The result is always non-negative. By convention, the LCM is 0 if
    either argument is 0.

    Args:
        a: The first integer.
        b: The second integer.

    Returns:
        The least common multiple of a and b.
    """
    # Implemented by hand rather than with math.lcm/math.gcd, as the point of the
    # challenge.
    if a == 0 or b == 0:
        return 0
    return abs(a // _gcd(a, b) * b)  # divide first to keep the intermediate small


tests = [
    (4, 6, 12),
    (9, 6, 18),
    (10, 100, 100),
    (13, 17, 221),
    (45, 70, 630),
]


@mark.parametrize(('a', 'b', 'expected'), tests)
def test_lcm(a: int, b: int, expected: int) -> None:
    """Test lcm function."""
    assert lcm(a, b) == expected


if __name__ == '__main__':
    a, b, expected = tests[0]
    print(lcm(a, b))
