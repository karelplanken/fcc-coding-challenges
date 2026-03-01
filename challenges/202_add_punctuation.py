# Daily Coding challenge #202 (2026-02-28) - freeCodeCamp.org
# Add Punctuation
# Given a string of sentences with missing periods, add a period (".") in the following
# places:

# Before each space that comes immediately before an uppercase letter
# And at the end of the string
# Return the resulting string.
# import re
import re

from pytest import mark


def add_punctuation(sentences: str) -> str:
    return re.sub(r'(?= [A-Z])', '.', sentences) + '.'

# def add_punctuation(sentences: str) -> str:
#     words = sentences.split()

#     for i in range(1, len(words)):
#         if words[i][0].isupper():
#             words[i - 1] += '.'
#     words[-1] += '.'

#     return ' '.join(words)


tests = [
    ('Hello world', 'Hello world.'),
    ("Hello world It's nice today", "Hello world. It's nice today."),
    ('JavaScript is great Sometimes', 'JavaScript is great. Sometimes.'),
    (
        'A b c D e F g h I J k L m n o P Q r S t U v w X Y Z',
        'A b c. D e. F g h. I. J k. L m n o. P. Q r. S t. U v w. X. Y. Z.',
    ),
    ('Wait.. For it', 'Wait... For it.'),
]


@mark.parametrize('sentences, expected', tests)
def test(sentences: str, expected: str) -> None:
    assert add_punctuation(sentences) == expected


if __name__ == '__main__':
    sentences, expected = tests[1]
    print(add_punctuation(sentences))