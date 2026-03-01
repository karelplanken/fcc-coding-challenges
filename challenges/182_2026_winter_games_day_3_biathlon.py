# Daily Coding challenge #182 (2026-02-08) - freeCodeCamp.org
# 2026 Winter Games Day 3: Biathlon
# Given an array of integers, where each value represents the number of targets hit in
# a single round of a biathlon, return the total penalty distance the athlete must ski.

# Each round consists of 5 targets.
# Each missed target results in a 150 meter penalty loop.
from pytest import mark


# More Pythonic and concise
def calculate_penalty_distance(rounds: list[int]) -> int:
    PENALTY_PER_MISS = 150
    TARGETS_PER_ROUND = 5
    return sum((TARGETS_PER_ROUND - hits) * PENALTY_PER_MISS for hits in rounds)


# # Verbose and simple
# def calculate_penalty_distance(rounds: list[int]) -> int:
#     PENALTY_PER_MISS = 150
#     TARGETS_PER_ROUND = 5
#     total_penalty = 0

#     for hits in rounds:
#         if (missed := TARGETS_PER_ROUND - hits):
#             total_penalty += missed * PENALTY_PER_MISS

#     return total_penalty


tests = [
    ([4, 4], 300),
    ([5, 5], 0),
    ([4, 5, 3, 5], 450),
    ([5, 4, 5, 5], 150),
    ([4, 3, 0, 3], 1500),
]


@mark.parametrize('rounds, expected', tests)
def test_solution(rounds: list[int], expected: int) -> None:
    assert calculate_penalty_distance(rounds) == expected


if __name__ == '__main__':
    rounds, expected = tests[0]
    print(calculate_penalty_distance(rounds))
