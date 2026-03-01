# Daily Coding challenge #44 (2025-09-23) - freeCodeCamp.org
# String Mirror
# Given two strings, determine if the second string is a mirror of the first.

# A string is considered a mirror if it contains the same letters in reverse order.
# Treat uppercase and lowercase letters as distinct.
# Ignore all non-alphabetical characters.
from pytest import mark


def is_mirror(str1: str, str2: str) -> bool:
    for char_1, char_2 in zip(
        (char for char in str1 if char.isalpha()),
        (char for char in reversed(str2) if char.isalpha()),
    ):
        if char_1 != char_2:
            return False

    return True


tests = [
    ('helloworld', 'helloworld', False),
    ('Hello World', 'dlroW olleH', True),
    ('RaceCar', 'raCecaR', True),
    ('RaceCar', 'RaceCar', False),
    ('Mirror', 'rorrim', False),
    ('Hello World', 'dlroW-olleH', True),
    ('Hello World', '!dlroW !olleH', True),
]


@mark.parametrize('str1, str2, expected', tests)
def test_is_mirror(str1: str, str2: str, expected: bool) -> None:
    assert is_mirror(str1, str2) == expected


if __name__ == '__main__':
    str1, str2, expected = tests[1]
    is_mirror(str1, str2)
