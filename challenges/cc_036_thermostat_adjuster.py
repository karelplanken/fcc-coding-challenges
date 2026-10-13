"""Daily Coding Challenge #36 (2025-09-15) - freeCodeCamp.org."""

# Thermostat Adjuster
# Given the current temperature of a room and a target temperature, return a string
# indicating how to adjust the room temperature based on these constraints:
#
# - Return "heat" if the current temperature is below the target.
# - Return "cool" if the current temperature is above the target.
# - Return "hold" if the current temperature is equal to the target.
from pytest import mark


def adjust_thermostat(temp: int | float, target: int | float) -> str:
    """Return how to adjust the thermostat based on current and target temperatures.

    Args:
        temp: Current temperature of the room.
        target: Target temperature.

    Returns:
        'heat' if temp is below target, 'cool' if above, 'hold' if equal.

    Raises:
        ValueError: If temp or target is NaN (or otherwise fails all three
            comparisons against a valid number).

    Note:
        Raises rather than silently returning 'hold' on invalid input. Under
        IEEE 754, NaN fails '<', '>', and '==' against any value, so a naive
        if/elif/else would fall through to 'hold' on a bad reading (e.g. a
        malfunctioning sensor) — telling the system to do nothing, which is
        the least safe response to a temperature that isn't actually known.
        Failing loudly here surfaces the bad data at the source instead of
        propagating a wrong-but-plausible-looking answer downstream.
    """
    if temp < target:
        return 'heat'
    if temp > target:
        return 'cool'
    if temp == target:
        return 'hold'
    msg = 'temp and target must be valid, non-NaN numbers (int or float)'
    raise ValueError(msg)


tests: list[tuple[float, float, str]] = [
    (68, 72, 'heat'),
    (75, 72, 'cool'),
    (72, 72, 'hold'),
    (-20.5, -10.1, 'heat'),
    (100, 99.9, 'cool'),
    (0.0, 0.0, 'hold'),
]


@mark.parametrize('temp, target, expected', tests)
def test_adjust_thermostat(temp: float, target: float, expected: str) -> None:
    """Test adjust_thermostat function."""
    assert adjust_thermostat(temp, target) == expected


if __name__ == '__main__':
    temp, target, expected = tests[0]
    print(adjust_thermostat(temp, target))
