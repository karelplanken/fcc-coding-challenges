# Daily Coding challenge #254 (2026-04-21) - freeCodeCamp.org
# Odd Words
# Given a string of words, return only the words with an odd number of letters.

# Words in the given string will be separated by a single space.
# Return the words separated by a single space.
from pytest import mark


def get_odd_words(s: str) -> str:
    return ' '.join(word for word in s.split() if len(word) % 2 == 1)


tests = [
    ('This is a super good test', 'a super'),
    ('one two three four', 'one two three'),
    (
        'banana split sundae with rainbow sprinkles on top',
        'split rainbow sprinkles top',
    ),
    ('The quick brown fox jumped over the lazy river', 'The quick brown fox the river'),
]


@mark.parametrize('s, expected', tests)
def test(s: str, expected: str) -> None:
    assert get_odd_words(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(get_odd_words(s))
