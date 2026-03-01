# Daily Coding challenge #169 (2026-01-26) - freeCodeCamp.org
# FizzBuzz Mini
# Given an integer, return a string based on the following rules:

# If the number is divisible by 3, return "Fizz".
# If the number is divisible by 5, return "Buzz".
# If the number is divisible by both 3 and 5, return "FizzBuzz".
# Otherwise, return the given number as a string.
from pytest import mark


def fizz_buzz_mini(n: int) -> str:
    result = ('Fizz' if n % 3 == 0 else '') + ('Buzz' if n % 5 == 0 else '')
    return result or str(n)


tests = [
    (3, 'Fizz'),
    (4, '4'),
    (35, 'Buzz'),
    (75, 'FizzBuzz'),
    (98, '98'),
]


@mark.parametrize('n,expected', tests)
def test_fizz_buzz_mini(n: int, expected: str) -> None:
    assert fizz_buzz_mini(n) == expected


if __name__ == '__main__':
    n, expected = tests[0]
    print(fizz_buzz_mini(n))
