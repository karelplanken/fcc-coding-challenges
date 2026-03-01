# Daily Coding challenge #140 (2025-12-28) - freeCodeCamp.org
# SCREAMING_SNAKE_CASE
# Given a string representing a variable name, return the variable name converted to
# SCREAMING_SNAKE_CASE.

# The given variable names will be written in one of the following formats:

# camelCase
# PascalCase
# snake_case
# kebab-case
# In the above formats, words are separated by an underscore (_), a hyphen (-), or a
# new word starts with a capital letter.

# To convert to SCREAMING_SNAKE_CASE:

# Make all letters uppercase
# Separate words with an underscore (_)
from pytest import mark

# One-liner solution (less efficient multiple string traversals):
# def to_screaming_snake_case(variable_name: str) -> str:
#     return '_'.join(
#         (
#             ''.join(
#                 ' ' + char if char.isupper() else char
#                 for char in variable_name.replace('_', ' ').replace('-', ' ')
#             )
#             .upper()
#             .split()
#         )
#     )


# More efficient solution (single string traversal):
def to_screaming_snake_case(variable_name: str) -> str:
    result = []

    for i, char in enumerate(variable_name):
        if char in '_-':
            result.append('_')
        elif char.isupper() and i > 0 and variable_name[i - 1] not in '_-':
            result.append('_')
            result.append(char)
        else:
            result.append(char.upper())

    return ''.join(result)


tests = [
    ('userEmail', 'USER_EMAIL'),
    ('UserPassword', 'USER_PASSWORD'),
    ('user_id', 'USER_ID'),
    ('user-address', 'USER_ADDRESS'),
    ('username', 'USERNAME'),
]


@mark.parametrize('variable_name, expected', tests)
def test(variable_name: str, expected: str) -> None:
    assert to_screaming_snake_case(variable_name) == expected


if __name__ == '__main__':
    variable_name, expected = tests[1]
    print(to_screaming_snake_case(variable_name))
