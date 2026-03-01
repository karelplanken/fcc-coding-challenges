# Daily Coding challenge #107 (2025-11-25) - freeCodeCamp.org
# FizzBuzz

# Given an integer (n), return an array of integers from 1 to n (inclusive), replacing
# numbers that are multiple of:

# 3 with "Fizz".
# 5 with "Buzz".
# 3 and 5 with "FizzBuzz".
from pytest import mark


def fizz_buzz(number: int) -> list[str | int]:
    return [
        'FizzBuzz'
        if num % 15 == 0
        else 'Fizz'
        if num % 3 == 0
        else 'Buzz'
        if num % 5 == 0
        else num
        for num in range(1, number + 1)
    ]


tests = [
    (2, [1, 2]),
    (4, [1, 2, 'Fizz', 4]),
    (8, [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8]),
    (
        20,
        [
            1,
            2,
            'Fizz',
            4,
            'Buzz',
            'Fizz',
            7,
            8,
            'Fizz',
            'Buzz',
            11,
            'Fizz',
            13,
            14,
            'FizzBuzz',
            16,
            17,
            'Fizz',
            19,
            'Buzz',
        ],
    ),
    (
        50,
        [
            1,
            2,
            'Fizz',
            4,
            'Buzz',
            'Fizz',
            7,
            8,
            'Fizz',
            'Buzz',
            11,
            'Fizz',
            13,
            14,
            'FizzBuzz',
            16,
            17,
            'Fizz',
            19,
            'Buzz',
            'Fizz',
            22,
            23,
            'Fizz',
            'Buzz',
            26,
            'Fizz',
            28,
            29,
            'FizzBuzz',
            31,
            32,
            'Fizz',
            34,
            'Buzz',
            'Fizz',
            37,
            38,
            'Fizz',
            'Buzz',
            41,
            'Fizz',
            43,
            44,
            'FizzBuzz',
            46,
            47,
            'Fizz',
            49,
            'Buzz',
        ],
    ),
]


@mark.parametrize('number,expected', tests)
def test_fizz_buzz(number: int, expected: list[str | int]) -> None:
    assert fizz_buzz(number) == expected


if __name__ == '__main__':
    number, expected = tests[0]
    print(fizz_buzz(number))
