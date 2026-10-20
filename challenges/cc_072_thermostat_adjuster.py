"""Daily Coding Challenge #72 (2025-10-21) - freeCodeCamp.org."""

# Thermostat Adjuster 2
# Given the current temperature of a room in Fahrenheit and a target temperature in
# Celsius, return a string indicating how to adjust the room temperature based on these
# constraints:
#
# - Return "Heat: X degrees Fahrenheit" if the current temperature is below the target.
#   With X being the number of degrees in Fahrenheit to heat the room to reach the
#   target, rounded to 1 decimal place.
# - Return "Cool: X degrees Fahrenheit" if the current temperature is above the target.
#   With X being the number of degrees in Fahrenheit to cool the room to reach the
#   target, rounded to 1 decimal place.
# - Return "Hold" if the current temperature is equal to the target.
#
# To convert Celsius to Fahrenheit, multiply the Celsius temperature by 1.8 and add 32
# to the result (F = (C * 1.8) + 32).
from pytest import mark


def _celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit.

    Args:
        celsius: The temperature in Celsius.

    Returns:
        The temperature in Fahrenheit.
    """
    return celsius * 9 / 5 + 32


def adjust_thermostat(current_f: float, target_c: float) -> str:
    """Determine how to adjust the room temperature to reach the target.

    Args:
        current_f: The current temperature in Fahrenheit.
        target_c: The target temperature in Celsius.

    Returns:
        'Hold' if the temperatures are equal at 0.1 °F display precision,
        otherwise 'Heat: X degrees Fahrenheit' or 'Cool: X degrees Fahrenheit'
        with X the absolute difference rounded to one decimal place.
    """
    delta = round(_celsius_to_fahrenheit(target_c) - current_f, 1)
    if delta == 0:
        return 'Hold'
    action = 'Heat' if delta > 0 else 'Cool'
    return f'{action}: {abs(delta):.1f} degrees Fahrenheit'


tests = [
    (32, 0, 'Hold'),
    (70, 25, 'Heat: 7.0 degrees Fahrenheit'),
    (72, 18, 'Cool: 7.6 degrees Fahrenheit'),
    (212, 100, 'Hold'),
    (59, 22, 'Heat: 12.6 degrees Fahrenheit'),
]


@mark.parametrize('current_f, target_c, expected', tests)
def test_adjust_thermostat(current_f: int, target_c: int, expected: str) -> None:
    """Test adjust_thermostat function."""
    assert adjust_thermostat(current_f, target_c) == expected


if __name__ == '__main__':
    current_f, target, expected = tests[0]
    print(adjust_thermostat(current_f, target))
