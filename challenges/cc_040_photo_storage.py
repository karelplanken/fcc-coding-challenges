"""Daily Coding Challenge #40 (2025-09-19) - freeCodeCamp.org."""

# Photo Storage
# Given a photo size in megabytes (MB), and hard drive capacity in gigabytes (GB),
# return the number of photos the hard drive can store using the following constraints:
#
# - 1 gigabyte equals 1000 megabytes.
# - Return the number of whole photos the drive can store.
from fractions import Fraction

from pytest import mark

_MB_PER_GB = 1_000


def _exact(value: int | float) -> Fraction:
    """Return the decimal number the caller wrote as an exact Fraction.

    Args:
        value: The number to convert.

    Returns:
        The exact rational value of `value`, as written in decimal.
    """
    # str() first: Fraction(0.1) would capture the binary float, not 1/10.
    return Fraction(str(value))


def number_of_photos(photo_size_mb: int | float, drive_size_gb: int | float) -> int:
    """Return the number of whole photos that fit on a hard drive.

    Args:
        photo_size_mb: The size of each photo in megabytes.
        drive_size_gb: The capacity of the hard drive in gigabytes.

    Returns:
        The number of whole photos the drive can store (0 if none fit).

    Raises:
        ValueError: If photo_size_mb is not positive or drive_size_gb is
            negative.
    """
    if photo_size_mb <= 0:
        msg = 'photo size must be a positive number'
        raise ValueError(msg)
    if drive_size_gb < 0:
        msg = 'drive size must not be negative'
        raise ValueError(msg)

    drive_mb = _exact(drive_size_gb) * _MB_PER_GB
    photo_mb = _exact(photo_size_mb)
    return drive_mb // photo_mb


tests: list[tuple[int | float, int | float, int]] = [
    (1, 1, 1000),
    (2, 1, 500),
    (4, 256, 64000),
    (3.5, 750, 214285),
    (3.5, 5.5, 1571),
]


@mark.parametrize('photo_size_mb, drive_size_gb, expected', tests)
def test_number_of_photos(
    photo_size_mb: int | float, drive_size_gb: int | float, expected: int
) -> None:
    """Test number_of_photos function."""
    assert number_of_photos(photo_size_mb, drive_size_gb) == expected


if __name__ == '__main__':
    photo_size_mb, drive_size_gb, expected = tests[0]
    print(number_of_photos(photo_size_mb, drive_size_gb), expected)
