# Daily Coding challenge #10 (2025-08-20) - freeCodeCamp.org
# 3 Strikes
# Given an integer between 1 and 10,000, return a count of how many numbers from 1 up
# to that integer whose square contains at least one digit 3.
# def squares_with_three(n: int) -> int:
#     return sum(1 for i in range(1, n) if '3' in str(i * i))
from pytest import mark


def squares_with_three(n: int) -> int:
    return sum('3' in str(i * i) for i in range(1, n))


tests = [(1, 0), (10, 1), (100, 19), (1000, 326), (10000, 4531)]


@mark.parametrize('n, expected', tests)
def test_squares_with_three(n: int, expected: int) -> None:
    assert squares_with_three(n) == expected


if __name__ == '__main__':
    n, expected = tests[0]
    print(squares_with_three(n))
