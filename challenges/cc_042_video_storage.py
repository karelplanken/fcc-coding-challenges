"""Daily Coding Challenge #42 (2025-09-21) - freeCodeCamp.org."""

# Video Storage
# Given a video size, a unit for the video size, a hard drive capacity, and a unit for
# the hard drive, return the number of videos the hard drive can store using the
# following constraints:
#
# - The unit for the video size can be bytes ("B"), kilobytes ("KB"), megabytes ("MB"),
#   or gigabytes ("GB").
# - If not given one of the video units above, return "Invalid video unit".
# - The unit of the hard drive capacity can be gigabytes ("GB") or terabytes ("TB").
# - If not given one of the hard drive units above, return "Invalid drive unit".
# - Return the number of whole videos the drive can fit.
# - Use the following conversions:
#
# | Unit | Equivalent |
# |:----:|:----------:|
# | 1 B  |   1 B      |
# | 1 KB |   1000 B   |
# | 1 MB |   1000 KB  |
# | 1 GB |   1000 MB  |
# | 1 TB |   1000 GB  |
#
# For example, given 500, "MB", 100, and "GB" as arguments, determine how many 500 MB
# videos can fit on a 100 GB hard drive.
from fractions import Fraction
from types import MappingProxyType

from pytest import mark

_BYTES_PER_VIDEO_UNIT = MappingProxyType({
    'B': 1,
    'KB': 1_000,
    'MB': 1_000_000,
    'GB': 1_000_000_000,
})
_BYTES_PER_DRIVE_UNIT = MappingProxyType({'GB': 1_000_000_000, 'TB': 1_000_000_000_000})


def _exact(value: int | float) -> Fraction:
    """Return the decimal number the caller wrote as an exact Fraction.

    Args:
        value: The number to convert.

    Returns:
        The exact rational value of `value`, as written in decimal.
    """
    # str() first: Fraction(0.1) would capture the binary float, not 1/10.
    return Fraction(str(value))


def number_of_videos(
    video_size: int | float,
    video_unit: str,
    drive_size: int | float,
    drive_unit: str,
) -> int | str:
    """Return the number of whole videos that fit on a hard drive.

    Args:
        video_size: The size of each video.
        video_unit: The unit of the video size: "B", "KB", "MB" or "GB".
        drive_size: The size of the hard drive.
        drive_unit: The unit of the hard drive size: "GB" or "TB".

    Returns:
        The number of whole videos the drive can store (0 if none fit), or
        "Invalid video unit" / "Invalid drive unit" if a unit is not recognised.

    Raises:
        ValueError: If video_size is not positive or drive_size is negative.
    """
    if video_unit not in _BYTES_PER_VIDEO_UNIT:
        return 'Invalid video unit'
    if drive_unit not in _BYTES_PER_DRIVE_UNIT:
        return 'Invalid drive unit'
    if video_size <= 0:
        msg = 'video size must be a positive number'
        raise ValueError(msg)
    if drive_size < 0:
        msg = 'drive size must not be negative'
        raise ValueError(msg)

    drive_bytes = _exact(drive_size) * _BYTES_PER_DRIVE_UNIT[drive_unit]
    video_bytes = _exact(video_size) * _BYTES_PER_VIDEO_UNIT[video_unit]
    return drive_bytes // video_bytes


tests: list[tuple[int | float, str, int | float, str, int | str]] = [
    (500, 'MB', 100, 'GB', 200),
    (1, 'TB', 10, 'TB', 'Invalid video unit'),
    (2000, 'MB', 100000, 'MB', 'Invalid drive unit'),
    (500000, 'KB', 2, 'TB', 4000),
    (1.5, 'GB', 2.2, 'TB', 1466),
]


@mark.parametrize('video_size, video_unit, drive_size, drive_unit, expected', tests)
def test_number_of_videos(
    video_size: int | float,
    video_unit: str,
    drive_size: int | float,
    drive_unit: str,
    expected: int | str,
) -> None:
    """Test number_of_videos function."""
    assert number_of_videos(video_size, video_unit, drive_size, drive_unit) == expected


if __name__ == '__main__':
    video_size, video_unit, drive_size, drive_unit, expected = tests[0]
    print(number_of_videos(video_size, video_unit, drive_size, drive_unit))
