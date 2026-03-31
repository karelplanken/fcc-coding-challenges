# Daily Coding challenge #213 (2026-03-11) - freeCodeCamp.org
# Word Length Converter
# Given a string of words, return a new string where each word is replaced by its
# length.

# Words in the given string will be separated by a single space
# Keep the spaces in the returned string.
# For example, given "hello world", return "5 5".
from pytest import mark


def convert_words(s: str) -> str:
    return ' '.join(str(len(word)) for word in s.split())
    # Micro optimization:
    # return ' '.join(map(str, map(len, s.split())))


tests = [
    ('hello world', '5 5'),
    ('Thanks and happy coding', '6 3 5 6'),
    ('The quick brown fox jumps over the lazy dog', '3 5 5 3 5 4 3 4 3'),
    (
        'Lorem ipsum dolor sit amet consectetur adipiscing elit donec ut ligula '
        + 'vehicula iaculis orci vel semper nisl',
        '5 5 5 3 4 11 10 4 5 2 6 8 7 4 3 6 4',
    ),
]


@mark.parametrize('s, expected', tests)
def test_convert_words(s: str, expected: str) -> None:
    assert convert_words(s) == expected


if __name__ == '__main__':
    s, expected = tests[3]
    print(convert_words(s))
