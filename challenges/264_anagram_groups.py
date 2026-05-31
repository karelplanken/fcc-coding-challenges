# Daily Coding challenge #264 (2026-05-01) - freeCodeCamp.org
# Anagram Groups
# Given an array of words, return a 2d array of the words grouped into anagrams.

# Words are anagrams if they contain the same letters in any order.
# Each word belongs to exactly one group.
# Return order doesn't matter.
# For example, given ["listen", "silent", "hello", "enlist", "world"],
# return [["listen", "silent", "enlist"], ["hello"], ["world"]].
from collections import defaultdict

from pytest import mark


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = defaultdict(list)

    for word in words:
        groups[tuple(sorted(word))].append(word)

    return list(groups.values())


tests = [
    (
        ['listen', 'silent', 'hello', 'enlist', 'world'],
        [['listen', 'silent', 'enlist'], ['hello'], ['world']],
    ),
    (
        ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'],
        [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']],
    ),
    (
        [
            'care',
            'race',
            'acre',
            'pots',
            'stop',
            'tops',
            'opts',
            'post',
            'spot',
            'evil',
            'vile',
            'live',
            'veil',
        ],
        [
            ['acre', 'care', 'race'],
            ['evil', 'live', 'veil', 'vile'],
            ['opts', 'post', 'pots', 'spot', 'stop', 'tops'],
        ],
    ),
    (
        [
            'algorithms',
            'logarithms',
            'education',
            'cautioned',
            'auctioned',
            'triangle',
            'integral',
            'alerting',
            'relating',
        ],
        [
            ['alerting', 'integral', 'relating', 'triangle'],
            ['algorithms', 'logarithms'],
            ['auctioned', 'cautioned', 'education'],
        ],
    ),
]


def normalize_list_of_lists(list_lists: list[list[str]]) -> list[list[str]]:
    return sorted(map(sorted, list_lists))


@mark.parametrize('words, expected', tests)
def test_group_anagrams(words: list[str], expected: list[list[str]]) -> None:
    result = group_anagrams(words)
    assert normalize_list_of_lists(result) == normalize_list_of_lists(expected)


if __name__ == '__main__':
    words, expected = tests[1]
    print(group_anagrams(words))
