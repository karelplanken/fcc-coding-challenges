# Daily Coding challenge #335 (2026-07-11) - freeCodeCamp.org
# Five Dice
# Given an array of five dice with values 1-6, return the best possible hand.
#
# Here are the hands ranked lowest to highest:
#
# | Hand | Description |
# |------|-------------|
# | "no pair" | No pair or better |
# | "pair" | Two dice with the same value |
# | "two pair" | Two different pairs |
# | "three of a kind" | Three dice with the same value |
# | "small straight" | Four consecutive values |
# | "large straight" | Five consecutive values |
# | "full house" | Three of a kind and a pair |
# | "four of a kind" | Four dice with the same value |
# | "five of a kind" | All five dice with the same value |
from collections import Counter

from pytest import mark

_STRAIGHT_RUNS = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]


def five_dice(dice: list[int]) -> str:
    if len(dice) != 5 or not all(1 <= d <= 6 for d in dice):
        raise ValueError(f'expected 5 dice with values 1-6, got {dice!r}')

    counts = Counter(dice)
    freq = sorted(counts.values(), reverse=True)  # e.g. [3, 2] for full house
    values = set(counts)  # distinct dice values present

    if freq[0] == 5:
        return 'five of a kind'
    if freq[0] == 4:
        return 'four of a kind'
    if freq == [3, 2]:
        return 'full house'
    if values in ({1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}):
        return 'large straight'
    if any(run <= values for run in _STRAIGHT_RUNS):
        return 'small straight'
    if freq[0] == 3:
        return 'three of a kind'
    if freq[:2] == [2, 2]:
        return 'two pair'
    if freq[0] == 2:
        return 'pair'
    return 'no pair'


tests = [
    ([1, 1, 1, 1, 1], 'five of a kind'),
    ([5, 5, 5, 6, 5], 'four of a kind'),
    ([2, 5, 6, 4, 3], 'large straight'),
    ([4, 3, 3, 3, 1], 'three of a kind'),
    ([4, 6, 2, 6, 5], 'pair'),
    ([1, 4, 5, 6, 2], 'no pair'),
    ([1, 3, 4, 6, 2], 'small straight'),
    ([2, 2, 5, 2, 5], 'full house'),
    ([6, 4, 5, 6, 4], 'two pair'),
]


@mark.parametrize('dice, expected', tests)
def test_five_dice(dice: list[int], expected: str) -> None:
    assert five_dice(dice) == expected


if __name__ == '__main__':
    dice, expected = tests[2]
    print(five_dice(dice))
