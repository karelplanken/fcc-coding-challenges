# Daily Coding challenge #302 (2026-06-08) - freeCodeCamp.org
# Jet Lagged
# Given a departure city, an arrival city, a flight duration in hours, and a direction
# of travel, return the number of jet lag hours the traveler is experiencing.

# The given cities will be from the following list that includes their UTC offset:

# City	Offset
# "Los Angeles"	-8
# "New York"	-5
# "London"	0
# "Istanbul"	+3
# "Dubai"	+4
# "Hong Kong"	+8
# "Tokyo"	+9
# To calculate jet lag hours:

# Find the timezone difference in hours between the two cities.
# Determine the direction multiplier. If travelling "east", it's 1.5, otherwise,
# it's 1.0.
# Get the jet lag hours with the formula:
# timezone difference + (flight duration * 0.1) * direction multiplier
# Return the jet lag hours rounded to one decimal place.
from enum import StrEnum

from pytest import mark


class Direction(StrEnum):
    EAST = 'east'
    WEST = 'west'

    @property
    def multiplier(self) -> float:
        return 1.5 if self is Direction.EAST else 1.0


TZ_OFFSET = {
    'Los Angeles': -8,
    'New York': -5,
    'London': 0,
    'Istanbul': +3,
    'Dubai': +4,
    'Hong Kong': +8,
    'Tokyo': +9,
}


def get_jet_lag_hours(
    departure_city: str, arrival_city: str, flight_duration: float, direction: str
) -> float:
    tz_diff = abs(TZ_OFFSET[departure_city] - TZ_OFFSET[arrival_city])
    flight_fatigue = (flight_duration * 0.1) * Direction(direction).multiplier
    return round(tz_diff + flight_fatigue, 1)


tests = [
    ('Istanbul', 'Hong Kong', 10, 'east', 6.5),
    ('London', 'New York', 8, 'west', 5.8),
    ('Hong Kong', 'Tokyo', 4, 'east', 1.6),
    ('Dubai', 'London', 7, 'west', 4.7),
    ('Los Angeles', 'Hong Kong', 15, 'west', 17.5),
    ('Tokyo', 'Dubai', 9, 'west', 5.9),
    ('New York', 'Istanbul', 10, 'east', 9.5),
]


@mark.parametrize(
    'departure_city, arrival_city, flight_duration, direction, expected', tests
)
def test(
    departure_city: str,
    arrival_city: str,
    flight_duration: float,
    direction: str,
    expected: float,
) -> None:
    assert (
        get_jet_lag_hours(departure_city, arrival_city, flight_duration, direction)
        == expected
    )


if __name__ == '__main__':
    departure_city, arrival_city, flight_duration, direction, expected = tests[0]
    print(get_jet_lag_hours(departure_city, arrival_city, flight_duration, direction))
