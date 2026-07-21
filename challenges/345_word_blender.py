# Daily Coding challenge #345 (2026-07-21) - freeCodeCamp.org
# Word Blender
# Given two words, return a new word by combining the first half of the first word with
# the second half of the second word.
#
# - For odd-length words, the first half is the shorter half.
from pytest import mark


def blend_words(word1: str, word2: str) -> str:
    """Combine the shorter first half of word1 with the longer second half of word2.

    For odd-length words, floor division puts the extra character on the
    second half, so `len(word) // 2` is the shorter-half boundary.

    Args:
        word1: first word to blend
        word2: second word to blend

    Returns:
        the blended word
    """
    def shorter_half(word: str) -> str:
        return word[: len(word) // 2]

    def longer_half(word: str) -> str:
        return word[len(word) // 2 :]

    return shorter_half(word1) + longer_half(word2)


tests = [
    ('turtle', 'toucan', 'turcan'),
    ('chipmunk', 'flamingo', 'chipingo'),
    ('falcon', 'pelican', 'falican'),
    ('hyena', 'iguana', 'hyana'),
    ('scorpion', 'gorilla', 'scorilla'),
    ('platypus', 'wolverine', 'platerine'),
]


@mark.parametrize('word1, word2, expected', tests)
def test_blend_words(word1: str, word2: str, expected: str) -> None:
    assert blend_words(word1, word2) == expected


if __name__ == '__main__':
    word1, word2, expected = tests[0]
    print(blend_words(word1, word2))
