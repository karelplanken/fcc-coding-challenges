# Daily Coding challenge #133 (2025-12-21) - freeCodeCamp.org
# Daylight Hours
# December 21st is the winter solstice for the northern hemisphere and the summer
# solstice for the southern hemisphere. That means it's the day with the least daylight
# in the north and the most daylight in the south.

# Given a latitude number from -90 to 90, return a rough approximation of daylight
# hours on the solstice using the following table:

# Latitude	Daylight Hours
# -90	24
# -75	23
# -60	21
# -45	15
# -30	13
# -15	12
# 0	12
# 15	11
# 30	10
# 45	9
# 60	6
# 75	2
# 90	0
# If the given latitude does not exactly match a table entry, use the value of the
# closest latitude.
from pytest import mark

LATITUDE_HOURS = {
    -90: 24,
    -75: 23,
    -60: 21,
    -45: 15,
    -30: 13,
    -15: 12,
    0: 12,
    15: 11,
    30: 10,
    45: 9,
    60: 6,
    75: 2,
    90: 0,
}


def daylight_hours(latitude: int) -> int:
    if latitude < -90 or latitude > 90:
        raise ValueError(f'Latitude must be between -90 and 90, got {latitude}')
    return LATITUDE_HOURS[15 * round(latitude / 15)]


tests = [(45, 9), (0, 12), (-90, 24), (-10, 12), (23, 10), (88, 0), (-33, 13), (70, 2)]


@mark.parametrize('latitude, expected', tests)
def test_daylight_hours(latitude: int, expected: int) -> None:
    assert daylight_hours(latitude) == expected


if __name__ == '__main__':
    latitude, expected = tests[0]
    print(daylight_hours(100))
