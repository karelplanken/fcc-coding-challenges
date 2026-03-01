# Daily Coding challenge #156 (2026-01-13) - freeCodeCamp.org
# Odd or Even?
# Given a positive integer, return "Odd" if it's an odd number, and "Even" is it's even.
from pytest import mark


def odd_or_even(n: int) -> str:
    return 'Even' if n % 2 == 0 else 'Odd'


tests = [
    (1, 'Odd'),
    (2, 'Even'),
    (13, 'Odd'),
    (196, 'Even'),
    (123456789, 'Odd'),
]


@mark.parametrize('n, expected', tests)
def test_odd_or_even(n: int, expected: str) -> None:
    assert odd_or_even(n) == expected


if __name__ == '__main__':
    n, expected = tests[0]
    print(odd_or_even(n))
