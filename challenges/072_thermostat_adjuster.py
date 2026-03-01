# Daily Coding challenge #72 (2025-10-21) - freeCodeCamp.org
# Thermostat Adjuster 2
# Given the current temperature of a room in Fahrenheit and a target temperature in
# Celsius, return a string indicating how to adjust the room temperature based on these
# constraints:

# Return "Heat: X degrees Fahrenheit" if the current temperature is below the target.
# With X being the number of degrees in Fahrenheit to heat the room to reach the
# target, rounded to 1 decimal place.
# Return "Cool: X degrees Fahrenheit" if the current temperature is above the target.
# With X being the number of degrees in Fahrenheit to cool the room to reach the
# target, rounded to 1 decimal place.
# Return "Hold" if the current temperature is equal to the target.
# To convert Celsius to Fahrenheit, multiply the Celsius temperature by 1.8 and add 32
# to the result (F = (C * 1.8) + 32).
from pytest import mark


def adjust_thermostat(current_f: int, target_c: int) -> str:
    target_fahrenheit = target_c * 1.8 + 32
    delta_fahrenheit = target_fahrenheit - current_f

    if delta_fahrenheit > 0:
        return f'Heat: {delta_fahrenheit:.1f} degrees Fahrenheit'
    elif delta_fahrenheit < 0:
        return f'Cool: {abs(delta_fahrenheit):.1f} degrees Fahrenheit'
    else:
        return 'Hold'


tests = [
    (32, 0, 'Hold'),
    (70, 25, 'Heat: 7.0 degrees Fahrenheit'),
    (72, 18, 'Cool: 7.6 degrees Fahrenheit'),
    (212, 100, 'Hold'),
    (59, 22, 'Heat: 12.6 degrees Fahrenheit'),
]


@mark.parametrize('current_f, target_c, expected', tests)
def test_adjust_thermostat(current_f: int, target_c: int, expected: str) -> None:
    assert adjust_thermostat(current_f, target_c) == expected


if __name__ == '__main__':
    current_f, target, expected = tests[0]
    print(adjust_thermostat(current_f, target))
