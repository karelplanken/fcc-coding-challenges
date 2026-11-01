"""Daily Coding Challenge #59 (2025-10-08) - freeCodeCamp.org."""

# Space Week Day 5: Goldilocks Zone
# For the fifth day of Space Week, you will calculate the "Goldilocks zone" of a star -
# the region around a star where conditions are "just right" for liquid water to exist.
#
# Given the mass of a star, return an array with the start and end distances of its
# Goldilocks Zone in Astronomical Units.
#
# To calculate the Goldilocks Zone:
#
# 1. Find the luminosity of the star by raising its mass to the power of 3.5.
# 2. The start of the zone is 0.95 times the square root of its luminosity.
# 3. The end of the zone is 1.37 times the square root of its luminosity.
#
# - Return the distances rounded to two decimal places.
#
# For example, given 1 as a mass, return [0.95, 1.37].

# Design note (personal): this is deliberately a single pure function. The problem maps
# one number (a star's mass) to two numbers (the zone boundaries), so classes would add
# structure without a consumer. If stars gained more derived properties, were handled as
# collections, or the zone were passed on to other code, promote this to a frozen
# ``Star` dataclass. Validate the mass in ``__post_init__`` so an invalid star cannot
# be constructed, and expose ``luminosity`` and ``goldilocks_zone`` as properties (the
# latter returning a frozen ``GoldilocksZone(start, end)`` value object). Keep rounding
# at the boundary, in this function, so the domain object retains full precision.
import math

from pytest import mark

LUMINOSITY_EXPONENT = 3.5
ZONE_START_FACTOR = 0.95
ZONE_END_FACTOR = 1.37


def goldilocks_zone(mass: float) -> list[float]:
    """Calculate the Goldilocks zone of a star given its mass.

    The luminosity of the star is its mass raised to the power 3.5. The start and end
    of the zone are 0.95 and 1.37 times the square root of that luminosity.

    Args:
        mass: The mass of the star.

    Returns:
        The start and end distances of the Goldilocks zone in astronomical units (AU),
        rounded to two decimal places.

    Raises:
        ValueError: If mass is not a finite, positive number.
    """
    if not (math.isfinite(mass) and mass > 0):
        msg = f'mass must be a finite, positive number, got {mass!r}'
        raise ValueError(msg)
    luminosity = mass**LUMINOSITY_EXPONENT
    sqrt_luminosity = math.sqrt(luminosity)
    return [
        round(ZONE_START_FACTOR * sqrt_luminosity, 2),
        round(ZONE_END_FACTOR * sqrt_luminosity, 2),
    ]


tests: list[tuple[float, list[float]]] = [
    (1, [0.95, 1.37]),
    (0.5, [0.28, 0.41]),
    (6, [21.85, 31.51]),
    (3.7, [9.38, 13.52]),
    (20, [179.69, 259.13]),
]


@mark.parametrize('mass, expected', tests)
def test_goldilocks_zone(mass: float, expected: list[float]) -> None:
    """Test goldilocks_zone function."""
    assert goldilocks_zone(mass) == expected


if __name__ == '__main__':
    mass, expected = tests[0]
    print(goldilocks_zone(mass))
