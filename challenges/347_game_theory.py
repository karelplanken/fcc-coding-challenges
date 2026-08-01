# Daily Coding challenge #347 (2026-07-23) - freeCodeCamp.org
# Game Theory
# Given two equal length strings representing two players' strategies for a game, return
# the scores as an array [player1, player2].
#
# - The given strings will only contain one of two letters: "C" (cooperate) or "D"
#   (defect).
# - Each character represents one round, scored as follows:
#   - If both players cooperate, each scores 3.
#   - If both players defect, each scores 1.
#   - If one player defects and the other cooperates, the defector scores 5 and the
# cooperator scores 0.
from collections import Counter
from types import MappingProxyType
from typing import NamedTuple

from pytest import mark


class PlayerScores(NamedTuple):
    player1: int
    player2: int


STRATEGIES_TO_SCORES = MappingProxyType({
    ('C', 'C'): PlayerScores(3, 3),
    ('D', 'D'): PlayerScores(1, 1),
    ('C', 'D'): PlayerScores(0, 5),
    ('D', 'C'): PlayerScores(5, 0),
})


def play_game(p1: str, p2: str) -> list[int]:
    """Returns the total score for players p1 and p2.

    Assumes p1 and p2 contain only 'C'/'D' and are the same length
    (if not, the shorter length is respected). Empty input yields [0, 0].
    """
    score1 = score2 = 0
    for game, n in Counter(zip(p1, p2)).items():
        outcome = STRATEGIES_TO_SCORES[game]
        score1 += n * outcome.player1
        score2 += n * outcome.player2
    return [score1, score2]


tests = [
    ('CCCC', 'CCCC', [12, 12]),
    ('DDDD', 'DDDD', [4, 4]),
    ('CCDD', 'CDDD', [5, 10]),
    ('CCCDCDCCCDDC', 'CCDDCDCDDCCD', [24, 34]),
    ('DDCCDDDDCDDCDDDCDD', 'CCDCCCDCCCDCCCCDCC', [66, 21]),
]


@mark.parametrize('p1, p2, expected', tests)
def test_play_game(p1: str, p2: str, expected: list[int]) -> None:
    assert play_game(p1, p2) == expected


if __name__ == '__main__':
    p1, p2, expected = tests[0]
    print(play_game(p1, p2))
