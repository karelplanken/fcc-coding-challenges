"""Daily Coding Challenge #344 (2026-07-20) - freeCodeCamp.org."""

# Golden Ratio
# Given two numbers, determine if their ratio approximates the golden ratio.
#
# - Use a golden ratio of `1.618`
# - Allow a tolerance of `0.01`
from math import isclose, sqrt

from pytest import mark

GOLDEN_RATIO = (1 + sqrt(5)) / 2
ABS_TOL = 0.01
RE_TOL = 0.0


def is_golden_ratio(a: int, b: int) -> bool:
    """Returns whether the ratio of a and b falls in the range of golden ratio.
    
    The ratio from large over small from a and b is compared to the golden ratio 
    (GOLDEN_RATIO) +/- tolerance (TOLERANCE), both defined as global constants, 
    irrespective of params order.

    The golden ratio, assigned to the constant GOLDEN_RATIO, is calculated from an
    analytical expression because that shows its origin unlike a magic floating point
    number.

    Args:
        a: integer value
        b: integer value

    Returns:
        True if a / b or b / a falls in the range else False
    """
    if a <= 0 or b <= 0:
        return False

    smaller, larger = (a, b) if a < b else (b, a)
    return isclose(larger / smaller, GOLDEN_RATIO, rel_tol=RE_TOL, abs_tol=ABS_TOL)


tests = [
    (21, 34, True),
    (15, 20, False),
    (8, 13, True),
    (10, 16, False),
    (1618, 1000, True),
    (88, 55, False),
]


@mark.parametrize('a, b, expected', tests)
def test_is_golden_ratio(a: int, b: int, expected: bool) -> None:
    """Test is_golden_ratio function."""
    assert is_golden_ratio(a, b) == expected


if __name__ == '__main__':
    a, b, expected = tests[4]
    print(is_golden_ratio(a, b))
