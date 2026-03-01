# Daily Coding challenge #185 (2026-02-11) - freeCodeCamp.org
# 2026 Winter Games Day 6: Figure Skating
# Given an array of judge scores and optional penalties, calculate the final score for
# a figure skating routine.

# The first argument is an array of 10 judge scores, each a number from 0 to 10. Remove
# the highest and lowest judge scores and sum the remaining 8 scores to get the base
# score.

# Any additional arguments passed to the function are penalties. Subtract all penalties
# from the base score to get the final score.
from pytest import mark


def compute_score(judge_scores: list[float], *penalties: float) -> float:
    return sum(sorted(judge_scores)[1:-1]) - sum(penalties)


tests = [
    ([10, 8, 9, 6, 9, 8, 8, 9, 7, 7], (1,), 64),
    ([10, 10, 10, 10, 10, 10, 10, 10, 10, 10], (), 80),
    ([10, 8, 9, 10, 9, 8, 8, 9, 10, 7], (1, 2, 1), 67),
    ([8.0, 8.5, 9.0, 8.5, 9.0, 8.0, 9.0, 8.5, 9.0, 8.5], (0.5, 1.0), 67.5),
    ([6.0, 8.5, 7.0, 9.0, 7.5, 8.0, 6.5, 9.5, 7.0, 8.0], (1.5, 0.5, 0.5), 59),
]


@mark.parametrize('judge_scores, penalties, expected', tests)
def test_compute_score(
    judge_scores: list[float], penalties: tuple[float], expected: float
) -> None:
    assert compute_score(judge_scores, *penalties) == expected


if __name__ == '__main__':
    judge_scores, penalties, expected = tests[0]
    print(compute_score(judge_scores, *penalties))
