# Daily Coding challenge #59 (2025-10-08) - freeCodeCamp.org
# Space Week Day 5: Goldilocks Zone
# For the fifth day of Space Week, you will calculate the "Goldilocks zone" of a star -
# the region around a star where conditions are "just right" for liquid water to exist.

# Given the mass of a star, return an array with the start and end distances of its
# Goldilocks Zone in Astronomical Units.

# To calculate the Goldilocks Zone:

# Find the luminosity of the star by raising its mass to the power of 3.5.
# The start of the zone is 0.95 times the square root of its luminosity.
# The end of the zone is 1.37 times the square root of its luminosity.
# Return the distances rounded to two decimal places.
# For example, given 1 as a mass, return [0.95, 1.37].
from pytest import mark


def goldilocks_zone(mass: float) -> list[float]:
    sqrt_luminosity = mass ** (7 / 4)
    return [round(0.95 * sqrt_luminosity, 2), round(1.37 * sqrt_luminosity, 2)]


tests = [
    (1, [0.95, 1.37]),
    (0.5, [0.28, 0.41]),
    (6, [21.85, 31.51]),
    (3.7, [9.38, 13.52]),
    (20, [179.69, 259.13]),
]


@mark.parametrize('mass, expected', tests)
def test_goldilocks_zone(mass: float, expected: list[float]) -> None:
    assert goldilocks_zone(mass) == expected


if __name__ == '__main__':
    mass, expected = tests[2]
    print(goldilocks_zone(mass))
