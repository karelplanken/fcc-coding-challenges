# Daily Coding challenge #85 (2025-11-03) - freeCodeCamp.org
# Word Counter
# Given a sentence string, return the number of words that are in the sentence.

# Words are any sequence of non-space characters and are separated by a single space.
from pytest import mark


def count_words(sentence: str) -> int:
    return len(sentence.split())


tests = [
    ('Hello world', 2),
    ('The quick brown fox jumps over the lazy dog.', 9),
    ('I like coding challenges!', 4),
    ('Complete the challenge in JavaScript and Python.', 7),
    ('The missing semi-colon crashed the entire internet.', 7),
]


@mark.parametrize(('sentence', 'expected'), tests)
def test_count_words(sentence: str, expected: int) -> None:
    assert count_words(sentence) == expected


if __name__ == '__main__':
    sentence, expected = tests[0]
    print(count_words(sentence))
