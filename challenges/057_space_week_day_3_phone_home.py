# Daily Coding challenge #57 (2025-10-06) - freeCodeCamp.org
# Space Week Day 3: Phone Home
# For day three of Space Week, you are given an array of numbers representing distances
# (in kilometers) between yourself, satellites, and your home planet in a communication
# route. Determine how long it will take a message sent through the route to reach its
# destination planet using the following constraints:

# The first value in the array is the distance from your location to the first
# satellite.
# Each subsequent value, except for the last, is the distance to the next satellite.
# The last value in the array is the distance from the previous satellite to your home
# planet.
# The message travels at 300,000 km/s.
# Each satellite the message passes through adds a 0.5 second transmission delay.
# Return a number rounded to 4 decimal places, with trailing zeros removed.
from pytest import mark

LIGHT_SPEED_KM_S = 300_000
SATELLITE_DELAY_S = 0.5


def send_message(route: list[int]) -> float:
    travel_time = sum(route) / LIGHT_SPEED_KM_S
    processing_time = (len(route) - 1) * SATELLITE_DELAY_S
    # Rounding to 4 decimal places removes trailing zeros automatically
    return round(travel_time + processing_time, 4)


tests = [
    ([300000, 300000], 2.5),
    ([384400, 384400], 3.0627),
    ([54600000, 54600000], 364.5),
    ([1000000, 500000000, 1000000], 1674.3333),
    ([10000, 21339, 50000, 31243, 10000], 2.4086),
    ([802101, 725994, 112808, 3625770, 481239], 21.1597),
]


@mark.parametrize('route, expected', tests)
def test_send_message(route: list[int], expected: str) -> None:
    assert send_message(route) == expected


if __name__ == '__main__':
    route, expected = tests[0]
    print(send_message(route))
