# Daily Coding challenge #127 (2025-12-15) - freeCodeCamp.org
# Speed Check
# Given the speed you are traveling in miles per hour (MPH), and a speed limit in
# kilometers per hour (KPH), determine whether you are speeding and if you will get
# a warning or a ticket.

# 1 mile equals 1.60934 kilometers.
# If you are travelling less than or equal to the speed limit, return "Not Speeding".
# If you are travelling 5 KPH or less over the speed limit, return "Warning".
# If you are travelling more than 5 KPH over the speed limit, return "Ticket".
from pytest import mark

# Constant for clarity
MILES_TO_KM = 1.60934
TOLERANCE_KPH = 5


def speed_check(speed_mph: int, speed_limit_kph: int) -> str:
    speed_kph = speed_mph * MILES_TO_KM
    excess_speed = speed_kph - speed_limit_kph

    if excess_speed <= 0:
        return 'Not Speeding'
    if excess_speed <= TOLERANCE_KPH:
        return 'Warning'
    return 'Ticket'


tests = [
    (30, 70, 'Not Speeding'),
    (40, 60, 'Warning'),
    (40, 65, 'Not Speeding'),
    (60, 90, 'Ticket'),
    (65, 100, 'Warning'),
    (88, 40, 'Ticket'),
]


@mark.parametrize('speed_mph, speed_limit_kph, expected', tests)
def test_speed_check(speed_mph: int, speed_limit_kph: int, expected: str) -> None:
    assert speed_check(speed_mph, speed_limit_kph) == expected


if __name__ == '__main__':
    speed_mph, speed_limit_kph, expected = tests[0]
    print(speed_check(speed_mph, speed_limit_kph))
