# Daily Coding challenge #152 (2026-01-09) - freeCodeCamp.org
# Circular Prime
# Given an integer, determine if it is a circular prime.

# A circular prime is an integer where all rotations of its digits are themselves prime.

# For example, 197 is a circular prime because all rotations of its digits: 197, 971,
# and 719, are prime numbers.
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


def get_rotations(n: int) -> list[int]:
    s = str(n)
    return [int(s[i:] + s[:i]) for i in range(len(s))]


def is_circular_prime(n: int) -> bool:
    if n <= 1:
        return False

    rotations = get_rotations(n)
    return all(map(is_prime, rotations))


tests = [
    (197, True),
    (23, False),
    (13, True),
    (89, False),
    (1193, True),
]


@mark.parametrize(('n', 'expected'), tests)
def test_is_circular_prime(n: int, expected: bool) -> None:
    assert is_circular_prime(n) == expected


if __name__ == '__main__':
    n, expected = tests[0]
    print(is_circular_prime(n))
