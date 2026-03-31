# Daily Coding challenge #233 (2026-03-31) - freeCodeCamp.org
# Wake-Up Alarm
# Given a string representing the time you set your alarm and a string representing the
# time you actually woke up, determine if you woke up early, on time, or late.

# Both times will be given in "HH:MM" 24-hour format.
# Return:

# "early" if you woke up before your alarm time.
# "on time" if you woke up at your alarm time, or within the 10 minute snooze window
# after the alarm time.
# "late" if you woke up more than 10 minutes after your alarm time.
# Both times are on the same day.
from datetime import timedelta

from pytest import mark

SNOOZE_WINDOW = timedelta(minutes=10)


def to_timedelta(t: str) -> timedelta:
    hours, minutes = map(int, t.split(':'))
    return timedelta(hours=hours, minutes=minutes)


def alarm_check(alarm_time: str, wake_time: str) -> str:
    """Assumes both times are on the same day. Does not handle midnight crossings."""
    target = to_timedelta(alarm_time)
    actual = to_timedelta(wake_time)

    if actual < target:
        return 'early'

    if (actual - target) > SNOOZE_WINDOW:
        return 'late'

    return 'on time'


tests = [
    ('07:00', '06:45', 'early'),
    ('06:30', '06:30', 'on time'),
    ('08:10', '08:15', 'on time'),
    ('09:30', '09:45', 'late'),
    ('08:15', '08:25', 'on time'),
    ('05:45', '05:56', 'late'),
    ('04:30', '04:00', 'early'),
]


@mark.parametrize('alarm_time, wake_time, expected', tests)
def test_solution(alarm_time: str, wake_time: str, expected: str) -> None:
    assert alarm_check(alarm_time, wake_time) == expected


if __name__ == '__main__':
    alarm_time, wake_time, expected = tests[0]
    print(alarm_check(alarm_time, wake_time))
