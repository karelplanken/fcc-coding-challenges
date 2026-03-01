# Daily Coding challenge #32 (2025-09-11) - freeCodeCamp.org
# Reverse Sentence
# Given a string of words, return a new string with the words in reverse order. For
# example, the first word should be at the end of the returned string, and the last
# word should be at the beginning of the returned string.

# In the given string, words can be separated by one or more spaces.
# The returned string should only have one space between words.
from pytest import mark


def reverse_sentence(sentence: str) -> str:
    return ' '.join(reversed(sentence.split()))


tests = [
    ('world hello', 'hello world'),
    ('push commit git', 'git commit push'),
    ('npm  install   apt    sudo', 'sudo apt install npm'),
    ('import    default   function  export', 'export function default import'),
]


@mark.parametrize('sentence, expected', tests)
def test_reverse_sentence(sentence: str, expected: str) -> None:
    assert reverse_sentence(sentence) == expected


if __name__ == '__main__':
    sentence, expected = tests[0]
    print(reverse_sentence(sentence))
