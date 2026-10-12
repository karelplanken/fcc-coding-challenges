"""Daily Coding Challenge #63 (2025-10-12) - freeCodeCamp.org."""

# Battle of Words
# Given two sentences representing your team and an opposing team, where each word from
# your team battles the corresponding word from the opposing team, determine which team
# wins using the following rules:
#
# - The given sentences will always contain the same number of words.
# - Words are separated by a single space and will only contain letters.
# - The value of each word is the sum of its letters.
# - Letters a to z correspond to the values 1 through 26. For example, a is 1, and z is
#   26.
# - A capital letter doubles the value of the letter. For example, A is 2, and Z is 52.
# - Words battle in order: the first word of your team battles the first word of the
#   opposing team, and so on.
# - A word wins if its value is greater than the opposing word's value.
# - The team with more winning words is the winner.
#
# Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw"
# if both teams have the same number of wins.
from string import ascii_lowercase, ascii_uppercase

from pytest import mark

_LETTER_VALUES = {
    **{char: i for i, char in enumerate(ascii_lowercase, start=1)},
    **{char: 2 * i for i, char in enumerate(ascii_uppercase, start=1)},
}


def _word_value(word: str) -> int:
    try:
        return sum(_LETTER_VALUES[char] for char in word)
    except KeyError as err:
        msg = f'invalid character: {err.args[0]!r}'
        raise ValueError(msg) from None


def battle(our_team: str, opponent: str) -> str:
    """Determine which team wins the battle of words.

    Words are compared in order, and the team with more winning words is the winner. If
    both teams have the same number of winning words, the result is a draw.

    Args:
        our_team: The sentence representing your team.
        opponent: The sentence representing the opposing team.

    Returns:
        The result of the battle: "We win", "We lose", or "Draw".

    Raises:
        ValueError: If the teams have different numbers of words, if either team is
            empty, or if a word contains a character other than an ASCII letter.
    """
    our_words, opponent_words = our_team.split(), opponent.split()
    if len(our_words) != len(opponent_words):
        msg = 'both teams must have the same number of words'
        raise ValueError(msg)
    if not our_words:
        msg = 'both teams must have at least one word'
        raise ValueError(msg)

    net_wins = sum(
        (ours > theirs) - (ours < theirs)
        for ours, theirs in zip(
            map(_word_value, our_words), map(_word_value, opponent_words), strict=True
        )
    )

    if net_wins > 0:
        return 'We win'
    if net_wins < 0:
        return 'We lose'
    return 'Draw'


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
    """Test battle function."""
    assert battle(our_team, opponent) == expected


if __name__ == '__main__':
    our_team, opponent, expected = tests[0]
    print(battle(our_team, opponent))
