# Daily Coding challenge #105 (2025-11-23) - freeCodeCamp.org
# Character Count

# Given a sentence string, return an array with a count of each character in
# alphabetical order.

# Treat upper and lowercase letters as the same letter when counting.
# Ignore numbers, spaces, punctuation, etc.
# Return the count and letter in the format "letter count". For instance, "a 3".
# All returned letters should be lowercase.
# Do not return a count of letters that are not in the given string.
from collections import Counter

from pytest import mark


def count_characters(sentence: str) -> list[str]:
    lower_letters_only = [char.lower() for char in sentence if char.isalpha()]
    return [
        f'{letter} {count}'
        for letter, count in sorted(Counter(lower_letters_only).items())
    ]


tests = [
    ('hello world', ['d 1', 'e 1', 'h 1', 'l 3', 'o 2', 'r 1', 'w 1']),
    (
        'I love coding challenges!',
        [
            'a 1',
            'c 2',
            'd 1',
            'e 3',
            'g 2',
            'h 1',
            'i 2',
            'l 3',
            'n 2',
            'o 2',
            's 1',
            'v 1',
        ],
    ),
    (
        '// TODO: Complete this challenge ASAP!',
        [
            'a 3',
            'c 2',
            'd 1',
            'e 4',
            'g 1',
            'h 2',
            'i 1',
            'l 3',
            'm 1',
            'n 1',
            'o 3',
            'p 2',
            's 2',
            't 3',
        ],
    ),
]


@mark.parametrize(('sentence', 'expected'), tests)
def test_count_characters(sentence: str, expected: list[str]) -> None:
    assert count_characters(sentence) == expected


if __name__ == '__main__':
    sentence, expected = tests[0]
    print(count_characters(sentence))
