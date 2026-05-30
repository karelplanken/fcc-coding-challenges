# Daily Coding challenge #293 (2026-05-30) - freeCodeCamp.org
# Best Hand
# Given an array of five strings representing playing cards, return the name of the
# best hand.

# Each card is represented as a two-character string: the rank followed by the suit,
# "2h" for example.
# Ranks, from low to high, are:
# "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", and "A".
# Suits are: "h", "d", "c", and "s".
# Aces ("A") can be used as high or low in a straight.
# The hands, in order from worst to best, are:
# Name	Description
# "High Card"	No pair or better
# "Pair"	Two of one rank
# "Two Pair"	Two of one rank and two of another
# "Three of a Kind"	Three of one rank
# "Straight"	Five ranks in a row
# "Flush"	Five of the same suit
# "Full House"	Three of one rank, and two of another
# "Four of a Kind"	Four of one rank
# "Straight Flush"	Five ranks in a row of the same suit
# "Royal Flush"	"A", "K", "Q", "J", "T" of the same suit
# Return the name of the best hand.
from collections import Counter
from collections.abc import Callable

from pytest import mark


class Hand:
    def __init__(self, cards: list[str]) -> None:
        self.ranks = self._get_ranks(cards)
        self.suits = self._get_suits(cards)
        self.counted = Counter(self.ranks).most_common()

    def _get_ranks(self, cards: list[str]) -> list[str]:
        sorted_ranks = sorted((card[0] for card in cards), key=_sort_key)
        # Treat A as low if hand is A-2-3-4-5
        if sorted_ranks[-1] == HIGH_ACE and sorted_ranks[0] == LOW_TWO:
            sorted_ranks = [LOW_ACE] + sorted_ranks[:-1]
        return sorted_ranks

    def _get_suits(self, cards: list[str]) -> list[str]:
        return [card[1] for card in cards]

    def __str__(self) -> str:
        return f'Hand(ranks={self.ranks}, suits={self.suits}, counted={self.counted})'


type HandChecker = Callable[[Hand], bool]

# Keep the RANKS string as is since it is used for lookups where order does matter.
RANKS = 'A23456789TJQKA'
# 'A' at index 0 is only used for low ace in straight, so we can ignore it in the index:
RANK_INDEX = {r: i for i, r in enumerate(RANKS[1:])}
LOW_ACE = RANKS[0]  # 'A'
HIGH_ACE = RANKS[-1]  # 'A'
LOW_TWO = RANKS[1]  # '2'


def _sort_key(rank: str) -> int:
    return RANK_INDEX[rank]


# Each receives (ranks, suits, counted_ranks) so the dispatch table is uniform.
def _is_royal_flush(hand: Hand) -> bool:
    return set(hand.ranks) == {'A', 'K', 'Q', 'J', 'T'} and len(set(hand.suits)) == 1


def _is_straight_flush(hand: Hand) -> bool:
    return _is_straight(hand) and len(set(hand.suits)) == 1


def _is_four_of_a_kind(hand: Hand) -> bool:
    return hand.counted[0][1] == 4


def _is_full_house(hand: Hand) -> bool:
    return hand.counted[0][1] == 3 and hand.counted[1][1] == 2


def _is_flush(hand: Hand) -> bool:
    return len(set(hand.suits)) == 1


def _is_straight(hand: Hand) -> bool:
    # RANKS contains every valid straight as a contiguous substring
    return ''.join(hand.ranks) in RANKS


def _is_three_of_a_kind(hand: Hand) -> bool:
    return hand.counted[0][1] == 3


def _is_two_pair(hand: Hand) -> bool:
    return hand.counted[0][1] == 2 and hand.counted[1][1] == 2


def _is_pair(hand: Hand) -> bool:
    return hand.counted[0][1] == 2


# Best hands first; first match wins.
HANDS: list[tuple[str, HandChecker]] = [
    ('Royal Flush', _is_royal_flush),
    ('Straight Flush', _is_straight_flush),
    ('Four of a Kind', _is_four_of_a_kind),
    ('Full House', _is_full_house),
    ('Flush', _is_flush),
    ('Straight', _is_straight),
    ('Three of a Kind', _is_three_of_a_kind),
    ('Two Pair', _is_two_pair),
    ('Pair', _is_pair),
    ('High Card', lambda hand: True),  # always matches if no better hand found
]


def get_best_hand(cards: list[str]) -> str:
    hand = Hand(cards)

    for name, check in HANDS:
        if check(hand):
            return name

    raise AssertionError('HANDS table is missing a catch-all entry')


tests = [
    (['7s', '7h', '7d', '2c', '5h'], 'Three of a Kind'),  # 0
    (['Ks', 'Kh', 'Kd', '4s', '4h'], 'Full House'),  # 1
    (['2h', '5h', '7h', '9h', 'Jh'], 'Flush'),  # 2
    (['As', 'Ah', 'Ad', 'Ac', 'Kh'], 'Four of a Kind'),  # 3
    (['Ts', 'Th', '9d', '9c', '8h'], 'Two Pair'),  # 4
    (['9c', '8c', '7c', '6c', '5c'], 'Straight Flush'),  # 5
    (['As', 'Kh', 'Jd', '8c', '5h'], 'High Card'),  # 6
    (['As', '2h', '3d', '4c', '5h'], 'Straight'),  # 7
    (['Ts', 'Th', '7c', '6d', '5h'], 'Pair'),  # 8
    (['As', 'Ks', 'Qs', 'Js', 'Ts'], 'Royal Flush'),  # 9
]


@mark.parametrize('cards, expected', tests)
def test_get_best_hand(cards: list[str], expected: str) -> None:
    assert get_best_hand(cards) == expected


if __name__ == '__main__':
    cards, expected = tests[0]
    print(get_best_hand(cards))
