# Daily Coding challenge #359 (2026-08-04) - freeCodeCamp.org
# Golf Handicap Calculator
# Given an array of golf scores and a corresponding array of course par values, return
# the golfer's handicap index using the following method:
#
# - Calculate the differential for each round by subtracting the par from the score,
#   then return the average of all differentials rounded to one decimal place.
from math import floor

from pytest import mark


def round_half_up(value: float, decimals: int = 0) -> float:
    """Round half away from zero (avoids round()'s banker's rounding)."""
    factor: int = 10**decimals
    return floor(value * factor + 0.5) / factor


def calculate_handicap(scores: list[int], pars: list[int]) -> float:
    """Calculate a golf handicap index as a rounded average of score-par differentials.

    Args:
        scores: Golf scores per round.
        pars: Course par values per round, same length as scores.

    Raises:
        ValueError: If scores and pars have different lengths, or if either is empty.

    Returns:
        Handicap index rounded to one decimal place.
    """
    if len(scores) != len(pars):
        raise ValueError(
            f'scores and pars must be the same length '
            f'(got {len(scores)} and {len(pars)})'
        )
    if not scores or not pars:
        raise ValueError('both scores and pars must not be empty')

    average_differential = sum(s - p for s, p in zip(scores, pars)) / len(scores)
    return round_half_up(average_differential, 1)


tests: list[tuple[list[int], list[int], float]] = [
    ([72, 72, 72], [72, 72, 72], 0),
    ([80, 76, 78, 78], [72, 72, 72, 72], 6),
    ([42, 45, 46, 44], [36, 36, 36, 36], 8.3),
    ([85, 80, 76, 79, 82], [72, 72, 72, 71, 71], 8.8),
    ([41, 50, 48, 52, 46, 49], [35, 37, 35, 37, 35, 37], 11.7),
]


@mark.parametrize('scores, pars, expected', tests)
def test_calculate_handicap(
    scores: list[int], pars: list[int], expected: float
) -> None:
    assert calculate_handicap(scores, pars) == expected


if __name__ == '__main__':
    scores, pars, expected = tests[0]
    print(calculate_handicap(scores, pars))
