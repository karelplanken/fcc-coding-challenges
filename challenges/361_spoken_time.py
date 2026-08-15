# Daily Coding challenge #361 (2026-08-06) - freeCodeCamp.org
# Spoken Time
# Given the angles for the hour and minute hands of an analog clock in degrees
# (clockwise from 12), return the time in spoken English.
#
# Convert the minute hand angle to minutes (360° = 60 minutes), then use the following
# rules:
#
# | Minutes              | Spoken                                     |
# |----------------------|--------------------------------------------|
# | 0                    | "Y o'clock"                                |
# | 15                   | "quarter past Y"                           |
# | 1–29 (excluding 15)  | "X minutes past Y"                         |
# | 30                   | "half past Y"                              |
# | 45                   | "quarter to Z"                             |
# | 31–59 (excluding 45) | "X minutes to Z" (where X is 60 - minutes) |
#
# Where Y is the current hour and Z is the next hour, both derived from the hour hand
# angle (360° = 12 hours).
#
# Note: Hand angles may not land exactly on a number, consider rounding them somehow.
from typing import Final

from pytest import mark

# Type annotations serve documentation purposes:
HOURS_ON_CLOCK: Final[int] = 12
MINUTES_PER_HOUR: Final[int] = 60
DEGREES_ON_CLOCK: Final[int] = 360
DEGREE_PER_HOUR: Final[int] = DEGREES_ON_CLOCK // HOURS_ON_CLOCK
DEGREE_PER_MINUTE: Final[int] = DEGREES_ON_CLOCK // MINUTES_PER_HOUR

# How close an angle must be to a tick boundary to be treated as "on" it.
# Guards against float representation noise (e.g. 89.99999999999997 instead
# of an intended 90) without prematurely snapping angles that are genuinely
# partway between ticks (e.g. 89.5, which should stay at minute 14, not 15).
_BOUNDARY_TOLERANCE: Final[float] = 1e-6


def _snap_to_boundary_if_close(
    angle: float, step: float, tolerance: float = _BOUNDARY_TOLERANCE
) -> float:
    """Snaps `angle` to the nearest multiple of `step` if it's within `tolerance` of
    one.

    Pure float-precision utility with no knowledge of clocks: it corrects
    representation noise near a grid boundary, and leaves everything else
    untouched.
    """
    nearest_multiple = round(angle / step) * step
    if abs(angle - nearest_multiple) <= tolerance:
        return nearest_multiple
    return angle


def get_hours(hour_angle: float) -> int:
    """Converts hours hand angle to hours.

    Floored, not rounded: like reading a real clock, the hour hasn't
    ticked over until the hand actually gets there.

    Args:
        hour_angle: Angle of hours hand.

    Returns:
        Hours (1-12) corresponding to the angle of the hours hand.
    """
    snapped_angle = _snap_to_boundary_if_close(hour_angle, DEGREE_PER_HOUR)
    hours = int(snapped_angle // DEGREE_PER_HOUR) % HOURS_ON_CLOCK
    return HOURS_ON_CLOCK if hours == 0 else hours


def get_minutes(minute_angle: float) -> int:
    """Converts minute hand angle to minutes.

    Floored, matching the hour hand: the spoken time reflects the last
    minute mark the hand has fully reached, not the nearest one.

    Args:
        minute_angle: Angle of minute hand.

    Returns:
        Minutes (0-59) corresponding to the angle of the minute hand.
    """
    snapped_angle = _snap_to_boundary_if_close(minute_angle, DEGREE_PER_MINUTE)
    minutes = int(snapped_angle // DEGREE_PER_MINUTE) % MINUTES_PER_HOUR
    return minutes


def get_time_string(hours: int, minutes: int) -> str:
    """Assembles the spoken time string.

    Args:
        hours: The hour component of the time (1-12).
        minutes: The minute component of the time (0-59).

    Returns:
        The time in spoken English.

    Raises:
        ValueError: If the time components are not valid.
    """
    next_hour = hours % HOURS_ON_CLOCK + 1  # 1-11 -> +1; 12 -> 0 -> 1

    if minutes == 0:
        return f"{hours} o'clock"

    if minutes == 15:
        return f'quarter past {hours}'

    if 0 < minutes < 30:
        return f'{minutes} minutes past {hours}'

    if minutes == 30:
        return f'half past {hours}'

    if minutes == 45:
        return f'quarter to {next_hour}'

    if minutes > 30:
        return f'{MINUTES_PER_HOUR - minutes} minutes to {next_hour}'

    raise ValueError(f'cannot create spoken time for {hours=} and {minutes=}')


def get_spoken_time(hour_angle: float, minute_angle: float) -> str:
    """Determines the time in spoken English given the angles of the hour and minute
    hands.

    When hour_angle is 0, it represents 12 o'clock. When minute_angle is 0, it
    represents the top of the hour.

    If angles exceed 360 degrees, they are wrapped around to fit within the 0-360 degree
    range (Python's floor division/modulo return a non-negative remainder for a
    positive divisor, so negative angles wrap correctly with no extra handling).

    Hour and minute are read independently from their respective hand angles,
    matching the problem's per-hand input model — there's no cross-hand
    consistency check, since the two angles aren't specified to derive from a
    single underlying time.

    Args:
        hour_angle: Hour hand angle in degrees (0-360).
        minute_angle: Minute hand angle in degrees (0-360).

    Returns:
        The time in spoken English.
    """
    hours, minutes = get_hours(hour_angle), get_minutes(minute_angle)
    return get_time_string(hours, minutes)


tests: list[tuple[float, float, str]] = [
    (90, 0, "3 o'clock"),
    (160, 120, '20 minutes past 5'),
    (255, 180, 'half past 8'),
    (67.5, 92, 'quarter past 2'),
    (200, 240, '20 minutes to 7'),
    (322.5, 273, 'quarter to 11'),
    (117.5, 335, '5 minutes to 4'),
]


@mark.parametrize('hour_angle, minute_angle, expected', tests)
def test_get_spoken_time(hour_angle: float, minute_angle: float, expected: str) -> None:
    assert get_spoken_time(hour_angle, minute_angle) == expected


if __name__ == '__main__':
    hour_angle, minute_angle, expected = tests[0]
    print(get_spoken_time(hour_angle, minute_angle))
