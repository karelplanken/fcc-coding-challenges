"""Daily Coding Challenge #11 (2025-08-21) - freeCodeCamp.org."""

# Mile Pace
# Given a number of miles ran, and a time in "MM:SS" (minutes:seconds) it took to run
# those miles, return a string for the average time it took to run each mile in the
# format "MM:SS".
#
# - Add leading zeros when needed.
from pytest import mark

SECONDS_PER_MINUTE = 60


def _parse_mmss(duration: str) -> int:
    """Convert an "MM:SS" string to total seconds.

    Args:
        duration: Time in "MM:SS" format.

    Returns:
        Total number of seconds.
    """
    minutes, seconds = map(int, duration.split(':'))
    return minutes * SECONDS_PER_MINUTE + seconds


def _format_mmss(total_seconds: int) -> str:
    """Convert total seconds to an "MM:SS" string with leading zeros.

    Args:
        total_seconds: Total number of seconds.

    Returns:
        Time in "MM:SS" format.
    """
    minutes, seconds = divmod(total_seconds, SECONDS_PER_MINUTE)
    return f'{minutes:02}:{seconds:02}'


def mile_pace(miles: float, duration: str) -> str:
    """Return average time per mile in "MM:SS" format.

    Notice that banker's rounding is used to round the average time per mile.

    Args:
        miles: Number of miles run.
        duration: Time taken to run the miles in "MM:SS" format.

    Returns:
        Average time per mile in "MM:SS" format.

    Raises:
        ValueError: If miles is not greater than zero.
    """
    if not miles > 0:
        msg = 'miles must be greater than zero'
        raise ValueError(msg)

    avg_seconds_per_mile = round(_parse_mmss(duration) / miles)
    return _format_mmss(avg_seconds_per_mile)


tests: list[tuple[float, str, str]] = [
    (3, '24:00', '08:00'),
    (1, '06:45', '06:45'),
    (2, '07:00', '03:30'),
    (26.2, '120:35', '04:36'),
]


@mark.parametrize('miles, duration, expected', tests)
def test_mile_pace(miles: float, duration: str, expected: str) -> None:
    """Test mile_pace function."""
    assert mile_pace(miles, duration) == expected


if __name__ == '__main__':
    miles, duration, expected = tests[0]
    print(mile_pace(miles, duration))
