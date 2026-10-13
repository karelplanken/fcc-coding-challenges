"""Daily Coding Challenge #64 (2025-10-13) - freeCodeCamp.org."""

# 24 to 12
# Given a string representing a time of the day in the 24-hour format of "HHMM", return
# the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".
#
# - The given input will always be a four-digit string in 24-hour time format, from
#   "0000" to "2359".
from pytest import mark


def to_12(t: str) -> str:
    """Convert a 24-hour time string to 12-hour format.

    The input is assumed to be valid, as guaranteed by the problem: a
    four-digit ASCII string from "0000" to "2359". This is not checked;
    invalid input may return a malformed result (e.g. "2460" gives
    "12:60 PM") or raise ValueError from int().

    Args:
        t: A time of day in 24-hour "HHMM" format.

    Returns:
        The time in 12-hour "H:MM AM" or "H:MM PM" format.
    """
    hours, minutes = int(t[:2]), t[2:]
    suffix = 'AM' if hours < 12 else 'PM'
    return f'{hours % 12 or 12}:{minutes} {suffix}'


tests = [
    ('1124', '11:24 AM'),
    ('0900', '9:00 AM'),
    ('1455', '2:55 PM'),
    ('2346', '11:46 PM'),
    ('0030', '12:30 AM'),
]


@mark.parametrize('t, expected', tests)
def test_to_12(t: str, expected: str) -> None:
    """Test to_12 function."""
    assert to_12(t) == expected


if __name__ == '__main__':
    t, expected = tests[1]
    print(to_12(t))
