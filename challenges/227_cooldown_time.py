# Daily Coding challenge #227 (2026-03-25) - freeCodeCamp.org
# Cooldown Time
# Given two timestamps, the first representing when a user finished an exam, and the
# second representing the current time, determine whether the user can take an exam
# again.

# Both timestamps will be given the format: "YYYY-MM-DDTHH:MM:SS", for example
# "2026-03-25T14:00:00". Note that the time is 24-hour clock.
# A user must wait at least 48 hours before retaking an exam.
from datetime import datetime, timedelta

from pytest import mark

MINIMUM_WAIT_TIME = timedelta(hours=48)


def can_retake(finish_time: str, current_time: str) -> bool:
    finish_dt = datetime.fromisoformat(finish_time)
    current_dt = datetime.fromisoformat(current_time)
    wait_td = current_dt - finish_dt

    return wait_td >= MINIMUM_WAIT_TIME


tests = [
    ('2026-03-23T08:00:00', '2026-03-25T14:00:00', True),
    ('2026-03-24T14:00:00', '2026-03-25T10:00:00', False),
    ('2026-03-23T09:25:00', '2026-03-25T09:25:00', True),
    ('2026-03-25T11:50:00', '2026-03-23T11:49:59', False),
]


@mark.parametrize('finish_time, current_time, expected', tests)
def test_solution(finish_time: str, current_time: str, expected: bool) -> None:
    assert can_retake(finish_time, current_time) == expected


if __name__ == '__main__':
    finish_time, current_time, expected = tests[0]
    print(can_retake(finish_time, current_time))
