# Daily Coding challenge #159 (2026-01-16) - freeCodeCamp.org
# Integer Hypotenuse
# Given two positive integers representing the lengths for the two legs
# (the two short sides) of a right triangle, determine whether the hypotenuse is
# an integer.

# The length of the hypotenuse is calculated by adding the squares of the two leg
# lengths together and then taking the square root of that total (a^2 + b^2 = c^2).
import math

from pytest import mark


def is_integer_hypotenuse(a: int, b: int) -> bool:
    hypotenuse_squared = a**2 + b**2
    hypotenuse = math.isqrt(hypotenuse_squared)
    return hypotenuse**2 == hypotenuse_squared


tests = [
    (3, 4, True),
    (2, 3, False),
    (5, 12, True),
    (10, 10, False),
    (780, 1040, True),
    (250, 333, False),
]


@mark.parametrize('a, b, expected', tests)
def test_is_integer_hypotenuse(a: int, b: int, expected: bool) -> None:
    assert is_integer_hypotenuse(a, b) == expected


if __name__ == '__main__':
    a, b, expected = tests[0]
    print(is_integer_hypotenuse(a, b))
