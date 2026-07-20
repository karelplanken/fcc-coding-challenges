# Daily Coding challenge #344 (2026-07-20) - freeCodeCamp.org
# Golden Ratio
# Given two numbers, determine if their ratio approximates the golden ratio.
#
# - Use a golden ratio of `1.618`
# - Allow a tolerance of `0.01`
from math import isclose, sqrt

from pytest import mark

GOLDEN_RATIO = (1 + sqrt(5)) / 2
TOLERANCE = 0.01


def is_golden_ratio(a: int, b: int) -> bool:
    """Returns whether the ratio of a and b falls in the range of golden (GOLDEN_RATIO)
    ratio +/- tolerance (TOLERANCE), both defined as global constants, irrespective of
    params order.

    Assumes that both params 'a' and 'b' are positive integers. The golden ratio is for
    the constant GOLDEN_RATIO is calculated exactly because it is fun, I'm a know it
    all, and I want to show off.

    Args:
        a: integer value
        b: integer value

    Returns:
        True if a / b or b / a falls in the range else False
    """
    smaller, larger = min(a, b), max(a, b)
    return isclose(larger / smaller, GOLDEN_RATIO, abs_tol=TOLERANCE)


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
    assert is_golden_ratio(a, b) == expected


if __name__ == '__main__':
    a, b, expected = tests[0]
    print(is_golden_ratio(a, b))
