"""Daily Coding Challenge #45 (2025-09-24) - freeCodeCamp.org."""

# Perfect Square
# Given an integer, determine if it is a perfect square.
#
# - A number is a perfect square if you can multiply an integer by itself to achieve the
#   number. For example, 9 is a perfect square because you can multiply 3 by itself to
#   get it.
import math

from pytest import mark


def is_perfect_square(n: int) -> bool:
    """Determine if n is a perfect square.

    Uses exact integer arithmetic, so it is correct for arbitrarily large n.
    Non-integer input (including floats and None) raises a TypeError.

    Args:
        n: The integer to check.

    Returns:
        True if n is a perfect square, False otherwise.
    """
    if n < 0:
        return False
    root = math.isqrt(n)
    return root * root == n


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
    """Test is_perfect_square function."""
    assert is_perfect_square(n) == expected


if __name__ == '__main__':
    n, expected = tests[0]
    print(is_perfect_square(n))
