# Daily Coding challenge #47 (2025-09-26) - freeCodeCamp.org
# Caught Speeding
# Given an array of numbers representing the speed at which vehicles were observed
# traveling, and a number representing the speed limit, return an array with two items,
# the number of vehicles that were speeding, followed by the average amount beyond the
# speed limit of those vehicles.
from pytest import mark


# If there were no vehicles speeding, return [0, 0].
def speeding(speeds: list[int], limit: int) -> list[float]:
    """Return [count of speeders, average excess speed]"""
    excess_speeds = [speed - limit for speed in speeds if speed > limit]

    if not excess_speeds:
        return [0, 0]

    return [len(excess_speeds), sum(excess_speeds) / len(excess_speeds)]


# Memory efficient version:
# def speeding(speeds: list[int], limit: int) -> list[float]:
#     """Return [count of speeders, average excess speed]"""
#     speeder_count = 0
#     total_excess = 0

#     for speed in speeds:
#         if speed > limit:
#             speeder_count += 1
#             total_excess += speed - limit

#     if speeder_count == 0:
#         return [0, 0]

#     average_excess = total_excess / speeder_count
#     return [speeder_count, average_excess]

tests = [
    ([50, 60, 55], 60, [0, 0]),
    ([58, 50, 60, 55], 55, [2, 4]),
    ([61, 81, 74, 88, 65, 71, 68], 70, [4, 8.5]),
    ([100, 105, 95, 102], 100, [2, 3.5]),
    ([40, 45, 44, 50, 112, 39], 55, [1, 57]),
]


@mark.parametrize('speeds, limit, expected', tests)
def test_speeding(speeds: list[int], limit: int, expected: list[float]) -> None:
    assert speeding(speeds, limit) == expected


if __name__ == '__main__':
    speeds, limit, expected = tests[1]
    print(speeding(speeds, limit))
