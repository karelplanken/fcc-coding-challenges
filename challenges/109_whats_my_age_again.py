# Daily Coding challenge #108 (2025-11-26) - freeCodeCamp.org
# What's My Age Again?

# What's My Age Again?

# Given the date of someone's birthday in the format YYYY-MM-DD, return the person's
# age as of November 27th, 2025.

# Assume all birthdays are valid dates before November 27th, 2025.
# Return the age as an integer.
# Be sure to account for whether the person has already had their birthday in 2025.
from datetime import date

from pytest import mark


def calculate_age(birthday: str) -> int:
    """
    Calculate a person's age based on their birthday.
    Args:
        birthday (str): The birthday in ISO format (YYYY-MM-DD).
    Returns:
        int: The person's age in years.
    Example:
        >>> calculate_age('1990-05-15')
        33
    """
    today = date.today()
    birth_date = date.fromisoformat(birthday)
    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age


tests = [
    ('2000-11-20', 25),
    ('2000-12-01', 24),
    ('2014-10-25', 11),
    ('1994-01-06', 31),
    ('1994-12-14', 30),
]


@mark.parametrize('birthday,expected', tests)
def test_calculate_age(birthday: str, expected: int) -> None:
    assert calculate_age(birthday) == expected


if __name__ == '__main__':
    birthday, expected = tests[0]
    print(calculate_age(birthday))
