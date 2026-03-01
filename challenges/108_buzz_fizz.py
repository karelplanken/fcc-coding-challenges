# Daily Coding challenge #108 (2025-11-26) - freeCodeCamp.org
# BuzzFizz

# Given an array, determine if it is a correct FizzBuzz sequence from 1 to the last
# item in the array. A sequence is correct if:

# Numbers that are multiples of 5 are replaced with "Buzz"
# Numbers that are multiples of 3 are replaced with "Fizz"
# Numbers that are multiples of both 3 and 5 are replaced with "FizzBuzz"
# All other numbers remain as integers in ascending order, starting from 1.
# The array must start at 1 and have no missing or extra elements.
from pytest import mark


def is_fizz_buzz(sequence: list[str | int]) -> bool:
    return all(
        actual
        == (
            'FizzBuzz'
            if i % 15 == 0
            else 'Fizz'
            if i % 3 == 0
            else 'Buzz'
            if i % 5 == 0
            else i
        )
        for i, actual in enumerate(sequence, start=1)
    )


tests = [
    ([1, 2, 'Fizz', 4], True),
    ([1, 2, 3, 4], False),
    ([1, 2, 'Fizz', 4, 'Buzz', 7], False),
    (
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
            'FizzBuzz',
        ],
        False,
    ),
    (
        [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 'Fizz'],
        False,
    ),
    (
        [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 'Buzz'],
        False,
    ),
    (
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
        True,
    ),
]


@mark.parametrize('sequence,expected', tests)
def test_is_fizz_buzz(sequence: list[str | int], expected: bool) -> None:
    assert is_fizz_buzz(sequence) == expected


if __name__ == '__main__':
    sequence, expected = tests[0]
    print(is_fizz_buzz(sequence))
