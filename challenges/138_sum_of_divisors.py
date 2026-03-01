# Daily Coding challenge #138 (2025-12-26) - freeCodeCamp.org
# Sum of Divisors
# Given a positive integer, return the sum of all its divisors.

# A divisor is any integer that divides the number evenly (the remainder is 0).
# Only count each divisor once.
# For example, given 6, return 12 because the divisors of 6 are 1, 2, 3, and 6, and the
# sum of those is 12.
from pytest import mark

# Checks every number from 1 to n (inefficient)
# def sum_divisors(n: int) -> int:
#     return sum(i for i in range(1, n + 1) if n % i == 0)


# Optimized version that's much faster:
def sum_divisors(n: int) -> int:
    """Find sum of divisors by checking only up to sqrt(n)."""
    if n == 1:
        return 1

    total = 0
    i = 1

    # Only check divisors up to sqrt(n)
    while i * i <= n:
        if n % i == 0:
            total += i
            # Add the corresponding divisor (n // i) if it's different
            if i != n // i:
                total += n // i
        i += 1

    return total


tests = [
    (6, 12),
    (13, 14),
    (28, 56),
    (84, 224),
    (549, 806),
    (9348, 23520),
]


@mark.parametrize('n, expected', tests)
def test_sum_divisors(n: int, expected: int) -> None:
    assert sum_divisors(n) == expected


if __name__ == '__main__':
    n, expected = tests[5]
    print(sum_divisors(n))
