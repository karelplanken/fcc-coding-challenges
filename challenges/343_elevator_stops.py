# Daily Coding challenge #343 (2026-07-19) - freeCodeCamp.org
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
    floors_stops = sorted(stops)
    current_floor_idx = bisect_right(floors_stops, current_floor)

    stops_below = [floor for floor in reversed(floors_stops[:current_floor_idx])]
    stops_above = floors_stops[current_floor_idx:]

    travel_up = max(stops_above) - current_floor if stops_above else 0
    travel_down = current_floor - min(stops_below) if stops_below else 0

    return (
        stops_below + stops_above
        if travel_down < travel_up
        else stops_above + stops_below
    )


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
    assert elevator_stops(current_floor, stops) == expected


if __name__ == '__main__':
    current_floor, stops, expected = tests[4]
    print(elevator_stops(current_floor, stops))
