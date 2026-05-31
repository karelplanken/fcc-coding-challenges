# Daily Coding challenge #294 (2026-05-31) - freeCodeCamp.org
# Parentheses Combinations
# Given an integer, n, return the number of valid combinations of n pairs of
# parentheses.
# A valid combination is a string where every opening parentheses has a corresponding
# closing parentheses, and no closing parentheses appears before its matching opening
# parentheses. For example, given 2, there are 2 valid combinations:
# (())
# ()()
from functools import cache
from math import comb

from pytest import mark


# Option A: Direct closed-form formula
def get_combinations(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


# Option B: Recursive with memoization (mirrors the reasoning)
def get_combinations_recursively(n: int) -> int:
    @cache
    def catalan(k: int) -> int:
        if k == 0:
            return 1
        return sum(catalan(i) * catalan(k - 1 - i) for i in range(k))

    return catalan(n)


tests = [
    (2, 2),
    (3, 5),
    (5, 42),
    (8, 1430),
    (13, 742900),
]


@mark.parametrize('n, expected', tests)
def test_get_combinations(n: int, expected: int) -> None:
    assert get_combinations(n) == expected


@mark.parametrize('n, expected', tests)
def test_get_combinations_recursively(n: int, expected: int) -> None:
    assert get_combinations_recursively(n) == expected

if __name__ == '__main__':
    n, expected = tests[0]
    print(get_combinations(n))
