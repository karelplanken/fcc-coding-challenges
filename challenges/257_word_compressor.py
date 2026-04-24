# Daily Coding challenge #257 (2026-04-24) - freeCodeCamp.org
# Word Compressor
# Given a string, return a compressed version of the string using the following rules:

# The first occurrence of a word remains unchanged.
# Subsequent occurrences are replaced with the position of the first occurrence, where
# the first word is at position 1.
# Words are separated by a single space.

# For example, given "practice makes perfect and perfect practice makes perfect",
# return "practice makes perfect and 3 1 2 3".
# starmap unpacks the tuple for you, keeping the signature natural
from itertools import starmap

from pytest import mark


def compress(s: str) -> str:
    seen: dict[str, str] = {}

    def get_word_or_position(position: int, word: str) -> str:
        if word in seen:
            return seen[word]
        seen[word] = str(position)
        return word

    return ' '.join(starmap(get_word_or_position, enumerate(s.split(), start=1)))


tests = [
    (
        'practice makes perfect and perfect practice makes perfect',
        'practice makes perfect and 3 1 2 3',
    ),
    ('hello hello hello', 'hello 1 1'),
    (
        'the cat sat on the mat on which the cat sat',
        'the cat sat on 1 mat 4 which 1 2 3',
    ),
    (
        "the more you know the more you realize you don't know",
        "the more you know 1 2 3 realize 3 don't 4",
    ),
    (
        'lorem ipsum dolor sit per elit donec sit nostra libero per donec ligula sit '
        + 'gravida at elit vitae a elit sodales donec en donec at dolor nam ligula '
        + 'dignissim risus at ligula per nam ipsum ipsum gravida en elit per ipsum '
        + 'ligula en gravida per sodales sit at nam lorem sit per libero en ipsum elit '
        + 'sit sodales sit risus elit risus ipsum elit at gravida vitae en dignissim '
        + 'nam sit vitae sollicitudin per nostra per sit libero',
        'lorem ipsum dolor sit per elit donec 4 nostra libero 5 7 ligula 4 gravida at '
        + '6 vitae a 6 sodales 7 en 7 16 3 nam 13 dignissim risus 16 13 5 27 2 2 15 23 '
        + '6 5 2 13 23 15 5 21 4 16 27 1 4 5 10 23 2 6 4 21 4 30 6 30 2 6 16 15 18 23 '
        + '29 27 4 18 sollicitudin 5 9 5 4 10',
    ),
]


@mark.parametrize(('s', 'expected'), tests)
def test_solution(s: str, expected: str) -> None:
    assert compress(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(compress(s))
