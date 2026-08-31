"""Daily Coding Challenge #14 (2025-08-24) - freeCodeCamp.org."""

# Character Battle
# Given two strings representing your army and an opposing army, each character from
# your army battles the character at the same position from the opposing army using the
# following rules:
#
# - Characters a-z have a strength of 1-26, respectively.
# - Characters A-Z have a strength of 27-52, respectively.
# - Digits 0-9 have a strength of their face value.
# - All other characters have a value of zero.
# - Each character can only fight one battle.
#
# For each battle, the stronger character wins. The army with more victories, wins the
# war. Return the following values:
#
# - "Opponent retreated" if your army has more characters than the opposing army.
# - "We retreated" if the opposing army has more characters than yours.
# - "We won" if your army won more battles.
# - "We lost" if the opposing army won more battles.
# - "It was a tie" if both armies won the same number of battles.
from string import ascii_lowercase, ascii_uppercase, digits
from types import MappingProxyType

from pytest import mark


def _get_map(chars: str, start_strength: int = 0) -> dict[str, int]:
    """Return a mapping of characters to their strength values.

    Args:
        chars: The characters to map, in ascending strength order.
        start_strength: The strength assigned to the first character.

    Returns:
        A dict mapping each character to its strength.
    """
    return {char: strength for strength, char in enumerate(chars, start=start_strength)}


CHARACTER_STRENGTHS = MappingProxyType({
    **_get_map(ascii_lowercase, 1),
    **_get_map(ascii_uppercase, 27),
    **_get_map(digits, 0),
})


def _get_strength(char: str) -> int:
    """Return the strength of a character.

    Args:
        char: The character to score.

    Returns:
        The character's strength, or 0 if it has no defined strength.
    """
    return CHARACTER_STRENGTHS.get(char, 0)


def _compare(we: str, they: str) -> int:
    """Score a single battle between two characters.

    Args:
        we: Our character in this battle.
        they: The opposing character in this battle.

    Returns:
        1 if our character wins, -1 if it loses, 0 on a tie.
    """
    we_strength = _get_strength(we)
    they_strength = _get_strength(they)
    return (we_strength > they_strength) - (we_strength < they_strength)


def battle(my_army: str, opposing_army: str) -> str:
    """Return the result of a battle between two armies.

    Args:
        my_army: Your army string.
        opposing_army: Opposing army string.

    Returns:
        The result of the battle.
    """
    if len(my_army) != len(opposing_army):
        return (
            'We retreated'
            if len(my_army) < len(opposing_army)
            else 'Opponent retreated'
        )

    net_score = sum(_compare(we, they) for we, they in zip(my_army, opposing_army))

    if net_score > 0:
        return 'We won'
    if net_score < 0:
        return 'We lost'
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
    """Test battle function."""
    assert battle(my_army, opposing_army) == expected


if __name__ == '__main__':
    my_army, opposing_army, expected = tests[0]
    print(battle(my_army, opposing_army))
