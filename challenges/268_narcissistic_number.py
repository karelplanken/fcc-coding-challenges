# Daily Coding challenge #268 (2026-05-05) - freeCodeCamp.org
# Narcissistic Number
# Given a positive integer, determine whether it is a narcissistic number.

# A number is narcissistic if the sum of each of its digits raised to the power of the
# total number of digits equals the number itself.
# For example, 153 has 3 digits, and 1^3 + 5^3 + 3^3 = 153, so it is narcissistic.
from typing import cast

from pytest import mark


def is_narcissistic(n: int) -> bool:
    digits = str(n)
    exponent = len(digits)
    # builtins.pyi (typeshed) deliberately types int.__pow__(int) -> Any in the
    # general-int overload to avoid false positives from the int|float ambiguity
    # (a negative exponent yields float). mypy --strict then propagates that Any
    # through sum(), triggering [no-any-return]. cast(int, ...) is the intended
    # workaround: see https://github.com/python/typeshed/issues/13253
    print(type(sum(int(digit) ** exponent for digit in digits)))
    return sum(cast(int, int(digit) ** exponent) for digit in digits) == n


tests = [
    (153, True),
    (154, False),
    (371, True),
    (512, False),
    (9, True),
    (11, False),
    (9474, True),
    (6549, False),
]


@mark.parametrize('n, expected', tests)
def test(n: int, expected: bool) -> None:
    assert is_narcissistic(n) == expected


if __name__ == '__main__':
    n, expected = tests[1]
    print(is_narcissistic(n))
