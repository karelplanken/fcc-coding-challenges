"""Daily Coding Challenge #61 (2025-10-10) - freeCodeCamp.org."""

# Space Week Day 7: Launch Fuel
# For the final day of Space Week, you will be given the mass in kilograms (kg) of a
# payload you want to send to orbit. Determine the amount of fuel needed to send your
# payload to orbit using the following rules:
#
# - Rockets require 1 kg of fuel per 5 kg of mass they must lift.
# - Fuel itself has mass. So when you add fuel, the mass to lift goes up, which requires
#   more fuel, which increases the mass, and so on.
# - To calculate the total fuel needed: start with the payload mass, calculate the fuel
#   needed for that, add that fuel to the total mass, and calculate again. Repeat this
#   process until the additional fuel required is less than 1 kg, then stop.
# - Ignore the mass of the rocket itself. Only compute fuel needed to lift the payload
#   and its own fuel.
#
# For example, given a payload mass of 50 kg, you would need 10 kg of fuel to lift it
# (payload / 5), which increases the total mass to 60 kg, which needs 12 kg to lift (2
# additional kg), which increases the total mass to 62 kg, which needs 12.4 kg to lift -
# 0.4 additional kg - which is less 1 additional kg, so we stop here. The total mass to
# lift is 62.4 kg, 50 of which is the initial payload and 12.4 of fuel.
#
# - Return the amount of fuel needed rounded to one decimal place.
import math

from pytest import mark


def launch_fuel(payload: float) -> float:
    """Calculate the amount of fuel needed to launch a payload to orbit.

    Rockets need 1 kg of fuel per 5 kg lifted, and fuel must lift itself, so
    each round of extra fuel is 1/5 of the previous round. The total is the
    geometric series

        fuel = p/5 + p/25 + ... + p/5**k = (p / 4) * (1 - 5**-k)

    where p is the payload and k is the number of rounds. Per the spec, the
    base fuel (p/5) is always followed by at least one additional round, and
    the process stops after the first additional round below 1 kg, which is
    still included. So k is the smallest k >= 2 with 5**k > p. For example,
    p = 50 gives k = 3: 10 + 2 + 0.4 = 12.4.

    Implementing the closed form looks like this:
    ...  # same validation
    steps, threshold = 2, 25
    while threshold <= payload:  # find smallest k >= 2 with 5**k > payload
        steps += 1
        threshold *= 5
    return round(payload / 4 * (1 - 5.0**-steps), 1)


    The loop below follows the spec's
    step-by-step procedure; the closed form above is the same sum.

    Args:
        payload: The mass of the payload in kilograms (kg).

    Returns:
        The total amount of fuel needed in kilograms (kg), rounded to one
        decimal place.

    Raises:
        ValueError: If the payload is not a finite, non-negative number.
    """
    if not math.isfinite(payload) or payload < 0:
        msg = f'payload must be a finite, non-negative number, got {payload!r}'
        raise ValueError(msg)

    increment = payload / 5
    total = increment
    while True:
        increment /= 5
        total += increment
        if increment < 1:  # the sub-1 kg round is still included
            return round(total, 1)


tests = [
    (50, 12.4),
    (500, 124.8),
    (243, 60.7),
    (11000, 2749.8),
    (6214, 1553.4),
]


@mark.parametrize('payload, expected', tests)
def test_launch_fuel(payload: float, expected: float) -> None:
    """Test launch_fuel function."""
    assert launch_fuel(payload) == expected


if __name__ == '__main__':
    # payload, expected = tests[0]
    # print(launch_fuel(payload))
    print(launch_fuel(3))
