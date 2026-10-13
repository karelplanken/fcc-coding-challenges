"""Daily Coding Challenge #39 (2025-09-18) - freeCodeCamp.org."""

# Fill The Tank
# Given the size of a fuel tank, the current fuel level, and the price per gallon,
# return the cost to fill the tank all the way.
#
# - tankSize is the total capacity of the tank in gallons.
# - fuelLevel is the current amount of fuel in the tank in gallons.
# - pricePerGallon is the cost of one gallon of fuel.
# - The returned value should be rounded to two decimal places in the format: "$d.dd".
from decimal import ROUND_HALF_UP, Decimal

from pytest import mark, raises


def cost_to_fill(tank_size: float, fuel_level: float, price_per_gallon: float) -> str:
    """Calculate the cost to fill the tank.

    Args:
        tank_size: Maximum capacity of the tank in gallons.
        fuel_level: Current amount of fuel in the tank in gallons.
        price_per_gallon: Cost of one gallon of fuel.

    Returns:
        Cost to fill the tank in the format "$d.dd".

    Raises:
        ValueError: If any input is negative, or if fuel level exceeds tank size.
    """
    if tank_size < 0:
        msg = 'tank size must be non-negative'
        raise ValueError(msg)
    if fuel_level < 0:
        msg = 'fuel level must be non-negative'
        raise ValueError(msg)
    if price_per_gallon < 0:
        msg = 'price per gallon must be non-negative'
        raise ValueError(msg)
    if fuel_level > tank_size:
        msg = 'fuel level cannot exceed tank size'
        raise ValueError(msg)

    gallons_needed = Decimal(str(tank_size)) - Decimal(str(fuel_level))
    price = Decimal(str(price_per_gallon))
    cost = (gallons_needed * price).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return f'${cost}'


tests: list[tuple[float, float, float, str]] = [
    (20, 0, 4.00, '$80.00'),
    (15, 10, 3.50, '$17.50'),
    (18, 9, 3.25, '$29.25'),
    (12, 12, 4.99, '$0.00'),
    (15, 9.5, 3.98, '$21.89'),
]

invalid_tests: list[tuple[float, float, float, str]] = [
    (-1, 0, 4.00, 'tank size must be non-negative'),
    (20, -5, 4.00, 'fuel level must be non-negative'),
    (20, 10, -4.00, 'price per gallon must be non-negative'),
    (10, 15, 4.00, 'fuel level cannot exceed tank size'),
]


@mark.parametrize('tank_size, fuel_level, price_per_gallon, expected', tests)
def test_cost_to_fill(
    tank_size: float, fuel_level: float, price_per_gallon: float, expected: str
) -> None:
    """Test cost_to_fill function."""
    assert cost_to_fill(tank_size, fuel_level, price_per_gallon) == expected


@mark.parametrize(
    'tank_size, fuel_level, price_per_gallon, expected_msg', invalid_tests
)
def test_cost_to_fill_raises(
    tank_size: float, fuel_level: float, price_per_gallon: float, expected_msg: str
) -> None:
    """Test cost_to_fill raises ValueError for invalid input."""
    with raises(ValueError, match=expected_msg):
        cost_to_fill(tank_size, fuel_level, price_per_gallon)


if __name__ == '__main__':
    tank_size, fuel_level, price_per_gallon, expected = tests[0]
    print(cost_to_fill(tank_size, fuel_level, price_per_gallon))
