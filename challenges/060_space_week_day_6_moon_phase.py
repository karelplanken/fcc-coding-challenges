# Daily Coding challenge #60 (2025-10-09) - freeCodeCamp.org
# Space Week Day 6: Moon Phase
# For day six of Space Week, you will be given a date in the format "YYYY-MM-DD" and
# need to determine the phase of the moon for that day using the following rules:

# Use a simplified lunar cycle of 28 days, divided into four equal phases:

# "New": days 1 - 7
# "Waxing": days 8 - 14
# "Full": days 15 - 21
# "Waning": days 22 - 28
# After day 28, the cycle repeats with day 1, a new moon.

# Use "2000-01-06" as a reference new moon (day 1 of the cycle) to determine the phase
# of the given day.
# You will not be given any dates before the reference date.
# Return the correct phase as a string.
# Note: Day 1 represents the day of the new moon, meaning 0 days have passed since the
# last new moon.
from datetime import date

from pytest import mark


def moon_phase(date_string: str) -> str:
    REFERENCE_DATE = date.fromisoformat('2000-01-06')
    CYCLE_DAYS = 28

    days = (date.fromisoformat(date_string) - REFERENCE_DATE).days

    cycle_day = days % CYCLE_DAYS

    if cycle_day < 7:
        return 'New'
    if cycle_day < 14:
        return 'Waxing'
    if cycle_day < 21:
        return 'Full'

    return 'Waning'


tests = [
    ('2000-01-12', 'New'),
    ('2000-01-13', 'Waxing'),
    ('2014-10-15', 'Full'),
    ('2012-10-21', 'Waning'),
    ('2022-12-14', 'New'),
]


@mark.parametrize('date_string, expected', tests)
def test_moon_phase(date_string: str, expected: str) -> None:
    assert moon_phase(date_string) == expected


if __name__ == '__main__':
    date_string, expected = tests[1]
    print(moon_phase(date_string))
