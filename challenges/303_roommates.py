# Daily Coding challenge #303 (2026-06-09) - freeCodeCamp.org
# Roommates
# Given an array of people and their roommate group, return the room assignments for a
# hotel stay using the following rules:

# Each person has a name and a group property:
# [
#   { "name": "Alice", "group": "A" },
#   { "name": "Bob", "group": "B" },
#   { "name": "Carol", "group": "A" }
# ]
# People can only share a room with someone from the same group and are paired in the
# order they are given.
# Return an array of strings with names separated by " and " for a shared room, and
# just the name for a solo room. Names must appear in the order they were paired. For
# the example above, return ["Alice and Carol", "Bob"].
# from collections import defaultdict
from collections import defaultdict
from itertools import batched

from pytest import mark


def get_roommates(people: list[dict[str, str]]) -> list[str]:
    # people is not sorted, otherwise itertools.groupby would be sufficient
    groups = defaultdict(list)
    for p in people:
        groups[p['group']].append(p['name'])
    return [
        ' and '.join(pair) for names in groups.values() for pair in batched(names, 2)
    ]


tests = [
    (
        [
            {'name': 'Alice', 'group': 'A'},
            {'name': 'Bob', 'group': 'B'},
            {'name': 'Carol', 'group': 'A'},
        ],
        ['Alice and Carol', 'Bob'],
    ),
    (
        [
            {'name': 'John', 'group': 'C'},
            {'name': 'Julia', 'group': 'C'},
            {'name': 'Jim', 'group': 'C'},
        ],
        ['John and Julia', 'Jim'],
    ),
    (
        [
            {'name': 'Adam', 'group': 'D'},
            {'name': 'Abraham', 'group': 'E'},
            {'name': 'Austin', 'group': 'E'},
            {'name': 'Augustus', 'group': 'D'},
            {'name': 'Angelica', 'group': 'D'},
            {'name': 'Aaron', 'group': 'E'},
        ],
        ['Adam and Augustus', 'Angelica', 'Abraham and Austin', 'Aaron'],
    ),
    (
        [
            {'name': 'Frank', 'group': 'A'},
            {'name': 'Emitt', 'group': 'B'},
            {'name': 'Daria', 'group': 'F'},
            {'name': 'Charles', 'group': 'D'},
            {'name': 'Bailey', 'group': 'A'},
            {'name': 'Albert', 'group': 'F'},
        ],
        ['Frank and Bailey', 'Emitt', 'Daria and Albert', 'Charles'],
    ),
    (
        [
            {'name': 'Kevin', 'group': 'A'},
            {'name': 'Yuri', 'group': 'A'},
            {'name': 'Hugo', 'group': 'B'},
            {'name': 'Violet', 'group': 'A'},
            {'name': 'Brett', 'group': 'A'},
            {'name': 'Wayne', 'group': 'B'},
        ],
        ['Kevin and Yuri', 'Violet and Brett', 'Hugo and Wayne'],
    ),
]


@mark.parametrize('people, expected', tests)
def test(people: list[dict[str, str]], expected: list[str]) -> None:
    assert get_roommates(people) == expected


if __name__ == '__main__':
    people, expected = tests[0]
    print(get_roommates(people), expected)
