# Daily Coding challenge #119 (2025-12-07) - freeCodeCamp.org
# String Compression
# Given a string sentence, return a compressed version of the sentence where consecutive
# duplicate words are replaced by the word followed with the number of times it repeats
# in parentheses.

# Only consecutive duplicates are compressed.
# Words are separated by single spaces.
# For example, given "yes yes yes please", return "yes(3) please".
# Option 1: Cleaner loop logic (minimal changes)
# def compress_string(sentence: str) -> str:
#     if not sentence:
#         return sentence

#     words = sentence.split()
#     compressed = []
#     count = 1

#     for i in range(1, len(words)):
#         if words[i] == words[i - 1]:
#             count += 1
#         else:
#             word = f'{words[i - 1]}({count})' if count > 1 else words[i - 1]
#             compressed.append(word)
#             count = 1

#     # Handle last word(s) - same logic
#     word = f'{words[-1]}({count})' if count > 1 else words[-1]
#     compressed.append(word)

#     return ' '.join(compressed)

# Option 2: Using itertools.groupby (Pythonic)
# from itertools import groupby


# def compress_string(sentence: str) -> str:
#     if not sentence:
#         return sentence

#     words = sentence.split()
#     compressed = []

#     for word, group in groupby(words):
#         count = len(list(group))
#         compressed.append(f'{word}({count})' if count > 1 else word)

#     return ' '.join(compressed)


# Option 3: Generator expression (memory efficient)
from collections.abc import Iterator
from itertools import groupby

from pytest import mark


def compress_string(sentence: str) -> str:
    if not sentence:
        return sentence

    words = sentence.split()

    def format_group(word: str, group: Iterator[str]) -> str:
        count = sum(1 for _ in group)
        return f'{word}({count})' if count > 1 else word

    return ' '.join(format_group(word, group) for word, group in groupby(words))


tests = [
    ('yes yes yes please', 'yes(3) please'),
    ('I have have have apples', 'I have(3) apples'),
    ('one one three and to the the the the', 'one(2) three and to the(4)'),
    ('route route route route route route tee tee tee tee tee tee', 'route(6) tee(6)'),
]


@mark.parametrize('sentence,expected', tests)
def test_compress_string(sentence: str, expected: str) -> None:
    assert compress_string(sentence) == expected


if __name__ == '__main__':
    sentence, expected = tests[0]
    print(compress_string(sentence))
