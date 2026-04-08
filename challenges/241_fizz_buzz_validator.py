# Daily Coding challenge #241 (2026-04-08) - freeCodeCamp.org
# FizzBuzz Validator
# Given an array of sequential integers, with multiples of 3 and 5 replaced, determine
# if it's a valid FizzBuzz sequence.

# In a valid FizzBuzz sequence:

# Multiples of 3 are replaced with "Fizz".
# Multiples of 5 are replaced with "Buzz".
# Multiples of both 3 and 5 are replaced with "FizzBuzz".
# All other numbers remain as integers.
from pytest import mark


def _fizzbuzz(n: int) -> str | int:
    if n % 15 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    return n


def is_fizz_buzz(arr: list[int | str]) -> bool:
    anchor_idx, anchor_value = next(
        (i, value) for i, value in enumerate(arr) if isinstance(value, int)
    )
    start = anchor_value - anchor_idx

    return all(_fizzbuzz(start + i) == value for i, value in enumerate(arr))


tests: list[tuple[list[int | str], bool]] = [
    ([1, 2, 'Fizz', 4, 'Buzz'], True),
    ([13, 14, 'FizzBuzz', 16, 17], True),
    ([1, 2, 'Fizz', 4, 5], False),
    (['FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz'], True),
    ([1, 2, 'Fizz', 'Buzz', 5], False),
    ([97, 98, 'Buzz', 'Fizz', 101, 'Fizz', 103], False),
    (['Fizz', 'Buzz', 101, 'Fizz', 103, 104, 'FizzBuzz'], True),
]


@mark.parametrize('arr, expected', tests)
def test_is_fizz_buzz(arr: list[int | str], expected: bool) -> None:
    assert is_fizz_buzz(arr) == expected


if __name__ == '__main__':
    arr, expected = tests[0]
    print(is_fizz_buzz(arr))
