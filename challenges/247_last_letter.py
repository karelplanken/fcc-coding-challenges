# Daily Coding challenge #246 (2026-04-13) - freeCodeCamp.org
# Last Letter
# Given a string, return the letter from the string that appears last in the alphabet.

# If two or more letters tie for the last in the alphabet, return the first one.
# Ignore all non-letter characters.
from pytest import mark


def get_last_letter(s: str) -> str | None:
    letters = [char for char in s if char.isalpha()]

    if not letters:
        return None

    return max(letters, key=lambda letter: (letter.lower(), -letters.index(letter)))


tests = [
    ('world', 'w'),
    ('Hello World', 'W'),
    ('The quick brown fox jumped over the lazy dog.', 'z'),
    ('HeLl0', 'L'),
    ('!#$ er@R asd fT.,> 2t0e9', 'T'),
]


@mark.parametrize('s, expected', tests)
def test_get_last_letter(s: str, expected: str) -> None:
    assert get_last_letter(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(get_last_letter(s))
