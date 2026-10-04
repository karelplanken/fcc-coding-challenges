"""Daily Coding Challenge #55 (2025-10-04) - freeCodeCamp.org."""

# Space Week Day 1: Stellar Classification
# October 4th marks the beginning of World Space Week. The next seven days will bring
# you astronomy-themed coding challenges.
#
# For today's challenge, you are given the surface temperature of a star in Kelvin (K)
# and need to determine its stellar classification based on the following ranges:
#
# - "O": 30,000 K or higher
# - "B": 10,000 K - 29,999 K
# - "A": 7,500 K - 9,999 K
# - "F": 6,000 K - 7,499 K
# - "G": 5,200 K - 5,999 K
# - "K": 3,700 K - 5,199 K
# - "M": 0 K - 3,699 K
#
# - Return the classification of the given star.
from bisect import bisect_right

from pytest import mark

# Lower bounds of each class above M; _CLASSES[i] covers [_BOUNDS[i-1], _BOUNDS[i]).
_BOUNDS = (3_700, 5_200, 6_000, 7_500, 10_000, 30_000)
_CLASSES = 'MKGFABO'


def classification(temp: int) -> str:
    """Return the stellar classification based on the given temperature.

    Args:
        temp: The surface temperature of the star in Kelvin.

    Returns:
        The stellar classification letter (O, B, A, F, G, K or M).

    Raises:
        ValueError: If temp is negative.
    """
    if temp < 0:
        msg = f'Temperature cannot be negative: {temp} K'
        raise ValueError(msg)
    return _CLASSES[bisect_right(_BOUNDS, temp)]


tests = [
    (5778, 'G'),
    (2400, 'M'),
    (9999, 'A'),
    (3700, 'K'),
    (3699, 'M'),
    (210000, 'O'),
    (6000, 'F'),
    (11432, 'B'),
]


@mark.parametrize('temp, expected', tests)
def test_classification(temp: int, expected: str) -> None:
    """Test classification function."""
    assert classification(temp) == expected


if __name__ == '__main__':
    temp, expected = tests[0]
    print(classification(temp))
