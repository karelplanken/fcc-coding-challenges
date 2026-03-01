# Daily Coding challenge #141 (2025-12-29) - freeCodeCamp.org
# Takeoff Fuel
# Given the numbers of gallons of fuel currently in your airplane, and the required
# number of liters of fuel to reach your destination, determine how many additional
# gallons of fuel you should add.

# 1 gallon equals 3.78541 liters.
# If the airplane already has enough fuel, return 0.
# You can only add whole gallons.
# Do not include decimals in the return number.
from math import ceil

from pytest import mark


def fuel_to_add(current_gallons: int, required_liters: int) -> int:
    LITERS_PER_GALLON = 3.78541
    GALLONS_PER_LITER = 1 / LITERS_PER_GALLON
    required_gallons = required_liters * GALLONS_PER_LITER
    gallons_needed = required_gallons - current_gallons

    if gallons_needed <= 0:
        return 0

    return ceil(gallons_needed)


tests = [
    (0, 1, 1),
    (5, 40, 6),
    (10, 30, 0),
    (896, 20500, 4520),
    (1000, 50000, 12209),
]


@mark.parametrize('current_gallons, required_liters, expected', tests)
def test_fuel_to_add(current_gallons: int, required_liters: int, expected: int) -> None:
    assert fuel_to_add(current_gallons, required_liters) == expected


if __name__ == '__main__':
    current_gallons, required_liters, expected = tests[2]
    print(fuel_to_add(current_gallons, required_liters))
