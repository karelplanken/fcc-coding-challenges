# Daily Coding challenge #218 (2026-03-16) - freeCodeCamp.org
# Evenly Divisible
# Given two integers, determine if you can evenly divide the first one by the second
# one.
from pytest import mark


def is_evenly_divisible(a: int, b: int) -> bool:
    return b != 0 and a % b == 0


tests = [
    (4, 2, True),
    (7, 3, False),
    (5, 10, False),
    (48, 6, True),
    (3186, 9, True),
    (4192, 11, False),
]


@mark.parametrize('a, b, expected', tests)
def test_is_evenly_divisible(a: int, b: int, expected: bool) -> None:
    assert is_evenly_divisible(a, b) == expected


if __name__ == '__main__':
    a, b, expected = tests[0]
    print(is_evenly_divisible(a, b))
