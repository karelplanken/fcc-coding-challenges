# Daily Coding challenge #192 (2026-02-18) - freeCodeCamp.org
# 2026 Winter Games Day 13: Nordic Combined
# Given an array of jump scores for athletes, calculate their start delay times for the
# cross-country portion of the Nordic Combined.

# The athlete with the highest jump score starts first (0 second delay). All other
# athletes start later based on how far behind their jump score is compared to the best
# jump.

# To calculate the delay for each athlete, subtract the athlete's jump score from the
# best overall jump score and multiply the result by 1.5. Round the delay up to the
# nearest integer.
import math

from pytest import mark


def calculate_start_delays(jump_scores: list[int]) -> list[int]:
    best_score = max(jump_scores)

    return [math.ceil((best_score - score) * 1.5) for score in jump_scores]


tests = [
    ([120, 110, 125], [8, 23, 0]),
    ([118, 125, 122, 120], [11, 0, 5, 8]),
    ([100, 105, 95, 110, 120, 115, 108], [30, 23, 38, 15, 0, 8, 18]),
    (
        [130, 125, 128, 120, 118, 122, 127, 115, 132, 124],
        [3, 11, 6, 18, 21, 15, 8, 26, 0, 12],
    ),
]


@mark.parametrize('jump_scores, expected', tests)
def test_calculate_start_delays(jump_scores: list[int], expected: list[int]) -> None:
    assert calculate_start_delays(jump_scores) == expected


if __name__ == '__main__':
    jump_scores, expected = tests[1]
    print(calculate_start_delays(jump_scores))
