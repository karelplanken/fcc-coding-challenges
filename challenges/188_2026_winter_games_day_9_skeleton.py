# Daily Coding challenge #188 (2026-02-14) - freeCodeCamp.org
# 2026 Winter Games Day 9: Skeleton
# Given a string representing the curves on a skeleton track, determine the difficulty
# of the track.

# The given string will only consist of the letters:

# "L" for a left turn
# "R" for a right turn
# "S" for a straight segment
# Each direction change adds 15 points (an "L" followed by an "R" or vice versa).

# All other curves add 5 points each (all other "L" or "R" characters).

# Straight segments add 0 points.

# The difficulty of the track is based on the total score. Return:

# "Easy" if the total is 0 - 100
# "Medium" if the total is 101-200
# "Hard" if the total is over 200
# from collections import Counter
# from itertools import pairwise
from pytest import mark


def get_difficulty(track: str) -> str:
    score = 5 if track and track[0] in 'LR' else 0

    # Using zip:
    score += sum(
        15 if prev != 'S' and prev != curr else 5
        for prev, curr in zip(track, track[1:])
        if curr != 'S'
    )

    return 'Easy' if score <= 100 else 'Medium' if score <= 200 else 'Hard'


tests = [
    ('SLSLLSRRLSRLRL', 'Easy'),
    ('LLRSLRLRSLLRLRSLRRLRSRLLS', 'Hard'),
    ('SRRRRLSLLRLRSSRLSRL', 'Medium'),
    ('LSRLRLSRLRLSLRSLRLLRLSRLRLRSL', 'Hard'),
    ('SLLSSLRLSLSLRSLSSLRL', 'Medium'),
    ('SRSLSRSLSRRSLSRSRSLSRLSRSR', 'Easy'),
]


@mark.parametrize('track, expected', tests)
def test(track: str, expected: str) -> None:
    assert get_difficulty(track) == expected


if __name__ == '__main__':
    track, expected = tests[5]
    print(get_difficulty(track))
