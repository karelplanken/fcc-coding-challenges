"""Daily Coding Challenge #84 (2025-11-02) - freeCodeCamp.org."""

# Infected
# On November 2nd, 1988, the first major internet worm was released, infecting about 10%
# of computers connected to the internet after only a day.
#
# In this challenge, you are given a number of days that have passed since an internet
# worm was released, and you need to determine how many computers are infected using the
# following rules:
#
# - On day 0, the first computer is infected.
# - Each subsequent day, the number of infected computers doubles.
# - Every 3rd day, a patch is applied after the virus spreads and reduces the number of
#   infected computers by 20%. Round the number of patched computers up to the nearest
#   whole number.
#
# For example, on:
#
# - Day 0: 1 total computer is infected.
# - Day 1: 2 total computers are infected.
# - Day 2: 4 total computers are infected.
# - Day 3: 8 total computers are infected. Then, apply the patch: 8 infected * 20% = 1.6
#   patched. Round 1.6 up to 2. 8 computers infected - 2 patched = 6 total computers
#   infected after day 3.
#
# Return the number of total infected computers after the given amount of days have
# passed.
from pytest import mark

_SPREAD_FACTOR = 2
_PATCH_NUMERATOR, _PATCH_DENOMINATOR = 1, 5  # 20%, kept exact
_PATCH_INTERVAL = 3


def infected(days: int) -> int:
    """Return the number of infected computers after the given number of days.

    One computer is infected on day 0. Each day the count doubles; every third
    day, after spreading, 20% of infected computers (rounded up) are patched.
    All arithmetic is exact integer arithmetic, so results stay correct for
    arbitrarily large day counts.

    Args:
        days: Days elapsed since the worm was released.

    Returns:
        The number of infected computers at the end of that day.

    Raises:
        ValueError: If ``days`` is negative.
    """
    if days < 0:
        msg = f'days must be non-negative, got {days}'
        raise ValueError(msg)

    computers = 1
    for day in range(1, days + 1):
        computers *= _SPREAD_FACTOR
        if day % _PATCH_INTERVAL == 0:
            # Exact integer ceil(computers * 1/5) via negated floor division.
            patched = -(-computers * _PATCH_NUMERATOR // _PATCH_DENOMINATOR)
            computers -= patched
    return computers


tests = [
    (1, 2),
    (3, 6),
    (8, 152),
    (17, 39808),
    (25, 5217638),
]


@mark.parametrize(('days', 'expected'), tests)
def test_infected(days: int, expected: int) -> None:
    """Test infected function."""
    assert infected(days) == expected


if __name__ == '__main__':
    days, expected = tests[0]
    print(infected(days))
