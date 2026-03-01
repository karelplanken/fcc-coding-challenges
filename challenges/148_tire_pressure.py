# Daily Coding challenge #148 (2026-01-05) - freeCodeCamp.org
# Tire Pressure
# Given an array with four numbers representing the tire pressures in psi of the four
# tires in your vehicle, and another array of two numbers representing the minimum and
# maximum pressure for your tires in bar, return an array of four strings describing
# each tire's status.

# 1 bar equal 14.5038 psi.
# Return an array with the following values for each tire:

# "Low" if the tire pressure is below the minimum allowed.
# "Good" if it's between the minimum and maximum allowed.
# "High" if it's above the maximum allowed.
from pytest import mark


def tire_status(pressures_psi: list[int], range_bar: list[float]) -> list[str]:
    PSI_PER_BAR = 14.5038
    min_bar, max_bar = range_bar
    return [
        'Low'
        if (bar := psi / PSI_PER_BAR) < min_bar
        else 'High'
        if bar > max_bar
        else 'Good'
        for psi in pressures_psi
    ]


tests = [
    ([32, 28, 35, 29], [2, 3], ['Good', 'Low', 'Good', 'Low']),
    ([32, 28, 35, 30], [2, 2.3], ['Good', 'Low', 'High', 'Good']),
    ([29, 26, 31, 28], [2.1, 2.5], ['Low', 'Low', 'Good', 'Low']),
    ([31, 31, 30, 29], [1.5, 2], ['High', 'High', 'High', 'Good']),
    ([30, 28, 30, 29], [1.9, 2.1], ['Good', 'Good', 'Good', 'Good']),
]


@mark.parametrize(('pressures_psi', 'range_bar', 'expected'), tests)
def test_tire_status(
    pressures_psi: list[int], range_bar: list[float], expected: list[str]
) -> None:
    assert tire_status(pressures_psi, range_bar) == expected


if __name__ == '__main__':
    pressures_psi, range_bar, expected = tests[0]
    print(tire_status(pressures_psi, range_bar))
