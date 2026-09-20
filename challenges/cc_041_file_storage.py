"""Daily Coding Challenge #41 (2025-09-20) - freeCodeCamp.org."""

# File Storage
# Given a file size, a unit for the file size, and hard drive capacity in gigabytes
# (GB), return the number of files the hard drive can store using the following
# constraints:
#
# - The unit for the file size can be bytes ("B"), kilobytes ("KB"), or megabytes
#   ("MB").
# - Return the number of whole files the drive can fit.
# - Use the following conversions:
#
# | Unit | Equivalent |
# |:----:|:----------:|
# | 1 B  |   1 B      |
# | 1 KB |   1000 B   |
# | 1 MB |   1000 KB  |
# | 1 GB |   1000 MB  |
#
# For example, given 500, "KB", and 1 as arguments, determine how many 500 KB files can
# fit on a 1 GB hard drive.
from fractions import Fraction
from types import MappingProxyType

from pytest import mark

_BYTES_PER_GB = 1_000_000_000
_BYTES_PER_UNIT = MappingProxyType({'B': 1, 'KB': 1_000, 'MB': 1_000_000})


def number_of_files(
    file_size: int | float, file_unit: str, drive_size_gb: int | float
) -> int:
    """Return the number of whole files that fit on a hard drive.

    Args:
        file_size: The size of each file.
        file_unit: The unit of the file size: "B", "KB" or "MB".
        drive_size_gb: The size of the hard drive in gigabytes.

    Returns:
        The number of whole files that fit on the hard drive.

    Raises:
        ValueError: If file size is not a positive number or if file_unit is not "B",
            "KB" or "MB".
    """
    if file_size <= 0:
        msg = 'file size must be a positive number'
        raise ValueError(msg)
    if file_unit not in _BYTES_PER_UNIT:
        msg = f'unsupported file unit: {file_unit!r}'
        raise ValueError(msg)
    # str() first: Fraction(0.1) would capture the binary float, not 1/10.
    drive_bytes = Fraction(str(drive_size_gb)) * _BYTES_PER_GB
    file_bytes = Fraction(str(file_size)) * _BYTES_PER_UNIT[file_unit]
    return drive_bytes // file_bytes


tests: list[tuple[int | float, str, int | float, int]] = [
    (500, 'KB', 1, 2000),
    (50000, 'B', 1, 20000),
    (5, 'MB', 1, 200),
    (4096, 'B', 1.5, 366210),
    (220.5, 'KB', 100, 453514),
    (4.5, 'MB', 750, 166666),
]


@mark.parametrize('file_size, file_unit, drive_size_gb, expected', tests)
def test_number_of_files(
    file_size: int | float, file_unit: str, drive_size_gb: int | float, expected: int
) -> None:
    """Test number_of_files function."""
    assert number_of_files(file_size, file_unit, drive_size_gb) == expected


if __name__ == '__main__':
    file_size, file_unit, drive_size_gb, expected = tests[0]
    print(number_of_files(file_size, file_unit, drive_size_gb))
