# Daily Coding challenge #315 (2026-06-21) - freeCodeCamp.org
# summer_solstice
# Today is the summer solstice, the longest day of the year in the Northern Hemisphere
# and the shortest in the Southern. Given a latitude, return a string representing
# daytime and nighttime hours.
#
# - The latitude will be between 90 (north pole) and -90 (south pole), inclusive
# - The number of daytime hours = 12 + (latitude / 90) * 12
# - Round the daytime hours to the nearest even number
#
# Return a 24-character string using `"☀️"` for daytime hours and `"🌑"` for nighttime
# hours, where:
#
# - Each character represents one hour, starting at midnight (hour 0)
# - Sunrise and sunset fall symmetrically around noon
#
# For example, a latitude of `0` (the equator) has 12 hours of daylight, so sunrise is
# at 6:00 AM and sunset is at 6:00 PM. Return: `"🌑🌑🌑🌑🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑🌑🌑🌑🌑"`.
from pytest import mark

HOURS_PER_DAY = 24
DAYTIME_SYMBOL = '☀️'
NIGHTTIME_SYMBOL = '🌑'


def get_daytime_hours(latitude: float) -> str:
    even_below, remainder = divmod(12 + (latitude / 90) * 12, 2)
    daytime_hours = int(even_below) * 2 + (2 if remainder > 1 else 0)

    sunrise = (HOURS_PER_DAY - daytime_hours) // 2
    sunset = sunrise + daytime_hours

    return (
        NIGHTTIME_SYMBOL * sunrise
        + DAYTIME_SYMBOL * daytime_hours
        + NIGHTTIME_SYMBOL * (HOURS_PER_DAY - sunset)
    )


tests = [
    (0, '🌑🌑🌑🌑🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑🌑🌑🌑🌑'),
    (90, '☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️'),
    (-90, '🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑'),
    (-33, '🌑🌑🌑🌑🌑🌑🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑🌑🌑🌑🌑🌑🌑'),
    (66.5, '🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑'),
    (40, '🌑🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑🌑'),
    (-50, '🌑🌑🌑🌑🌑🌑🌑🌑🌑☀️☀️☀️☀️☀️☀️🌑🌑🌑🌑🌑🌑🌑🌑🌑'),
]


@mark.parametrize('latitude, expected', tests)
def test_get_daytime_hours(latitude: float, expected: str) -> None:
    assert get_daytime_hours(latitude) == expected


if __name__ == '__main__':
    latitude, expected = tests[0]
    print(get_daytime_hours(latitude))
