# Daily Coding challenge #271 (2026-05-08) - freeCodeCamp.org
# Medication Reminder
# Given an array of medications and a string representing the current time, return the
# next medication you need to take and how long until you need to take it.

# Each medication is in the format [name, lastTaken], where name is the name of the
# medication and lastTaken is the time it was last taken.
# All given times will be in "HH:MM" (24-hour) format.
# Use the following medication schedule:

# Name	Schedule
# Deployxitrin	08:00, 16:00
# Debuggamanizole	07:00, 13:00, 21:00
# Mergeflictamine	every 4 hours
# Return a string in the format "{name} in Hh Mm". For example,
# "Debuggamanizole in 2h 0m" or "Deployxitrin in 1h 5m".
from bisect import bisect_right

from pytest import mark

# Static schedule as (minutes_since_midnight, name) — pre-sorted
_STATIC_SCHEDULE: list[tuple[int, str]] = sorted([
    (8 * 60, 'Deployxitrin'),
    (16 * 60, 'Deployxitrin'),
    (7 * 60, 'Debuggamanizole'),
    (13 * 60, 'Debuggamanizole'),
    (21 * 60, 'Debuggamanizole'),
])

_DAY_MINUTES = 24 * 60
_MERGEFLICT_INTERVAL = 4 * 60


def _to_minutes(t: str) -> int:
    h, m = t.split(':')
    return int(h) * 60 + int(m)


def medication_reminder(medications: list[list[str]], current_time: str) -> str:
    now = _to_minutes(current_time)

    schedule = list(_STATIC_SCHEDULE)
    for name, last_taken in medications:
        if name == 'Mergeflictamine':
            next_dose = (_to_minutes(last_taken) + _MERGEFLICT_INTERVAL) % _DAY_MINUTES
            schedule.append((next_dose, name))

    schedule.sort()

    times = [t for t, _ in schedule]
    idx = bisect_right(times, now) % len(schedule)  # wraps midnight cleanly
    next_time, next_name = schedule[idx]

    wait = (next_time - now) % _DAY_MINUTES
    return f'{next_name} in {wait // 60}h {wait % 60}m'


tests = [
    (
        [
            ['Deployxitrin', '08:00'],
            ['Debuggamanizole', '07:00'],
            ['Mergeflictamine', '10:00'],
        ],
        '11:00',
        'Debuggamanizole in 2h 0m',
    ),
    (
        [
            ['Deployxitrin', '08:00'],
            ['Debuggamanizole', '13:00'],
            ['Mergeflictamine', '14:00'],
        ],
        '14:55',
        'Deployxitrin in 1h 5m',
    ),
    (
        [
            ['Deployxitrin', '08:00'],
            ['Debuggamanizole', '13:00'],
            ['Mergeflictamine', '14:00'],
        ],
        '17:15',
        'Mergeflictamine in 0h 45m',
    ),
    (
        [
            ['Deployxitrin', '08:00'],
            ['Debuggamanizole', '07:00'],
            ['Mergeflictamine', '09:00'],
        ],
        '12:59',
        'Debuggamanizole in 0h 1m',
    ),
    (
        [
            ['Deployxitrin', '08:00'],
            ['Debuggamanizole', '21:00'],
            ['Mergeflictamine', '03:00'],
        ],
        '06:55',
        'Debuggamanizole in 0h 5m',
    ),
    (
        [
            ['Deployxitrin', '08:00'],
            ['Debuggamanizole', '07:00'],
            ['Mergeflictamine', '07:30'],
        ],
        '08:00',
        'Mergeflictamine in 3h 30m',
    ),
]


@mark.parametrize('medications, current_time, expected', tests)
def test_medication_reminder(
    medications: list[list[str]], current_time: str, expected: str
) -> None:
    assert medication_reminder(medications, current_time) == expected


if __name__ == '__main__':
    medications, current_time, expected = tests[3]
    print(medication_reminder(medications, current_time))
