"""Daily Coding Challenge #77 (2025-10-26) - freeCodeCamp.org."""

# Duration Formatter
# Given an integer number of seconds, return a string representing the same duration in
# the format "H:MM:SS", where "H" is the number of hours, "MM" is the number of minutes,
# and "SS" is the number of seconds. Return the time using the following rules:
#
# - Seconds: Should always be two digits.
# - Minutes: Should omit leading zeros when they aren't needed. Use "0" if the duration
#   is less than one minute.
# - Hours: Should be included only if they're greater than zero.
from pytest import mark

_SECONDS_PER_MINUTE = 60
_MINUTES_PER_HOUR = 60


def format(seconds: int) -> str:
    """Convert seconds to a duration string.

    Args:
        seconds: Non-negative number of seconds.

    Returns:
        Duration in "M:SS" format, or "H:MM:SS" when it spans at least one hour.

    Raises:
        ValueError: If seconds is negative.
    """
    if seconds < 0:
        msg = f'seconds must be non-negative, got {seconds}'
        raise ValueError(msg)

    total_minutes, secs = divmod(seconds, _SECONDS_PER_MINUTE)
    hours, minutes = divmod(total_minutes, _MINUTES_PER_HOUR)

    if hours > 0:
        return f'{hours}:{minutes:02}:{secs:02}'
    return f'{minutes}:{secs:02}'


tests = [
    (500, '8:20'),
    (4000, '1:06:40'),
    (1, '0:01'),
    (5555, '1:32:35'),
    (99999, '27:46:39'),
]


@mark.parametrize('seconds, expected', tests)
def test_format(seconds: int, expected: str) -> None:
    """Test format function."""
    assert format(seconds) == expected


if __name__ == '__main__':
    seconds, expected = tests[1]
    print(format(seconds))
