"""Daily Coding Challenge #56 (2025-10-05) - freeCodeCamp.org."""

# Space Week Day 2: Exoplanet Search
# For the second day of Space Week, you are given a string where each character
# represents the luminosity reading of a star. Determine if the readings have detected
# an exoplanet using the transit method. The transit method is when a planet passes in
# front of a star, reducing its observed luminosity.
#
# - Luminosity readings only comprise of characters 0-9 and A-Z where each reading
#   corresponds to the following numerical values:
# - Characters 0-9 correspond to luminosity levels 0-9.
# - Characters A-Z correspond to luminosity levels 10-35.
#
# A star is considered to have an exoplanet if any single reading is less than or equal
# to 80% of the average of all readings. For example, if the average luminosity of a
# star is 10, it would be considered to have a exoplanet if any single reading is 8 or
# less.
import string
from types import MappingProxyType

from pytest import mark

_SYMBOLS = string.digits + string.ascii_uppercase  # '0'-'9' -> 0-9, 'A'-'Z' -> 10-35
_READING_VALUE: MappingProxyType[str, int] = MappingProxyType({
    char: value for value, char in enumerate(_SYMBOLS)
})


def _get_reading_value(char: str) -> int:
    try:
        return _READING_VALUE[char]
    except KeyError:
        msg = f'invalid character {char!r}: expected 0-9 or A-Z'
        raise ValueError(msg) from None


def has_exoplanet(readings: str) -> bool:
    """Determine if the readings have detected an exoplanet using the transit method.

    The transit method is when a planet passes in front of a star, reducing its observed
    luminosity. A star is considered to have an exoplanet if any single reading is less
    than or equal to 80% of the average of all readings.

    Args:
        readings: Characters representing luminosity readings of a star.

    Returns:
        True if the star has an exoplanet, False otherwise.

    Raises:
        ValueError: If readings is empty or contains a character outside 0-9 and A-Z.
    """
    if not readings:
        msg = 'readings must not be empty'
        raise ValueError(msg)
    values = [_get_reading_value(char) for char in readings]
    # min <= 0.8 * sum / n  <=>  5 * min * n <= 4 * sum  (exact integer arithmetic)
    return 5 * min(values) * len(values) <= 4 * sum(values)


tests = [
    ('665544554', False),
    ('FGFFCFFGG', True),
    ('MONOPLONOMONPLNOMPNOMP', False),
    ('FREECODECAMP', True),
    ('9AB98AB9BC98A', False),
    ('ZXXWYZXYWYXZEGZXWYZXYGEE', True),
]


@mark.parametrize('readings, expected', tests)
def test_has_exoplanet(readings: str, expected: bool) -> None:
    """Test has_exoplanet function."""
    assert has_exoplanet(readings) == expected


if __name__ == '__main__':
    readings, expected = tests[0]
    print(has_exoplanet(readings))
