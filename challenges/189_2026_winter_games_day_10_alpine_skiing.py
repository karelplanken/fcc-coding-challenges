# Daily Coding challenge #189 (2026-02-14) - freeCodeCamp.org
# 2026 Winter Games Day 10: Alpine Skiing
# Given a ski hill's vertical drop, horizontal distance, and type, determine the
# difficulty rating of the hill.

# To determine the rating:

# Calculate the steepness of the hill by taking the drop divided by the distance.
# Then, calculate the adjusted steepness based on the hill type:
# "Downhill" multiply steepness by 1.2
# "Slalom": multiply steepness by 0.9
# "Giant Slalom": multiply steepness by 1.0
# Return:

# "Green" if the adjusted steepness is less than or equal to 0.1
# "Blue" if the adjusted steepness is greater than 0.1 and less than or equal to 0.25
# "Black" if the adjusted steepness is greater than 0.25
from bisect import bisect_left
from dataclasses import dataclass
from operator import attrgetter
from types import MappingProxyType

from pytest import mark

STEEPNESS_FACTOR = MappingProxyType(
    {
        'Downhill': 1.2,
        'Slalom': 0.9,
        'Giant Slalom': 1.0,
    }
)


@dataclass
class Rating:
    threshold: float
    name: str


THRESHOLD_GETTER = attrgetter('threshold')

RATING_THRESHOLDS = [
    Rating(threshold=0.00, name='Green'),
    Rating(threshold=0.10, name='Blue'),
    Rating(threshold=0.25, name='Black'),
]


def get_hill_rating(drop: int, distance: int, hill_type: str) -> str:
    adjusted_steepness = (drop / distance) * STEEPNESS_FACTOR[hill_type]
    idx = bisect_left(RATING_THRESHOLDS, adjusted_steepness, key=THRESHOLD_GETTER)
    return RATING_THRESHOLDS[idx - 1].name


tests = [
    (95, 900, 'Slalom', 'Green'),
    (620, 2800, 'Downhill', 'Black'),
    (420, 1680, 'Giant Slalom', 'Blue'),
    (250, 3000, 'Downhill', 'Green'),
    (110, 900, 'Slalom', 'Blue'),
    (380, 1500, 'Giant Slalom', 'Black'),
]


@mark.parametrize('drop, distance, hill_type, expected', tests)
def test(drop: int, distance: int, hill_type: str, expected: str) -> None:
    assert get_hill_rating(drop, distance, hill_type) == expected


if __name__ == '__main__':
    drop, distance, hill_type, expected = tests[0]
    print(get_hill_rating(drop, distance, hill_type))
