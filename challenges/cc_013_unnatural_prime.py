"""Daily Coding Challenge #13 (2025-08-23) - freeCodeCamp.org."""

# Unnatural Prime
# Given an integer, determine if that number is a prime number or a negative prime
# number.
#
# - A prime number is a positive integer greater than 1 that is only divisible by 1 and
#   itself.
# - A negative prime number is the negative version of a positive prime number.
# - 1 and 0 are not considered prime numbers.
from math import isqrt

from pytest import mark


def is_prime(n: int) -> bool:
    """Computes whether a given integer is a prime number.

    Args:
        n: Integer to check for primality.

    Returns:
        True if n is a prime number, False otherwise.
    """
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    return all(n % i for i in range(5, isqrt(n) + 1, 2) if i % 3 != 0)


def is_unnatural_prime(n: int) -> bool:
    """Computes whether n or -n is a prime number.

    Args:
        n: An integer to check for primality.

    Returns:
        True if n is a prime number or a negative prime number, False otherwise.
    """
    return is_prime(abs(n))


# Test cases
tests = [
    (1, False),
    (-1, False),
    (19, True),
    (-23, True),
    (0, False),
    (97, True),
    (-61, True),
    (99, False),
    (-44, False),
    # Additional edge cases
    (5, True),
    (-5, True),
    (25, False),  # 5 × 5
    (49, False),  # 7 × 7
    (121, False),  # 11 × 11
    (2, True),
    (-2, True),
    (3, True),
    (-3, True),
]


@mark.parametrize('n, expected', tests)
def test_is_unnatural_prime(n: int, expected: bool) -> None:
    """Test is_unnatural_prime function."""
    assert is_unnatural_prime(n) == expected


if __name__ == '__main__':
    n, expected = tests[0]
    print(is_unnatural_prime(n))
