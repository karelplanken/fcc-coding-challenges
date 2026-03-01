# Daily Coding challenge #77 (2025-10-26) - freeCodeCamp.org
# Duration Formatter
# Given an integer number of seconds, return a string representing the same duration in
# the format "H:MM:SS", where "H" is the number of hours, "MM" is the number of
# minutes, and "SS" is the number of seconds. Return the time using the following rules:

# Seconds: Should always be two digits.
# Minutes: Should omit leading zeros when they aren't needed. Use "0" if the duration
# is less than one minute.
# Hours: Should be included only if they're greater than zero.
from pytest import mark


def format(seconds: int) -> str:
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    if hours > 0:
        return f'{hours}:{minutes:02}:{seconds:02}'

    return f'{minutes}:{seconds:02}'


tests = [
    (500, '8:20'),
    (4000, '1:06:40'),
    (1, '0:01'),
    (5555, '1:32:35'),
    (99999, '27:46:39'),
]


@mark.parametrize('seconds, expected', tests)
def test_format(seconds: int, expected: str) -> None:
    assert format(seconds) == expected


if __name__ == '__main__':
    seconds, expected = tests[2]
    print(format(seconds))
