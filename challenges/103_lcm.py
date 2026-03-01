# Daily Coding challenge #103 (2025-11-21) - freeCodeCamp.org
# LCM
# Given two integers, return the least common multiple (LCM) of the two numbers.

# The LCM of two numbers is the smallest positive integer that is a multiple of both
# numbers. For example, given 4 and 6, return 12 because:

# Multiples of 4 are 4, 8, 12 and so on.
# Multiples of 6 are 6, 12, 18 and so on.
# 12 is the smallest number that is a multiple of both.
from pytest import mark


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)


tests = [
    (4, 6, 12),
    (9, 6, 18),
    (10, 100, 100),
    (13, 17, 221),
    (45, 70, 630),
]


@mark.parametrize(('a', 'b', 'expected'), tests)
def test_lcm(a: int, b: int, expected: int) -> None:
    assert lcm(a, b) == expected


if __name__ == '__main__':
    a, b, expected = tests[0]
    print(lcm(a, b))
