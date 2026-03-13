# Daily Coding challenge #215 (2026-03-13) - freeCodeCamp.org
# Parking Fee Calculator
# Given two strings representing the time you parked your car and the time you picked
# it up, calculate the parking fee.

# The given strings will be in the format "HH:MM" using a 24-hour clock. So "14:00" is
# 2pm for example.
# The first string will be the time you parked your car, and the second will be the
# time you picked it up.
# If the pickup time is earlier than the entry time, it means the parking spanned past
# midnight into the next day.

# Fee rules:
# Each hour parked costs $3.
# Partial hours are rounded up to the next full hour.
# If the parking spans overnight (past midnight), an additional $10 overnight fee is
# applied.
# There is a minimum fee of $5 (only used if the total would be less than $5).
# Return the total cost in the format "$cost", "$5" for example.
from math import ceil

from pytest import mark

RATE_PER_HOUR = 3
OVERNIGHT_FEE = 10
MINIMUM_FEE = 5
MINUTES_IN_DAY = 24 * 60


def time_to_minutes(t: str) -> int:
    h, m = map(int, t.split(':'))
    return h * 60 + m


def calculate_parking_fee(park_time: str, pickup_time: str) -> str:
    start = time_to_minutes(park_time)
    end = time_to_minutes(pickup_time)

    overnight = end < start

    total_minutes = (MINUTES_IN_DAY - start + end) if overnight else (end - start)

    cost = ceil(total_minutes / 60) * RATE_PER_HOUR + (overnight * OVERNIGHT_FEE)

    return f'${max(cost, MINIMUM_FEE)}'


tests = [
    ('09:00', '11:00', '$6'),
    ('10:00', '10:30', '$5'),
    ('08:10', '10:45', '$9'),
    ('14:40', '23:10', '$27'),
    ('18:15', '01:30', '$34'),
    ('11:11', '11:10', '$82'),
]


@mark.parametrize('park_time, pickup_time, expected', tests)
def test_calculate_parking_fee(park_time: str, pickup_time: str, expected: str) -> None:
    assert calculate_parking_fee(park_time, pickup_time) == expected


if __name__ == '__main__':
    park_time, pickup_time, expected = tests[0]
    print(calculate_parking_fee(park_time, pickup_time))
