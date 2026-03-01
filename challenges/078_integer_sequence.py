# Daily Coding challenge #78 (2025-10-27) - freeCodeCamp.org
# Integer Sequence
# Given a positive integer, return a string with all of the integers from 1 up to, and
# including, the given number, in numerical order.

# For example, given 5, return "12345".
from pytest import mark


def sequence(n: int) -> str:
    return ''.join(map(str, range(1, n + 1)))


tests = [
    (5, '12345'),
    (10, '12345678910'),
    (1, '1'),
    (27, '123456789101112131415161718192021222324252627'),
]


@mark.parametrize('n, expected', tests)
def test_sequence(n: int, expected: str) -> None:
    assert sequence(n) == expected


if __name__ == '__main__':
    n, expected = tests[0]
    print(sequence(n))
