"""Daily Coding Challenge #10 (2025-08-20) - freeCodeCamp.org."""

# 3 Strikes
# Given an integer between 1 and 10,000, return a count of how many numbers from 1 up to
# that integer whose square contains at least one digit 3.
from pytest import mark


def squares_with_three(n: int) -> int:
    """Counts how many squares from 1 to n contain the digit '3'.

    Args:
        n: An integer between 1 and 10,000.

    Returns:
        The count of numbers from 1 to n whose square contains at least one digit '3'.

    Raises:
        ValueError: If n is outside the valid range.
    """
    if not 1 <= n <= 10_000:
        msg = 'input must be between 1 and 10,000'
        raise ValueError(msg)
    return sum('3' in str(i * i) for i in range(1, n))


tests = [(1, 0), (10, 1), (100, 19), (1000, 326), (10000, 4531)]


@mark.parametrize('n, expected', tests)
def test_squares_with_three(n: int, expected: int) -> None:
    """Test squares_with_three function."""
    assert squares_with_three(n) == expected


if __name__ == '__main__':
    n, expected = tests[0]
    print(squares_with_three(n))
