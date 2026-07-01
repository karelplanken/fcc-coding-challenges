# Daily Coding challenge #313 (2026-06-19) - freeCodeCamp.org
# Rental Cost
# Given a rental timestamp, a return timestamp, and a rental tier, return the total
# cost of the rental including any late fees.

# Given timestamps are UTC ISO strings, for example: "2026-06-18T18:30:00Z".
# The rental tier is the number of days before the rental is due back: 1, 3, or 7.
# Rentals are due back by 12:00 PM UTC or earlier on the last day of the rental period.
# For example, a 1-day rental checked out at any time on March 15 is due back by
# 12:00 PM UTC on March 16.
# Each day past the due date and time incurs a late fee.
# Pricing is as follows:

# Tier	Base cost	Late fee per day
# 1 day	$4.99	$3.99
# 3 days	$3.99	$2.99
# 7 days	$2.99	$0.99
# Return the total cost rounded to two decimal places in the format "$D.CC".
from collections import namedtuple
from datetime import UTC, datetime, time, timedelta

from pytest import mark

RENTAL_DUE_TIME = time(hour=12, minute=0, second=0, microsecond=0, tzinfo=UTC)

RentalPrice = namedtuple('RentalPrice', ['tier', 'base_cost', 'late_fee_per_day'])

rental_prices = [
    RentalPrice(tier=1, base_cost=4.99, late_fee_per_day=3.99),
    RentalPrice(tier=3, base_cost=3.99, late_fee_per_day=2.99),
    RentalPrice(tier=7, base_cost=2.99, late_fee_per_day=0.99),
]

rental_price_by_tier = {
    rental_price.tier: rental_price for rental_price in rental_prices
}


def get_due_date(rented: datetime, tier: int) -> datetime:
    return (rented + timedelta(days=tier)).replace(
        hour=RENTAL_DUE_TIME.hour,
        minute=RENTAL_DUE_TIME.minute,
        second=RENTAL_DUE_TIME.second,
        microsecond=RENTAL_DUE_TIME.microsecond,
    )


def get_days_late(due: datetime, returned: datetime) -> int:
    if returned <= due:
        return 0
    whole_days_late, remainder = divmod(returned - due, timedelta(days=1))
    return whole_days_late + 1 if remainder else whole_days_late


def get_rental_cost(rented: str, returned: str, tier: int) -> str:
    dt_rented = datetime.fromisoformat(rented)
    dt_returned = datetime.fromisoformat(returned)

    dt_due = get_due_date(dt_rented, tier)
    rental_price = rental_price_by_tier[tier]

    days_late = get_days_late(dt_due, dt_returned)
    total_rent = rental_price.base_cost + rental_price.late_fee_per_day * days_late

    return f'${total_rent:.2f}'


tests = [
    ('2026-06-18T18:30:00Z', '2026-06-19T10:30:00Z', 1, '$4.99'),
    ('2026-06-18T14:30:00Z', '2026-06-20T12:30:00Z', 1, '$12.97'),
    ('2026-06-18T10:15:00Z', '2026-06-18T19:45:00Z', 3, '$3.99'),
    ('2026-06-18T15:20:00Z', '2026-06-23T08:10:00Z', 3, '$9.97'),
    ('2026-06-18T12:00:00Z', '2026-06-25T12:00:00Z', 7, '$2.99'),
    ('2026-06-18T08:00:00Z', '2027-06-18T14:00:00Z', 7, '$358.40'),
]


@mark.parametrize('rented, returned, tier, expected', tests)
def test_solution(rented: str, returned: str, tier: int, expected: str) -> None:
    assert get_rental_cost(rented, returned, tier) == expected


if __name__ == '__main__':
    rented, returned, tier, expected = tests[5]
    print(get_rental_cost(rented, returned, tier))
