# Daily Coding challenge #214 (2026-03-12) - freeCodeCamp.org
# Domino Chain Validator
# Given a 2D array representing a sequence of dominoes, determine whether it forms a
# valid chain.

# Each element in the array represents a domino and will be an array of two numbers
# from 1 to 6, (inclusive).
# For the chain to be valid, the second number of each domino must match the first
# number of the next domino.
# The first number of the first domino and the last number of the last domino don't
# need to match anything.
from itertools import pairwise

from pytest import mark


def is_valid_domino_chain(dominoes: list[list[int]]) -> bool:
    return all(
        head[-1] == tail[0] for head, tail in pairwise(dominoes)
    )


tests = [
    ([[1, 3], [3, 6], [6, 5]], True),
    ([[6, 2], [3, 4], [4, 1]], False),
    ([[2, 5], [5, 6], [5, 1]], False),
    (
        [
            [4, 3],
            [3, 1],
            [1, 6],
            [6, 6],
            [6, 5],
            [5, 1],
            [1, 1],
            [1, 4],
            [4, 4],
            [4, 2],
        ],
        True,
    ),
    (
        [
            [2, 3],
            [3, 3],
            [3, 6],
            [6, 1],
            [1, 4],
            [3, 5],
            [5, 5],
            [5, 4],
            [4, 2],
            [2, 2],
        ],
        False,
    ),
]


@mark.parametrize('dominoes, expected', tests)
def test_is_valid_domino_chain(dominoes: list[list[int]], expected: bool) -> None:
    assert is_valid_domino_chain(dominoes) == expected


if __name__ == '__main__':
    dominoes, expected = tests[1]
    print(is_valid_domino_chain(dominoes))
