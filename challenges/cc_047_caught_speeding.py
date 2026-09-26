"""Daily Coding Challenge #47 (2025-09-26) - freeCodeCamp.org."""

# Caught Speeding
# Given an array of numbers representing the speed at which vehicles were observed
# traveling, and a number representing the speed limit, return an array with two items,
# the number of vehicles that were speeding, followed by the average amount beyond the
# speed limit of those vehicles.
#
# - If there were no vehicles speeding, return [0, 0].
from pytest import mark


def speeding(speeds: list[int], limit: int) -> list[int | float]:
    """Return the number of speeding vehicles and their average excess speed.

    Speeds are treated as magnitudes, so negative values are rejected.

    Args:
        speeds: Observed vehicle speeds.
        limit: The speed limit.

    Returns:
        A two-item list: the number of speeding vehicles and their average
        amount over the limit, or [0, 0] if no vehicle was speeding.

    Raises:
        ValueError: If the limit or any speed is negative.
    """
    if limit < 0:
        msg = 'speed limit must be non-negative'
        raise ValueError(msg)
    if any(speed < 0 for speed in speeds):
        msg = 'speeds must be non-negative'
        raise ValueError(msg)

    excess = [speed - limit for speed in speeds if speed > limit]
    if not excess:
        return [0, 0]

    count = len(excess)
    return [count, sum(excess) / count]


tests: list[tuple[list[int], int, list[int | float]]] = [
    ([50, 60, 55], 60, [0, 0]),
    ([58, 50, 60, 55], 55, [2, 4]),
    ([61, 81, 74, 88, 65, 71, 68], 70, [4, 8.5]),
    ([100, 105, 95, 102], 100, [2, 3.5]),
    ([40, 45, 44, 50, 112, 39], 55, [1, 57]),
]


@mark.parametrize('speeds, limit, expected', tests)
def test_speeding(speeds: list[int], limit: int, expected: list[int | float]) -> None:
    """Test speeding function."""
    assert speeding(speeds, limit) == expected


if __name__ == '__main__':
    speeds, limit, expected = tests[1]
    print(speeding(speeds, limit))
