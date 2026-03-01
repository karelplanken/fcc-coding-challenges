# Daily Coding challenge #126 (2025-12-14) - freeCodeCamp.org
# Capitalize It
# Given a string title, return a new string formatted in title case using the following
# rules:

# Capitalize the first letter of each word.
# Make all other letters in each word lowercase.
# Words are always separated by a single space.
from pytest import mark


def title_case(title: str) -> str:
    # str.title() lowers all letters and capitalizes first letter of each word
    return ' '.join(word.title() for word in title.split(' '))


# def title_case(title: str) -> str:
#     return ' '.join(map(str.title, title.split(' ')))

tests = [
    ('hello world', 'Hello World'),
    ('the quick brown fox', 'The Quick Brown Fox'),
    ('JAVASCRIPT AND PYTHON', 'Javascript And Python'),
    ('AvOcAdO tOAst fOr brEAkfAst', 'Avocado Toast For Breakfast'),
]


@mark.parametrize('title, expected', tests)
def test_title_case(title: str, expected: str) -> None:
    assert title_case(title) == expected


if __name__ == '__main__':
    title, expected = tests[0]
    print(title_case(title))
