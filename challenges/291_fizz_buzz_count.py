# Daily Coding challenge #291 (2026-05-28) - freeCodeCamp.org
# FizzBuzz Count
# Given a start and end number, count the number of fizz and buzz appearances in the
# range (inclusive).
# Numbers divisible by 3 count as a fizz.
# Numbers divisible by 5 count as a buzz.
# Numbers divisible by both 3 and 5 count as both a fizz and a buzz.
# Return an object or dictionary with the counts in the format: { fizz, buzz }.
from pytest import mark


# Optimized solution using math to count multiples of 3 and 5 in the range without
# iterating through all numbers (see commented out solution below for reference):
def fizz_buzz_count(start: int, end: int) -> dict[str, int]:
    def count_multiples(n: int) -> int:
        # Count integers in [start, end] divisible by n using floor division math
        return (end // n) - ((start - 1) // n)

    return {
        'fizz': count_multiples(3),
        'buzz': count_multiples(5),
    }


# from collections import defaultdict
# def fizz_buzz_count(start: int, end: int) -> dict[str, int]:
#     count: dict[str, int] = defaultdict(int)

#     for i in range(start, end + 1):
#         if i % 3 == 0:
#             count['fizz'] += 1
#         if i % 5 == 0:
#             count['buzz'] += 1

#     return count


tests = [
    (1, 11, {'fizz': 3, 'buzz': 2}),
    (14, 41, {'fizz': 9, 'buzz': 6}),
    (24, 100, {'fizz': 26, 'buzz': 16}),
    (-635, -14, {'fizz': 207, 'buzz': 125}),
    (-5432, 6789, {'fizz': 4074, 'buzz': 2444}),
]


@mark.parametrize('start, end, expected', tests)
def test_fizz_buzz_count(start: int, end: int, expected: dict[str, int]) -> None:
    assert fizz_buzz_count(start, end) == expected


if __name__ == '__main__':
    start, end, expected = tests[4]
    print(fizz_buzz_count(start, end))
