# Daily Coding challenge #64 (2025-10-13) - freeCodeCamp.org
# 24 to 12
# Given a string representing a time of the day in the 24-hour format of "HHMM", return
# the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".

# The given input will always be a four-digit string in 24-hour time format,
# from "0000" to "2359".
import platform
from datetime import time

from pytest import mark

# Platform-specific format: Windows uses %#I, Unix/Linux/Mac use %-I
_HOUR_FORMAT = '%#I' if platform.system() == 'Windows' else '%-I'


def to_12(t: str) -> str:
    return time.strptime(t, '%H%M').strftime(f'{_HOUR_FORMAT}:%M %p')


tests = [
    ('1124', '11:24 AM'),
    ('0900', '9:00 AM'),
    ('1455', '2:55 PM'),
    ('2346', '11:46 PM'),
    ('0030', '12:30 AM'),
]


@mark.parametrize('t, expected', tests)
def test_to_12(t: str, expected: str) -> None:
    assert to_12(t) == expected


if __name__ == '__main__':
    t, expected = tests[2]
    print(to_12(t))
