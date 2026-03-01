# Daily Coding challenge #38 (2025-09-17) - freeCodeCamp.org
# Slug Generator
# Given a string, return a URL-friendly version of the string using the following
# constraints:

# All letters should be lowercase.
# All characters that are not letters, numbers, or spaces should be removed.
# All spaces should be replaced with the URL-encoded space code %20.
# Consecutive spaces should be replaced with a single %20.
# The returned string should not have leading or trailing %20.
from pytest import mark


def generate_slug(text: str) -> str:
    # Convert to lowercase and keep only alphanumeric and spaces
    cleaned = ''.join(c for c in text.lower() if c.isalnum() or c.isspace())
    # Replace consecutive spaces with single space, then strip and replace with %20
    # this also takes care of leading and trailing spaces
    return '%20'.join(cleaned.split())


tests = [
    ('helloWorld', 'helloworld'),
    ('hello world!', 'hello%20world'),
    (' hello-world ', 'helloworld'),
    ('hello  world', 'hello%20world'),
    ('  ?H^3-1*1]0! W[0%R#1]D  ', 'h3110%20w0r1d'),
]


@mark.parametrize('text, expected', tests)
def test_generate_slug(text: str, expected: str) -> None:
    assert generate_slug(text) == expected


if __name__ == '__main__':
    text, expected = tests[2]
    print(generate_slug(text))
