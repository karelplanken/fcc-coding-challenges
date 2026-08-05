# Daily Coding challenge #360 (2026-08-05) - freeCodeCamp.org
# Spoken Duration
# Given a number of seconds, return the duration in spoken English.
#
# - Break the duration into hours, minutes, and seconds.
# - Skip any zero values.
# - Use singular or plural as appropriate ("1 hour", "2 hours").
# - If present, join the last two units with "and", and the second and third to last
#   units with a comma ("1 hour, 2 minutes and 3 seconds").
from pytest import mark


class DurationError(Exception):
    """Raise this exception when the duration is invalid."""


def pluralize(value: int, unit: str) -> str:
    return f'{value} {unit}{"s" if value != 1 else ""}'


def join_naturally(words: list[str]) -> str:
    """Join a list of phrases the way spoken English would.

    ['a'] -> 'a'
    ['a', 'b'] -> 'a and b'
    ['a', 'b', 'c'] -> 'a, b and c'
    """
    if not words:
        raise ValueError('nothing to join')
    if len(words) == 1:
        return words[0]
    return f'{", ".join(words[:-1])} and {words[-1]}'


def get_spoken_duration(seconds: int) -> str:
    """Convert a number of seconds into a spoken English duration string.

    Args:
        seconds: A positive integer representing the number of seconds.

    Raises:
        DurationError: If seconds is not a positive integer.

    Returns:
        A string representation of the duration, e.g. '1 hour, 2 minutes and 3 seconds'.
    """
    if seconds <= 0:
        raise DurationError('seconds must be a positive integer')

    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    units = ((hours, 'hour'), (minutes, 'minute'), (secs, 'second'))

    return join_naturally([pluralize(v, u) for v, u in units if v])


tests = [
    (3723, '1 hour, 2 minutes and 3 seconds'),
    (7295, '2 hours, 1 minute and 35 seconds'),
    (8521, '2 hours, 22 minutes and 1 second'),
    (435, '7 minutes and 15 seconds'),
    (14455, '4 hours and 55 seconds'),
    (72000, '20 hours'),
    (1, '1 second'),
]


@mark.parametrize('seconds, expected', tests)
def test_get_spoken_duration(seconds: int, expected: str) -> None:
    assert get_spoken_duration(seconds) == expected


if __name__ == '__main__':
    seconds, expected = tests[0]
    print(get_spoken_duration(seconds))
