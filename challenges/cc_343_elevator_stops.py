"""Daily Coding Challenge #343 (2026-07-19) - freeCodeCamp.org."""

# Elevator Stops
# Given a number for the current floor of an elevator and an array of requested floors,
# return an array of the order the elevator should visit them to minimize number of
# floors traveled.
#
# - If tied, go up first
# - Floors with a request must be visited when the elevator first passes them
from bisect import bisect_right

from pytest import mark


def elevator_stops(current_floor: int, stops: list[int]) -> list[int]:
    """SCAN-ordered elevator stops (see: elevator/disk-scheduling algorithm).

    Assumes current_floor is not itself in stops (elevator is already there),
    and stops contains no duplicates (a floor button press adds one request).

    Args:
        current_floor: current floor of the elevator
        stops: list of requested floors

    Returns:
        list of floors in the order the elevator should visit them
    """
    floors_stops = sorted(stops)
    current_floor_idx = bisect_right(floors_stops, current_floor)

    below = list(
        reversed(floors_stops[:current_floor_idx])
    )  # closest-first, descending
    above = floors_stops[current_floor_idx:]  # closest-first, ascending

    dist_up = max(above, default=current_floor) - current_floor
    dist_down = current_floor - min(below, default=current_floor)

    return below + above if dist_down < dist_up else above + below


tests = [
    (5, [2, 8, 3, 9], [3, 2, 8, 9]),
    (6, [2, 10, 8, 3, 1, 9], [8, 9, 10, 3, 2, 1]),
    (1, [4, 8, 3, 6, 9], [3, 4, 6, 8, 9]),
    (12, [6, 10, 7, 3, 1, 4], [10, 7, 6, 4, 3, 1]),
    (11, [2, 8, 23, 5, 12, 10, 6, 9, 19], [10, 9, 8, 6, 5, 2, 12, 19, 23]),
]


@mark.parametrize('current_floor, stops, expected', tests)
def test_elevator_stops(
    current_floor: int, stops: list[int], expected: list[int]
) -> None:
    """Test elevator_stops function."""
    assert elevator_stops(current_floor, stops) == expected


if __name__ == '__main__':
    current_floor, stops, expected = tests[4]
    print(elevator_stops(current_floor, stops))
