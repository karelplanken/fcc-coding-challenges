"""Daily Coding Challenge #89 (2025-11-07) - freeCodeCamp.org."""

# Counting Cards
# A standard deck of playing cards has 13 unique cards in each suit. Given an integer
# representing the number of cards to pick from the deck, return the number of unique
# combinations of cards you can pick.
#
# - Order does not matter. Picking card A then card B is the same as picking card B then
#   card A.
#
# For example, given 52, return 1. There's only one combination of 52 cards to pick from
# a 52 card deck. And given 2, return 1326, There's 1326 card combinations you can end
# up with when picking 2 cards from the deck.
from math import comb

from pytest import mark

DECK_SIZE = 52


def combinations(cards: int) -> int:
    """Return the number of unordered hands of ``cards`` cards from a standard deck.

    Args:
        cards: Number of cards to pick, from 0 to 52 inclusive. Picking 0
            cards yields exactly one hand, the empty one.

    Returns:
        The binomial coefficient C(52, cards).

    Raises:
        ValueError: If ``cards`` is outside the range 0 to 52.
    """
    if not 0 <= cards <= DECK_SIZE:
        msg = f'cards must be between 0 and {DECK_SIZE}, got {cards}.'
        raise ValueError(msg)
    return comb(DECK_SIZE, cards)


tests = [
    (52, 1),
    (1, 52),
    (2, 1326),
    (5, 2598960),
    (10, 15820024220),
    (50, 1326),
]


@mark.parametrize(('cards', 'expected'), tests)
def test_combinations(cards: int, expected: int) -> None:
    """Test combinations function."""
    assert combinations(cards) == expected


if __name__ == '__main__':
    cards, expected = tests[0]
    print(combinations(cards))
