# Daily Coding challenge #63 (2025-10-12) - freeCodeCamp.org
# Battle of Words
# Given two sentences representing your team and an opposing team, where each word from
# your team battles the corresponding word from the opposing team, determine which team
# wins using the following rules:

# The given sentences will always contain the same number of words.
# Words are separated by a single space and will only contain letters.
# The value of each word is the sum of its letters.
# Letters a to z correspond to the values 1 through 26. For example, a is 1, and z is
# 26.A capital letter doubles the value of the letter. For example, A is 2, and Z is 52.
# Words battle in order: the first word of your team battles the first word of the
# opposing team, and so on.
# A word wins if its value is greater than the opposing word's value.
# The team with more winning words is the winner.
# Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw"
# if both teams have the same number of wins.
from pytest import mark


def get_char_value(char: str, base: str = 'a') -> int:
    value = ord(char.lower()) - ord(base) + 1
    return value * 2 if char.isupper() else value


def battle(our_team: str, opponent: str) -> str:
    battles_won = 0

    our_scores = (
        sum(get_char_value(char) for char in word) for word in our_team.split()
    )
    opponent_scores = (
        sum(get_char_value(char) for char in word) for word in opponent.split()
    )

    for our_score, opponent_score in zip(our_scores, opponent_scores):
        if our_score > opponent_score:
            battles_won += 1
        elif our_score < opponent_score:
            battles_won -= 1

    return 'We win' if battles_won > 0 else 'We lose' if battles_won < 0 else 'Draw'


tests = [
    ('hello world', 'hello word', 'We win'),
    ('Hello world', 'hello world', 'We win'),
    ('lorem ipsum', 'kitty ipsum', 'We lose'),
    ('hello world', 'world hello', 'Draw'),
    ('git checkout', 'git switch', 'We win'),
    ('Cheeseburger with fries', 'Cheeseburger with Fries', 'We lose'),
    ('We must never surrender', 'Our team must win', 'Draw'),
]


@mark.parametrize('our_team, opponent, expected', tests)
def test_battle(our_team: str, opponent: str, expected: str) -> None:
    assert battle(our_team, opponent) == expected


if __name__ == '__main__':
    our_team, opponent, exected = tests[0]
    print(battle(our_team, opponent))
