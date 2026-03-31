# Daily Coding challenge #205 (2026-03-03) - freeCodeCamp.org
# Perfect Cube Count
# Given two integers, determine how many perfect cubes exist in the range between and
# including the two numbers.

# The lower number is not garanteed to be the first argument.
# A number is a perfect cube if there exists an integer (n) where n * n * n = number.
# For example, 27 is a perfect cube because 3 * 3 * 3 = 27.
import math

from pytest import mark


def icbrt(n: int) -> int:
    """Integer cube root, works for negative numbers."""
    if n < 0:
        return -icbrt(-n)
    
    # Initial guess using floating point cube root
    # r = round(n ** (1 / 3))
    
    # Use math.cbrt for better accuracy
    r = int(math.cbrt(n))
    
    # Correct for floating point drift near the boundary
    while (r + 1) ** 3 <= n:
        r += 1
    while r**3 > n:
        r -= 1
    return r


def count_perfect_cubes(a: int, b: int) -> int:
    start, end = min(a, b), max(a, b)
    # Find the smallest n where n³ >= start
    n_min = icbrt(start)
    if n_min**3 < start:
        n_min += 1
    # Find the largest n where n³ <= end
    n_max = icbrt(end)
    return max(0, n_max - n_min + 1)


tests = [
    (3, 30, 2),
    (1, 30, 3),
    (30, 0, 4),
    (-64, 64, 9),
    (9214, -8127, 41),
]


@mark.parametrize('a, b, expected', tests)
def test(a: int, b: int, expected: int) -> None:
    assert count_perfect_cubes(a, b) == expected


if __name__ == '__main__':
    a, b, expected = tests[4]
    print(count_perfect_cubes(a, b))
