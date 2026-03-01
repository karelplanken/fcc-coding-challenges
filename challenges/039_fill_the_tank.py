# Daily Coding challenge #39 (2025-09-18) - freeCodeCamp.org
# Fill The Tank
# Given the size of a fuel tank, the current fuel level, and the price per gallon,
# return the cost to fill the tank all the way.

# tankSize is the total capacity of the tank in gallons.
# fuelLevel is the current amount of fuel in the tank in gallons.
# pricePerGallon is the cost of one gallon of fuel.
# The returned value should be rounded to two decimal places in the format: "$d.dd".
from pytest import mark


def cost_to_fill(tank_size: float, fuel_level: float, price_per_gallon: float) -> str:
    return f'${(tank_size - fuel_level) * price_per_gallon:.2f}'


tests = [
    (20, 0, 4.00, '$80.00'),
    (15, 10, 3.50, '$17.50'),
    (18, 9, 3.25, '$29.25'),
    (12, 12, 4.99, '$0.00'),
    (15, 9.5, 3.98, '$21.89'),
]


@mark.parametrize('tank_size, fuel_level, price_per_gallon, expected', tests)
def test_cost_to_fill(
    tank_size: float, fuel_level: float, price_per_gallon: float, expected: str
) -> None:
    assert cost_to_fill(tank_size, fuel_level, price_per_gallon) == expected


if __name__ == '__main__':
    tank_size, fuel_level, price_per_gallon, expected = tests[1]
    print(cost_to_fill(tank_size, fuel_level, price_per_gallon))
