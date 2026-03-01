# Daily Coding challenge #145 (2026-01-02) - freeCodeCamp.org
# Nth Fibonacci Number
# Given an integer n, return the nth number in the fibonacci sequence.

# The Fibonacci sequence is a series of numbers where each number is the sum of the two
# preceding ones. The first 10 numbers in the sequence
# are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
from pytest import mark


def nth_fibonacci(n: int) -> int:
    if n <= 2:
        return n - 1  # Returns 0 for n=1, 1 for n=2

    prev, curr = 0, 1
    for _ in range(n - 2):
        prev, curr = curr, prev + curr

    return curr


tests = [
    (4, 2),
    (10, 34),
    (15, 377),
    (40, 63245986),
    (75, 1304969544928657),
]


@mark.parametrize(('n', 'expected'), tests)
def test_nth_fibonacci(n: int, expected: int) -> None:
    assert nth_fibonacci(n) == expected


if __name__ == '__main__':
    n, expected = tests[4]
    print(nth_fibonacci(n))
