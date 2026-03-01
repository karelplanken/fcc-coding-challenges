# Daily Coding challenge #14 (2025-08-24) - freeCodeCamp.org
# Character Battle
# Given two strings representing your army and an opposing army, each character from
# your army battles the character at the same position from the opposing army using
# the following rules:

# Characters a-z have a strength of 1-26, respectively.
# Characters A-Z have a strength of 27-52, respectively.
# Digits 0-9 have a strength of their face value.
# All other characters have a value of zero.
# Each character can only fight one battle.
# For each battle, the stronger character wins. The army with more victories, wins the
# war. Return the following values:

# "Opponent retreated" if your army has more characters than the opposing army.
# "We retreated" if the opposing army has more characters than yours.
# "We won" if your army won more battles.
# "We lost" if the opposing army won more battles.
# "It was a tie" if both armies won the same number of battles.
from pytest import mark


def get_strength(char: str) -> int:
    if 'a' <= char <= 'z':
        return ord(char) - ord('a') + 1
    elif 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 27
    elif '0' <= char <= '9':
        return int(char)
    else:
        return 0


def battle(my_army: str, opposing_army: str) -> str:
    if len(my_army) < len(opposing_army):
        return 'We retreated'
    elif len(my_army) > len(opposing_army):
        return 'Opponent retreated'

    my_amry_score = 0
    opposing_army_score = 0

    for we, they in zip(my_army, opposing_army):
        if get_strength(we) > get_strength(they):
            my_amry_score += 1
        elif get_strength(we) < get_strength(they):
            opposing_army_score += 1

    if my_amry_score > opposing_army_score:
        return 'We won'
    elif my_amry_score < opposing_army_score:
        return 'We lost'
    else:
        return 'It was a tie'


tests = [
    ('Hello', 'World', 'We lost'),
    ('pizza', 'salad', 'We won'),
    ('C@T5', 'D0G$', 'We won'),
    ('kn!ght', 'orc', 'Opponent retreated'),
    ('PC', 'Mac', 'We retreated'),
    ('Wizards', 'Dragons', 'It was a tie'),
    ('Mr. Smith', 'Dr. Jones', 'It was a tie'),
]


@mark.parametrize('my_army, opposing_army, expected', tests)
def test_battle(my_army: str, opposing_army: str, expected: str) -> None:
    assert battle(my_army, opposing_army) == expected


if __name__ == '__main__':
    my_army, opposing_army, expected = tests[0]
    print(battle(my_army, opposing_army))
