# Daily Coding challenge #222 (2026-03-20) - freeCodeCamp.org
# Equinox Shadows
# Today is the equinox, when the sun is directly above the equator and perfectly
# overhead at noon. Given a time, determine the shadow cast by a 4-foot vertical pole.

# The time will be a string in "HH:MM" 24-hour format (for example, "15:00" is 3pm).
# You will only be given a time in 30 minute increments.
# Rules:

# The sun rises at 6am directly "east", and sets at 6pm directly "west".
# A shadow always points opposite the sun.
# The shadow's length (in feet) is the number of hours away from noon, cubed.
# There is no shadow before sunrise (before 6am), after sunset (6pm or later),
# or at noon.
# Return:
# If a shadow exists, return "(length)ft (direction)". For example, "8ft west".
# Otherwise, return "No shadow".
# For example, given "10:00", return "8ft west" because 10am is 2 hours from noon, so
# 2^3 = 8 feet, and the shadow points west because the sun is in the east at 10am.
from pytest import mark

SUNRISE = 6
SUNSET = 18
NOON = 12


def get_shadow(time: str) -> str:
    h, m = map(int, time.split(':'))
    hours = h + 0.5 if m else h

    if not (SUNRISE <= hours < SUNSET) or hours == NOON:
        return 'No shadow'

    return f'{abs(NOON - hours) ** 3:g}ft {"west" if hours < NOON else "east"}'


tests = [
    ('10:00', '8ft west'),
    ('15:00', '27ft east'),
    ('12:00', 'No shadow'),
    ('17:30', '166.375ft east'),
    ('05:00', 'No shadow'),
    ('06:00', '216ft west'),
    ('18:00', 'No shadow'),
    ('07:30', '91.125ft west'),
    ('00:00', 'No shadow'),
]


@mark.parametrize('time, expected', tests)
def test_solution(time: str, expected: str) -> None:
    assert get_shadow(time) == expected


if __name__ == '__main__':
    time, expected = tests[0]
    print(get_shadow(time))
