# Daily Coding challenge #45 (2025-09-24) - freeCodeCamp.org
# Perfect Square
# Given an integer, determine if it is a perfect square.

# A number is a perfect square if you can multiply an integer by itself to achieve the
# number. For example, 9 is a perfect square because you can multiply 3 by itself to
# get it.
# Refactor 2: One-liner with short-circuit evaluation
import math

from pytest import mark


def is_perfect_square(n: int) -> bool:
    return n >= 0 and int(math.sqrt(n)) ** 2 == n


# Using integer square root for better precision
# def is_perfect_square(n: int) -> bool:
#     if n < 0:
#         return False
#     root = int(math.sqrt(n))
#     return root * root == n


# Newton's method for integer square root (most efficient)
# def is_perfect_square(n: int) -> bool:
#     if n < 0:
#         return False
#     if n < 2:
#         return True

#     # Newton's method to find integer square root
#     x = n
#     while True:
#         y = (x + n // x) // 2
#         if y >= x:
#             return x * x == n
#         x = y

tests = [
    (9, True),
    (49, True),
    (1, True),
    (2, False),
    (99, False),
    (-9, False),
    (0, True),
    (25281, True),
]


@mark.parametrize('n, expected', tests)
def test_is_perfect_square(n: int, expected: bool) -> None:
    assert is_perfect_square(n) == expected


if __name__ == '__main__':
    n, expected = tests[0]
    print(is_perfect_square(n))
