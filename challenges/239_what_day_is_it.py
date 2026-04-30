# Daily Coding challenge #239 (2026-04-06) - freeCodeCamp.org
# What Day Is It?
# Given a Unix timestamp in milliseconds, return the day of the week.

# Valid return days are:

# "Sunday"
# "Monday"
# "Tuesday"
# "Wednesday"
# "Thursday"
# "Friday"
# "Saturday"
# Be sure to ignore time zones.
from pytest import mark

# January 1, 1970 (Unix epoch) was a Thursday. Dividing the timestamp by milliseconds
# per day and taking modulo 7 gives the index into a week days tuple.
WEEK_DAYS = (
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
)
MILLISECONDS_PER_DAY = 86_400_000


def get_day_of_week(timestamp: int) -> str:
    days_since_epoch = timestamp // MILLISECONDS_PER_DAY
    return WEEK_DAYS[days_since_epoch % len(WEEK_DAYS)]


tests = [
    (1775492249000, 'Monday'),
    (1766246400000, 'Saturday'),
    (33791256000000, 'Tuesday'),
    (1773576000000, 'Sunday'),
    (0, 'Thursday'),
]


@mark.parametrize('timestamp, expected', tests)
def test_get_day_of_week(timestamp: int, expected: str) -> None:
    assert get_day_of_week(timestamp) == expected


if __name__ == '__main__':
    timestamp, expected = tests[0]
    print(get_day_of_week(timestamp))
