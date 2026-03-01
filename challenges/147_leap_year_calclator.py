# Daily Coding challenge #147 (2026-01-04) - freeCodeCamp.org
# Leap Year Calculator
# Given an integer year, determine whether it is a leap year.

# A year is a leap year if it satisfies the following rules:

# The year is evenly divisible by 4, and
# The year is not evenly divisible by 100, unless
# The year is evenly divisible by 400.
from pytest import mark


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# More readable:
# def is_leap_year(year: int) -> bool:
#     divisible_by_4 = year % 4 == 0
#     divisible_by_100 = year % 100 == 0
#     divisible_by_400 = year % 400 == 0

#     return divisible_by_4 and (not divisible_by_100 or divisible_by_400)

# Early returns and improved readability:
# def is_leap_year(year: int) -> bool:
#     if year % 400 == 0:
#         return True
#     if year % 100 == 0:
#         return False
#     return year % 4 == 0

tests = [
    (2024, True),
    (2023, False),
    (2100, False),
    (2000, True),
    (1999, False),
    (2040, True),
    (2026, False),
]


@mark.parametrize(('year', 'expected'), tests)
def test_is_leap_year(year: int, expected: bool) -> None:
    assert is_leap_year(year) == expected


if __name__ == '__main__':
    year, expected = tests[0]
    print(is_leap_year(year))
