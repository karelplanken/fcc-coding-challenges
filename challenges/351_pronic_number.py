# Daily Coding challenge #351 (2026-07-27) - freeCodeCamp.org
# Pronic Number
# Given a number, determine whether it is a pronic number.
#
# A pronic number is the product of two consecutive integers. For example, 6 is pronic
# because 2 * 3 = 6.
from pytest import mark


def is_pronic(n: int) -> bool:
    if n < 0:
        raise ValueError('n must be a non-negative integer')
    k = int(n**0.5)
    # k might be off by one due to float truncation, so check a small neighborhood
    return any(k_ * (k_ + 1) == n for k_ in (k - 1, k, k + 1))


# Alternative using number theory:
# from math import isqrt
# def is_pronic(n: int) -> bool:
#     """Determine whether n is a pronic number: k * (k + 1) for some integer k >= 0.

#     Args:
#         n: non-negative integer to test.

#     Returns:
#         True if n is pronic, else False.

#     Raises:
#         ValueError: if n is negative.
#     """
#     if n < 0:
#         raise ValueError('n must be a non-negative integer')
#     # n is pronic iff n == k*(k+1) for some integer k >= 0.
#     # Since k^2 <= k*(k+1) < (k+1)^2,
#     # k is pinned down exactly as isqrt(n) (no off-by-one risk, unlike float sqrt) —
#     # so it's enough to check n == isqrt(n) * (isqrt(n) + 1).
#     k = isqrt(n)
#     k = isqrt(n)
#     return n == k * (k + 1)


tests = [
    (6, True),
    (15, False),
    (12, True),
    (132, True),
    (80, False),
    (0, True),
]


@mark.parametrize('n, expected', tests)
def test_is_pronic(n: int, expected: bool) -> None:
    assert is_pronic(n) == expected


if __name__ == '__main__':
    n, expected = tests[0]
    print(is_pronic(n))
