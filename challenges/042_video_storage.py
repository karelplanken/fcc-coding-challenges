# Daily Coding challenge #42 (2025-09-21) - freeCodeCamp.org
# Video Storage
# Given a video size, a unit for the video size, a hard drive capacity, and a unit for
# the hard drive, return the number of videos the hard drive can store using the
# following constraints:

# The unit for the video size can be bytes ("B"), kilobytes ("KB"), megabytes ("MB"),
# or gigabytes ("GB").
# If not given one of the video units above, return "Invalid video unit".
# The unit of the hard drive capacity can be gigabytes ("GB") or terabytes ("TB").
# If not given one of the hard drive units above, return "Invalid drive unit".
# Return the number of whole videos the drive can fit.
# Use the following conversions:
# Unit	Equivalent
# 1 B	1 B
# 1 KB	1000 B
# 1 MB	1000 KB
# 1 GB	1000 MB
# 1 TB	1000 GB
# For example, given 500, "MB", 100, and "GB" as arguments, determine how many 500 MB
# videos can fit on a 100 GB hard drive.
from pytest import mark

# Define base conversions - easier to maintain and verify
BYTE_CONVERSIONS = {
    'B': 1,
    'KB': 1_000,
    'MB': 1_000_000,
    'GB': 1_000_000_000,
    'TB': 1_000_000_000_000,
}

VALID_VIDEO_UNITS = {'B', 'KB', 'MB', 'GB'}
VALID_DRIVE_UNITS = {'GB', 'TB'}


def number_of_videos(
    video_size: int | float,
    video_unit: str,
    drive_size: int | float,
    drive_unit: str,
) -> int | str:
    # Validate units
    if video_unit not in VALID_VIDEO_UNITS:
        return 'Invalid video unit'
    if drive_unit not in VALID_DRIVE_UNITS:
        return 'Invalid drive unit'

    # Convert to bytes and calculate
    video_size_bytes = video_size * BYTE_CONVERSIONS[video_unit]
    drive_size_bytes = drive_size * BYTE_CONVERSIONS[drive_unit]

    return int(drive_size_bytes // video_size_bytes)


tests = [
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
    assert number_of_videos(video_size, video_unit, drive_size, drive_unit) == expected


if __name__ == '__main__':
    video_size, video_unit, drive_size, drive_unit, expected = tests[0]
    print(number_of_videos(video_size, video_unit, drive_size, drive_unit))
