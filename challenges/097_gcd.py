# Daily Coding challenge #97 (2025-11-15) - freeCodeCamp.org
# GCD
# Given two positive integers, return their greatest common divisor (GCD).

# The GCD of two integers is the largest number that divides evenly into both numbers
# without leaving a remainder.
# For example, the divisors of 4 are 1, 2, and 4. The divisors of 6 are 1, 2, 3, and 6.
# So given 4 and 6, return 2, the largest number that appears in both sets of divisors.
from pytest import mark


def gcd(x: int, y: int) -> int:
    """Return the greatest common divisor using Euclidean algorithm."""
    while y != 0:
        x, y = y, x % y
    return x

# def gcd(a: int, b: int) -> int:
#     """Return the greatest common divisor using Euclidean algorithm."""
#     while b:
#         a, b = b, a % b
#     return a

# def gcd(x: int, y: int) -> int:
#     # Pre-sorting is unnecessary because Euclidean algorithm works regardless
#     # of input order
#     small, large = (x, y) if y > x else (y, x)

#     while small != 0:
#         large, small = small, large % small

#     return large

tests = [
    (4, 6, 2),
    (20, 15, 5),
    (13, 17, 1),
    (654, 456, 6),
    (3456, 4320, 864),
]


@mark.parametrize(('x', 'y', 'expected'), tests)
def test_gcd(x: int, y: int, expected: int) -> None:
    assert gcd(x, y) == expected


if __name__ == '__main__':
    x, y, expected = tests[4]
    print(gcd(x, y))
