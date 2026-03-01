# Daily Coding challenge #200 (2026-02-26) - freeCodeCamp.org
# Letter and Number Count
# Given a string, return a message with the count of how many letters and numbers it
# contains.

# Letters are A-Z and a-z.
# Numbers are 0-9.
# Ignore all other characters.
# Return "The string has X letters and Y numbers.", where "X" is the count of letters
# and "Y" is the count of numbers. If either count is 1, use the singular form for that
# item. E.g: "1 letter" instead of "1 letters" and "1 number" instead of "1 numbers".
from pytest import mark


def count_letters_and_numbers(s: str) -> str:
    letters = sum(c.isalpha() for c in s)
    numbers = sum(c.isdigit() for c in s)

    l_word = 'letter' if letters == 1 else 'letters'
    n_word = 'number' if numbers == 1 else 'numbers'

    return f'The string has {letters} {l_word} and {numbers} {n_word}.'


tests = [
    ('helloworld123', 'The string has 10 letters and 3 numbers.'),
    ('Catch 22', 'The string has 5 letters and 2 numbers.'),
    ('A1!', 'The string has 1 letter and 1 number.'),
    ('12345', 'The string has 0 letters and 5 numbers.'),
    ('password', 'The string has 8 letters and 0 numbers.'),
]


@mark.parametrize('s, expected', tests)
def test(s: str, expected: str) -> None:
    assert count_letters_and_numbers(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(count_letters_and_numbers(s))
