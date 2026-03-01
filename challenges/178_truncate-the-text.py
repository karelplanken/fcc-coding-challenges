# Daily Coding challenge #178 (2026-02-04) - freeCodeCamp.org
# Truncate the Text
# Given a string, return it as-is if it's 20 characters or shorter. If it's longer than
# 20 characters, truncate it to the first 17 characters and append "..." to the end of
# it (so it's 20 characters total) and return the result.
from pytest import mark


def truncate_text(text: str) -> str:
    return text if len(text) <= 20 else text[:17] + '...'


tests = [
    ('Hello, world!', 'Hello, world!'),
    ('This string should get truncated.', 'This string shoul...'),
    ('Exactly twenty chars', 'Exactly twenty chars'),
    ('.....................', '....................'),
]


@mark.parametrize('text, expected', tests)
def test_truncate_text(text: str, expected: str) -> None:
    assert truncate_text(text) == expected


if __name__ == '__main__':
    text, expected = tests[0]
    print(truncate_text(text))
