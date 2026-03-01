# Daily Coding challenge #13 (2025-08-23) - freeCodeCamp.org
# Unnatural Prime
# Given an integer, determine if that number is a prime number or a negative
# prime number.

# A prime number is a positive integer greater than 1 that is only divisible by 1
# and itself.
# A negative prime number is the negative version of a positive prime number.
# 1 and 0 are not considered prime numbers.
from pytest import mark


def is_unnatural_prime(n: int) -> bool:
    n_abs = abs(n)

    if n_abs <= 1:
        return False

    if n_abs <= 3:
        return True

    if n_abs % 2 == 0 or n_abs % 3 == 0:
        return False

    # Check for divisors of form 6k±1 up to sqrt(n)
    i = 5
    while i * i <= n_abs:
        if n_abs % i == 0 or n_abs % (i + 2) == 0:
            return False
        i += 6

    return True


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
    assert is_unnatural_prime(n) == expected


if __name__ == '__main__':
    n, expected = tests[0]
    print(is_unnatural_prime(n))
