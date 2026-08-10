# Daily Coding challenge #364 (2026-08-09) - freeCodeCamp.org
# Between Two Buckets
# Given two buckets of paint, each with an RGB color and a fullness level, return the
# mixed RGB color as an array of three integers.
#
# - Each bucket is an object (JavaScript) or dictionary (Python) with a color property
#   (an array of three integers [r, g, b]) and a fullness property (0–100).
# - The mixed color is a weighted average of each channel in the two colors based on
#   fullness level, with each channel rounded to the nearest integer.
from math import floor
from typing import TypedDict

from pytest import mark


class Bucket(TypedDict):
    color: list[int]
    fullness: int


def mix_paint(bucket1: Bucket, bucket2: Bucket) -> list[int]:
    """Mix two paint buckets into a fullness-weighted average RGB color.

    Each bucket has a `color` ([r, g, b]) and a `fullness` (0-100). The result
    is each channel's weighted average, rounded half-up (not banker's rounding)
    to the nearest integer. If the color arrays differ in length, the shorter
    one determines the result length (via `zip`).

    Args:
        bucket1: First bucket's color and fullness.
        bucket2: Second bucket's color and fullness.

    Raises:
        ZeroDivisionError: if both buckets' fullness is 0.

    Returns:
        The mixed RGB color as [r, g, b].
    """
    w1, w2 = bucket1['fullness'], bucket2['fullness']
    total = w1 + w2
    return [
        floor((c1 * w1 + c2 * w2) / total + 0.5)
        for c1, c2 in zip(bucket1['color'], bucket2['color'])
    ]


tests: list[tuple[Bucket, Bucket, list[int]]] = [
    (
        {'color': [250, 250, 250], 'fullness': 50},
        {'color': [0, 0, 0], 'fullness': 50},
        [125, 125, 125],
    ),
    (
        {'color': [250, 250, 250], 'fullness': 80},
        {'color': [0, 0, 0], 'fullness': 20},
        [200, 200, 200],
    ),
    (
        {'color': [100, 150, 200], 'fullness': 30},
        {'color': [100, 150, 200], 'fullness': 70},
        [100, 150, 200],
    ),
    (
        {'color': [143, 143, 101], 'fullness': 45},
        {'color': [100, 204, 204], 'fullness': 90},
        [114, 184, 170],
    ),
    (
        {'color': [15, 134, 249], 'fullness': 29},
        {'color': [97, 178, 55], 'fullness': 54},
        [68, 163, 123],
    ),
]


@mark.parametrize('bucket1, bucket2, expected', tests)
def test_mix_paint(bucket1: Bucket, bucket2: Bucket, expected: list[int]) -> None:
    assert mix_paint(bucket1, bucket2) == expected


if __name__ == '__main__':
    bucket1, bucket2, expected = tests[2]
    print(mix_paint(bucket1, bucket2))
