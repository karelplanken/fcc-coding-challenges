# Daily Coding challenge #8 (2025-08-18) - freeCodeCamp.org
# Factorializer
# Given an integer from zero to 20, return the factorial of that number. The factorial
# of a number is the product of all the numbers between 1 and the given number.
# The factorial of zero is 1.
from pytest import mark


def factorial(n: int) -> int:
    if n == 0:
        return 1

    else:
        return n * factorial(n - 1)


# Most efficient (iterative approach)
# def factorial(n: int) -> int:
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

tests = [(0, 1), (5, 120), (20, 2432902008176640000)]


@mark.parametrize('n, expected', tests)
def test_factorial(n: int, expected: int) -> None:
    assert factorial(n) == expected


if __name__ == '__main__':
    n, expected = tests[0]
    print(factorial(n))
