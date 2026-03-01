# Daily Coding challenge #102 (2025-11-20) - freeCodeCamp.org
# Longest Word
# Given a sentence string, return the longest word in the sentence.

# Words are separated by a single space.
# Only letters (a-z, case-insensitive) count toward the word's length.
# If there are multiple words with the same length, return the first one that appears.
# Return the word as it appears in the given string, with punctuation removed.
from pytest import mark


def longest_word(sentence: str) -> str:
    words = [''.join(c for c in word if c.isalpha()) for word in sentence.split()]
    return max(words, key=len)


test = [
    ('The quick red fox', 'quick'),
    ('Hello coding challenge.', 'challenge'),
    ('Do Try This At Home.', 'This'),
    ('This sentence... has commas, ellipses, and an exclamation point!', 'exclamation'),
    ('A tie? No way!', 'tie'),
    ("Wouldn't you like to know.", 'Wouldnt'),
]


@mark.parametrize(('sentence', 'expected'), test)
def test_longest_word(sentence: str, expected: str) -> None:
    assert longest_word(sentence) == expected


if __name__ == '__main__':
    sentence, expected = test[0]
    print(longest_word(sentence))
