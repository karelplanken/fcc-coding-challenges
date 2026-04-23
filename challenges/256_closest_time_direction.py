# Daily Coding challenge #256 (2026-04-23) - freeCodeCamp.org
# Closest Time Direction
# Given two times, determine whether you can get from the first to the second faster by
# moving forward or backward.

# Times are given in 24-hour format ("HH:MM")
# The clock wraps around (23:59 goes to 00:00 when moving forward, and 00:00 goes to
# 23:59 when moving backwards)

# Return:
# "forward" if moving forward is shorter
# "backward" if moving backward is shorter
# "equal" if both directions take the same amount of time
from pytest import mark

MINUTES_PER_HOUR = 60
DAY = 24 * MINUTES_PER_HOUR


def to_minutes(hrs_mins: str) -> int:
    hours, minutes = map(int, hrs_mins.split(':'))
    return hours * MINUTES_PER_HOUR + minutes


def get_direction(time1: str, time2: str) -> str:
    forward = (to_minutes(time2) - to_minutes(time1)) % DAY
    backward = DAY - forward

    if forward < backward:
        return 'forward'
    if backward < forward:
        return 'backward'
    return 'equal'


tests = [
    ('10:00', '12:00', 'forward'),
    ('11:00', '05:00', 'backward'),
    ('00:00', '12:00', 'equal'),
    ('15:45', '01:10', 'forward'),
    ('03:30', '19:50', 'backward'),
    ('06:30', '18:30', 'equal'),
]


@mark.parametrize(('time1', 'time2', 'expected'), tests)
def test_solution(time1: str, time2: str, expected: str) -> None:
    assert get_direction(time1, time2) == expected


if __name__ == '__main__':
    time1, time2, expected = tests[3]
    print(get_direction(time1, time2))
