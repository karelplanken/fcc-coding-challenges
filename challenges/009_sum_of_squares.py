# Daily Coding challenge #9 (2025-08-19) - freeCodeCamp.org
# Sum of Squares
# Given a positive integer up to 1,000, return the sum of all the integers squared
# from 1 up to the number.
from pytest import mark


def sum_of_squares(n: int) -> int:
    return sum(i * i for i in range(1, n + 1))


# Mathematical formula (faster)
# def sum_of_squares(n: int) -> int:
#     return n * (n + 1) * (2 * n + 1) // 6


tests = [(5, 55), (10, 385), (25, 5525), (500, 41791750), (1000, 333833500)]


@mark.parametrize('n, expected', tests)
def test_sum_of_squares(n: int, expected: int) -> None:
    assert sum_of_squares(n) == expected


if __name__ == '__main__':
    n, expected = tests[0]
    print(sum_of_squares(n))
