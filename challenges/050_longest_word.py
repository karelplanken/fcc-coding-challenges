# Daily Coding challenge #50 (2025-09-29) - freeCodeCamp.org
# Longest Word
# Given a sentence, return the longest word in the sentence.

# Ignore periods (.) when determining word length.
# If multiple words are ties for the longest, return the first one that occurs.
from pytest import mark


def get_longest_word(sentence: str) -> str:
    return max(sentence.replace('.', '').split(), key=len)


tests = [
    ('coding is fun', 'coding'),
    ('Coding challenges are fun and educational.', 'educational'),
    ('This sentence has multiple long words.', 'sentence'),
]


@mark.parametrize('sentence, expected', tests)
def test_get_longest_word(sentence: str, expected: str) -> None:
    assert get_longest_word(sentence) == expected


if __name__ == '__main__':
    sentence, expected = tests[1]
    print(get_longest_word(sentence), expected)
