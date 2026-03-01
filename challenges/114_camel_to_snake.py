# Daily Coding challenge #114 (2025-12-02) - freeCodeCamp.org
# Camel to Snake
# Given a string in camel case, return the snake case version of the string using the
# following rules:

# The input string will contain only letters (A-Z and a-z) and will always start with a
# lowercase letter.
# Every uppercase letter in the camel case string starts a new word.
# Convert all letters to lowercase.
# Separate words with an underscore (_).
from pytest import mark


def to_snake(camel: str) -> str:
    return ''.join('_' + char.lower() if char.isupper() else char for char in camel)


tests = [
    ('helloWorld', 'hello_world'),
    ('myVariableName', 'my_variable_name'),
    ('freecodecampDailyChallenges', 'freecodecamp_daily_challenges'),
]


@mark.parametrize('camel,expected', tests)
def test_to_snake(camel: str, expected: str) -> None:
    assert to_snake(camel) == expected


if __name__ == '__main__':
    camel, expected = tests[0]
    print(to_snake(camel))
