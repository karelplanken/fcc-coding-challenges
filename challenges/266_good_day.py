# Daily Coding challenge #266 (2026-05-03) - freeCodeCamp.org
# Good Day
# Given a time string in "HH:MM" format (24-hour clock), return:

# "Good morning" for times 05:00 to 11:59
# "Good afternoon" for times 12:00 to 17:59
# "Good evening" for times 18:00 to 21:59
# "Good night" for times 22:00 to 04:59
from bisect import bisect
from types import MappingProxyType

from pytest import mark

HOURS_GREETING = MappingProxyType(
    {
        5: 'Good morning',  # 05:00–11:59
        12: 'Good afternoon',  # 12:00–17:59
        18: 'Good evening',  # 18:00–21:59
        22: 'Good night',  # 22:00–23:59
        24: 'Good night',  # 00:00–04:59
    }
)


HOURS_LIST = list(HOURS_GREETING.keys())


def get_greeting(s: str) -> str:
    hrs, _ = map(int, s.split(':'))
    idx = bisect(HOURS_LIST, hrs) - 1
    return HOURS_GREETING[HOURS_LIST[idx]]


tests = [
    ('24:00', 'Good night'),
    ('06:30', 'Good morning'),
    ('12:00', 'Good afternoon'),
    ('21:59', 'Good evening'),
    ('00:01', 'Good night'),
    ('11:30', 'Good morning'),
]


@mark.parametrize('s, expected', tests)
def test(s: str, expected: str) -> None:
    assert get_greeting(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(get_greeting(s))
