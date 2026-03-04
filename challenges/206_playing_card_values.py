# Daily Coding challenge #206 (2026-03-04) - freeCodeCamp.org
# Playing Card Values
# Given an array of playing cards, return a new array with the numeric value of each
# card.

# Card Values:

# An Ace ("A") has a value of 1.
# Numbered cards ("2" - "10") have their face value: 2 - 10, respectively.
# Face cards: Jack ("J"), Queen ("Q"), and King ("K") are each worth 10.
# Suits:

# Each card has a suit: Spades ("S"), Clubs ("C"), Diamonds ("D"), or Hearts ("H").
# Card Format:

# Each card is represented as a string: "valueSuit". For Example: "AS" is the Ace of
# Spades, "10H" is the Ten of Hearts, and "QC" is the Queen of Clubs.
from types import MappingProxyType

from pytest import mark

PLAYING_CARD_VALUES = MappingProxyType(
    {
        'A': 1,
        **{str(n): n for n in range(2, 11)},  # "2"–"10" map to themselves
        'J': 10,
        'Q': 10,
        'K': 10,
    }
)


def card_values(cards: list[str]) -> list[int]:
    return [PLAYING_CARD_VALUES[card[:-1]] for card in cards]


tests = [
    (['3H', '4D', '5S'], [3, 4, 5]),
    (['AS', '10S', '10H', '6D', '7D'], [1, 10, 10, 6, 7]),
    (['8D', 'QS', '2H', 'JC', '9C'], [8, 10, 2, 10, 9]),
    (['AS', 'KS'], [1, 10]),
    (['10H', 'JH', 'QH', 'KH', 'AH'], [10, 10, 10, 10, 1]),
]


@mark.parametrize('cards, expected', tests)
def test(cards: list[str], expected: list[int]) -> None:
    assert card_values(cards) == expected


if __name__ == '__main__':
    cards, expected = tests[0]
    print(card_values(cards))
