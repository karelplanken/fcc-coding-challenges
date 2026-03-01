# Daily Coding challenge #186 (2026-02-12) - freeCodeCamp.org
# 2026 Winter Games Day 7: Speed Skating
# Given two arrays representing the lap times (in seconds) for two speed skaters, return
# the lap number where the difference in lap times is the largest.

# The first element of each array corresponds to lap 1, the second to lap 2, and so on.
from dataclasses import dataclass

from pytest import mark


@dataclass
class LapTimeDelta:
    lap: int
    time_delta: float


def largest_difference(skater1: list[float], skater2: list[float]) -> int:
    lap_time_delta = LapTimeDelta(0, 0.0)

    for lap, (time_skater_1, time_skater_2) in enumerate(zip(skater1, skater2), 1):
        if (delta := abs(time_skater_1 - time_skater_2)) > lap_time_delta.time_delta:
            lap_time_delta.lap = lap
            lap_time_delta.time_delta = delta

    return lap_time_delta.lap


tests = [
    ([26.11, 25.80, 25.92, 26.23, 26.07], [25.93, 25.74, 26.53, 26.11, 26.30], 3),
    ([27.04, 25.94, 26.22, 26.07, 26.18], [25.59, 25.80, 26.11, 26.01, 26.23], 1),
    ([25.82, 25.90, 26.05, 26.00, 26.48], [25.85, 25.92, 26.07, 25.98, 25.95], 5),
    ([25.88, 26.10, 25.95, 26.05, 26.00], [25.90, 26.55, 25.92, 26.03, 26.01], 2),
    ([25.92, 26.01, 26.05, 25.88, 26.12], [25.95, 26.00, 26.03, 26.45, 26.10], 4),
]


@mark.parametrize('skater1, skater2, expected', tests)
def test_largest_difference(skater1: list, skater2: list, expected: int) -> None:
    assert largest_difference(skater1, skater2) == expected


if __name__ == '__main__':
    skater1, skater2, expected = tests[0]
    print(largest_difference(skater1, skater2))
