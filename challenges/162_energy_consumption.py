# Daily Coding challenge #162 (2026-01-19) - freeCodeCamp.org
# Energy Consumption
# Given the number of Calories burned during a workout, and the number of watt-hours
# used by your electronic devices during that workout, determine which one used more
# energy.

# To compare them, convert both values to joules using the following conversions:

# 1 Calorie equals 4184 joules.
# 1 watt-hour equals 3600 joules.
# Return:

# "Workout" if the workout used more energy.
# "Devices" if the device used more energy.
# "Equal" if both used the same amount of energy.
from pytest import mark

J_PER_CAL = 4184
J_PER_WH = 3600

# Most straightforward and readable solution:
def compare_energy(calories_burned: int, watt_hours_used: int) -> str:
    workout_joules = calories_burned * J_PER_CAL
    devices_joules = watt_hours_used * J_PER_WH

    if workout_joules > devices_joules:
        return 'Workout'
    elif workout_joules < devices_joules:
        return 'Devices'
    else:
        return 'Equal'


# Clever and intended for a code-golfing challenge:
# def compare_energy(calories_burned: int, watt_hours_used: int) -> str:
#     diff = calories_burned * 4184 - watt_hours_used * 3600
#     return {-1: 'Devices', 0: 'Equal', 1: 'Workout'}[(diff > 0) - (diff < 0)]


tests = [
    (250, 50, 'Workout'),
    (100, 200, 'Devices'),
    (450, 523, 'Equal'),
    (300, 75, 'Workout'),
    (200, 250, 'Devices'),
    (900, 1046, 'Equal'),
]


@mark.parametrize('calories_burned, watt_hours_used, expected', tests)
def test_compare_energy(
    calories_burned: int, watt_hours_used: int, expected: str
) -> None:
    assert compare_energy(calories_burned, watt_hours_used) == expected


if __name__ == '__main__':
    calories_burned, watt_hours_used, expected = tests[2]
    print(compare_energy(calories_burned, watt_hours_used))
