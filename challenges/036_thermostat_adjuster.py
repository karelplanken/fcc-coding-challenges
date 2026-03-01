# Daily Coding challenge #36 (2025-09-15) - freeCodeCamp.org
# Thermostat Adjuster
# Given the current temperature of a room and a target temperature, return a string
# indicating how to adjust the room temperature based on these constraints:

# Return "heat" if the current temperature is below the target.
# Return "cool" if the current temperature is above the target.
# Return "hold" if the current temperature is equal to the target.
from pytest import mark


def adjust_thermostat(temp: float, target: float) -> str:
    return 'heat' if temp < target else 'cool' if temp > target else 'hold'


tests = [
    (68, 72, 'heat'),
    (75, 72, 'cool'),
    (72, 72, 'hold'),
    (-20.5, -10.1, 'heat'),
    (100, 99.9, 'cool'),
    (0.0, 0.0, 'hold'),
]


@mark.parametrize('temp, target, expected', tests)
def test_adjust_thermostat(temp: float, target: float, expected: str) -> None:
    assert adjust_thermostat(temp, target) == expected


if __name__ == '__main__':
    temp, target, expected = tests[0]
    print(adjust_thermostat(temp, target))
