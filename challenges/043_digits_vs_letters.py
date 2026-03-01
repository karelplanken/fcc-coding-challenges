# Daily Coding challenge #43 (2025-09-22) - freeCodeCamp.org
# Digits vs Letters
# Given a string, return "digits" if the string has more digits than letters, "letters"
# if it has more letters than digits, and "tie" if it has the same amount of digits and
# letters.

# Digits consist of 0-9.
# Letters consist of a-z in upper or lower case.
# Ignore any other characters.
from pytest import mark


def digits_or_letters(s: str) -> str:
    letters = digits = 0
    for char in s:
        letters += char.isalpha()
        digits += char.isdigit()

    return 'letters' if letters > digits else 'digits' if digits > letters else 'tie'


tests = [
    ('abc123', 'tie'),
    ('a1b2c3d', 'letters'),
    ('1a2b3c4', 'digits'),
    ('abc123!@#DEF', 'letters'),
    ('H3110 W0R1D', 'digits'),
    ('P455W0RD', 'tie'),
]


@mark.parametrize('s, expected', tests)
def test_digits_or_letters(s: str, expected: str) -> None:
    assert digits_or_letters(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(digits_or_letters(s))
