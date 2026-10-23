"""Daily Coding Challenge #81 (2025-10-30) - freeCodeCamp.org."""

# Nth Prime
# A prime number is a positive integer greater than 1 that is divisible only by 1 and
# itself. The first five prime numbers are 2, 3, 5, 7, and 11.
#
# Given a positive integer n, return the nth prime number. For example, given 5 return
# the 5th prime number: 11.
from itertools import count, islice

from pytest import mark


def _is_prime(k: int) -> bool:
    """Return True if k is prime, using 6k±1 trial division."""
    if k <= 3:
        return k >= 2
    if k % 2 == 0 or k % 3 == 0:
        return False
    i = 5
    while i * i <= k:
        if k % i == 0 or k % (i + 2) == 0:
            return False
        i += 6
    return True


def nth_prime(n: int) -> int:
    """Return the nth prime number (1-based).

    Args:
        n: The index of the prime number to return.

    Returns:
        The nth prime number.

    Raises:
        ValueError: If n is not a positive integer.
    """
    if n <= 0:
        msg = f'expected a positive integer, got {n}'
        raise ValueError(msg)
    if n == 1:
        return 2
    odd_primes = (k for k in count(3, 2) if _is_prime(k))
    return next(islice(odd_primes, n - 2, None))


tests = [
    (5, 11),
    (10, 29),
    (16, 53),
    (99, 523),
    (1000, 7919),
]


@mark.parametrize('n, expected', tests)
def test_nth_prime(n: int, expected: int) -> None:
    """Test nth_prime function."""
    assert nth_prime(n) == expected


if __name__ == '__main__':
    n, expected = tests[0]
    print(nth_prime(n))
