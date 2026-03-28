# Daily Coding challenge #230 (2026-03-28) - freeCodeCamp.org
# Pascal's Triangle Row
# Given an integer n, return the nth row of Pascal's triangle as an array.

# In Pascal's Triangle, each row begins and ends with 1, and each interior value is the
# sum of the two values directly above it.

# Here's the first 5 rows of the triangle:

#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
from itertools import pairwise

from pytest import mark


# Iterative loop solution:
def pascal_row(n: int) -> list[int]:
    row = [1]
    for _ in range(n - 1):
        row = [1, *(a + b for a, b in pairwise(row)), 1]
    return row

# Recursive solution, which is not very efficient but straightforward:
# def pascal_row(n: int) -> list[int]:
#     if n == 1:
#         return [1]
    
#     prev_row = pascal_row(n - 1)
#     row = [1]
#     for a, b in pairwise(prev_row):
#         row.append(a + b)
#     row.append(1)

#     return row


tests = [
    (5, [1, 4, 6, 4, 1]),
    (3, [1, 2, 1]),
    (1, [1]),
    (10, [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]),
    (15, [1, 14, 91, 364, 1001, 2002, 3003, 3432, 3003, 2002, 1001, 364, 91, 14, 1]),
]


@mark.parametrize('n, expected', tests)
def test_solution(n: int, expected: list[int]) -> None:
    assert pascal_row(n) == expected


if __name__ == '__main__':
    n, expected = tests[4]
    print(pascal_row(n))
