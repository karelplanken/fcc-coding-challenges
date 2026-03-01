# Daily Coding challenge #41 (2025-09-20) - freeCodeCamp.org
# File Storage
# Given a file size, a unit for the file size, and hard drive capacity in
#  gigabytes (GB), return the number of files the hard drive can store using the
# following constraints:

# The unit for the file size can be bytes ("B"), kilobytes ("KB"), or megabytes ("MB").
# Return the number of whole files the drive can fit.
# Use the following conversions:
# Unit	Equivalent
# 1 B	1 B
# 1 KB	1000 B
# 1 MB	1000 KB
# 1 GB	1000 MB
# For example, given 500, "KB", and 1 as arguments, determine how many 500 KB files can
# fit on a 1 GB hard drive.
from pytest import mark

CONVERSION_FACTOR = {'B': 1, 'KB': 1000, 'MB': 1000_000, 'GB': 1000_000_000}


def number_of_files(file_size: int, file_unit: str, drive_size_gb: int) -> int:
    drive_size_b = drive_size_gb * CONVERSION_FACTOR['GB']
    file_size_b = file_size * CONVERSION_FACTOR[file_unit]
    return drive_size_b // file_size_b


tests = [
    (500, 'KB', 1, 2000),
    (50000, 'B', 1, 20000),
    (5, 'MB', 1, 200),
    (4096, 'B', 1.5, 366210),
    (220.5, 'KB', 100, 453514),
    (4.5, 'MB', 750, 166666),
]


@mark.parametrize('file_size, file_unit, drive_size_gb, expected', tests)
def test_number_of_files(
    file_size: int, file_unit: str, drive_size_gb: int, expected: str
) -> None:
    assert number_of_files(file_size, file_unit, drive_size_gb) == expected


if __name__ == '__main__':
    file_size, file_unit, drive_size_gb, expected = tests[0]
    print(number_of_files(file_size, file_unit, drive_size_gb))
