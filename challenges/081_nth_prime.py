# Daily Coding challenge #81 (2025-10-30) - freeCodeCamp.org
# Nth Prime
# A prime number is a positive integer greater than 1 that is divisible only by 1 and
# itself. The first five prime numbers are 2, 3, 5, 7, and 11.

# Given a positive integer n, return the nth prime number. For example, given 5 return
# the 5th prime number: 11.
from pytest import mark


def is_prime(k: int) -> bool:
    if k <= 1:
        return False
    if k == 2:
        return True
    if k % 2 == 0:
        return False
    if k == 3:
        return True
    if k % 3 == 0:
        return False

    # Check divisors of form 6k±1 up to √k
    i = 5
    while i * i <= k:
        if k % i == 0 or k % (i + 2) == 0:
            return False
        i += 6
    return True


def nth_prime(n: int) -> int:
    if n == 1:
        return 2

    count = 1  # We've already counted 2
    candidate = 3

    while count < n:
        if is_prime(candidate):
            count += 1
        if count < n:  # Only increment if we haven't found it yet
            candidate += 2  # Skip even numbers

    return candidate


tests = [
    (5, 11),
    (10, 29),
    (16, 53),
    (99, 523),
    (1000, 7919),
]


@mark.parametrize('n, expected', tests)
def test_nth_prime(n: int, expected: int) -> None:
    assert nth_prime(n) == expected


if __name__ == '__main__':
    n, expected = tests[3]
    print(nth_prime(n))
