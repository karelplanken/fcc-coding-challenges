# Daily Coding challenge #204 (2026-03-02) - freeCodeCamp.org
# Sum the Letters
# Given a string, return the sum of its letters.

# Letters are A-Z in uppercase or lowercase
# Letter values are: "A" = 1, "B" = 2, ..., "Z" = 26
# Uppercase and lowercase letters have the same value.
# Ignore all non-letter characters.
from pytest import mark


def sum_letters(s: str) -> int:
    return sum(ord(char) - 96 for char in s.lower() if char.isalpha())


tests = [
    ('Hello', 52),
    ('freeCodeCamp', 94),
    ('The quick brown fox jumps over the lazy dog.', 473),
    (
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ex nisl,'
        + ' pretium eu varius blandit, facilisis quis eros. Vestibulum ante ipsum'
        + ' primis in faucibus orci.',
        1681,
    ),
    ('</404>', 0),
]


@mark.parametrize('s, expected', tests)
def test(s: str, expected: int) -> None:
    assert sum_letters(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(sum_letters(s))
