"""Daily Coding Challenge #342 (2026-07-18) - freeCodeCamp.org."""

# Dice Odds
# Given a number of six-sided dice to roll and a target sum, return the odds of rolling
# that sum as a string in the format `"1 in X"`.
#
# - The number of dice will be between 1 and 6.
# - The target sum is always achievable with the given number of dice.
# - Round `"X"` to the nearest whole number.
from itertools import product

from pytest import mark

FACES_PER_DIE = 6


def get_odds(dice: int, target: int) -> str:
    all_combis = product(range(1, FACES_PER_DIE + 1), repeat=dice)
    target_combis = sum(1 for dices in all_combis if sum(dices) == target)

    return f'1 in {round((FACES_PER_DIE**dice) / target_combis)}'


tests = [
    (1, 5, '1 in 6'),
    (2, 4, '1 in 12'),
    (3, 10, '1 in 8'),
    (4, 7, '1 in 65'),
    (5, 26, '1 in 111'),
    (6, 35, '1 in 7776'),
]


@mark.parametrize('dice, target, expected', tests)
def test_get_odds(dice: int, target: int, expected: str) -> None:
    """Test get_odds function."""
    assert get_odds(dice, target) == expected


if __name__ == '__main__':
    dice, target, expected = tests[5]
    print(get_odds(dice, target))
