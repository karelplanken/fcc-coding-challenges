"""Daily Coding Challenge #9 (2025-08-19) - freeCodeCamp.org."""

# Sum of Squares
# Given a positive integer up to 1,000, return the sum of all the integers squared from
# 1 up to the number.
from pytest import mark


def sum_of_squares(n: int) -> int:
    """Calculates the sum of squares from 1 to n.

    Uses the mathematical formula for the sum of squares, which is faster than
    iterating over each number, squaring it, and adding the results.

    Args:
        n: A positive integer up to 1,000.

    Returns:
        The sum of squares from 1 to n.
    """
    return n * (n + 1) * (2 * n + 1) // 6


tests = [(5, 55), (10, 385), (25, 5525), (500, 41791750), (1000, 333833500)]


@mark.parametrize('n, expected', tests)
def test_sum_of_squares(n: int, expected: int) -> None:
    """Test sum_of_squares function."""
    assert sum_of_squares(n) == expected


if __name__ == '__main__':
    n, expected = tests[0]
    print(sum_of_squares(n))
