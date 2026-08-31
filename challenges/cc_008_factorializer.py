"""Daily Coding Challenge #8 (2025-08-18) - freeCodeCamp.org."""

# Factorializer
# Given an integer from zero to 20, return the factorial of that number. The factorial
# of a number is the product of all the numbers between 1 and the given number.
#
# - The factorial of zero is 1.
from pytest import mark


def factorial(n: int) -> int:
    """Recursively calculate the factorial of a given integer.

    Args:
        n: The integer for which to calculate the factorial. Must be between 0 and 20.

    Returns:
        The factorial of the given integer.
    """
    if n == 0:
        return 1

    else:
        return n * factorial(n - 1)


# Most efficient (iterative approach)
def factorial_iterative(n: int) -> int:
    """Calculate the factorial of a given integer using an iterative approach.

    Args:
        n: The integer for which to calculate the factorial. Must be between 0 and 20.

    Returns:
        The factorial of the given integer.
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


tests = [(0, 1), (5, 120), (20, 2432902008176640000)]


@mark.parametrize('n, expected', tests)
def test_factorial_recursive(n: int, expected: int) -> None:
    """Test factorial function."""
    assert factorial(n) == expected


@mark.parametrize('n, expected', tests)
def test_factorial_iterative(n: int, expected: int) -> None:
    """Test factorial function."""
    assert factorial_iterative(n) == expected


if __name__ == '__main__':
    n, expected = tests[0]
    print(factorial(n))
