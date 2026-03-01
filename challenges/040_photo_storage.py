# Daily Coding challenge #40 (2025-09-19) - freeCodeCamp.org
# Photo Storage
# Given a photo size in megabytes (MB), and hard drive capacity in gigabytes (GB),
# return the number of photos the hard drive can store using the following constraints:

# 1 gigabyte equals 1000 megabytes.
# Return the number of whole photos the drive can store.
from pytest import mark


def number_of_photos(photo_size_mb: int, drive_size_gb: int) -> int:
    return drive_size_gb * 1000 // photo_size_mb


tests = [
    (1, 1, 1000),
    (2, 1, 500),
    (4, 256, 64000),
    (3.5, 750, 214285),
    (3.5, 5.5, 1571),
]


@mark.parametrize('photo_size_mb, drive_size_gb, expected', tests)
def test_number_of_photos(
    photo_size_mb: int, drive_size_gb: int, expected: int
) -> None:
    assert number_of_photos(photo_size_mb, drive_size_gb) == expected


if __name__ == '__main__':
    photo_size_mb, drive_size_gb, expected = tests[0]
    print(number_of_photos(photo_size_mb, drive_size_gb), expected)
