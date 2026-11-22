"""Daily Coding Challenge #104 (2025-11-22) - freeCodeCamp.org."""

# Recipe Scaler
# Given an array of recipe ingredients and a number to scale the recipe, return an array
# with the quantities scaled accordingly.
#
# - Each item in the given array will be a string in the format: "quantity unit
#   ingredient". For example "2 C Flour".
# - Scale the quantity by the given number. Do not include any trailing zeros and do not
#   convert any units.
# - Return the scaled items in the same order they are given.
from decimal import Decimal, InvalidOperation

import pytest


def _to_decimal(value: object, what: str) -> Decimal:
    try:
        result = Decimal(str(value))
    except InvalidOperation:
        msg = f'Invalid {what}: {value!r}'
        raise ValueError(msg)
    if not result.is_finite():
        msg = f'Invalid {what}: {value!r}'
        raise ValueError(msg)
    return result


def scale_recipe(ingredients: list[str], factor: float | Decimal) -> list[str]:
    """Scale the quantity of each ingredient by a factor.

    Args:
        ingredients: Lines of the form '<quantity> <unit> <name>', e.g. '1.5 T Sugar'.
        factor: Multiplier applied to every quantity.

    Returns:
        The ingredient lines with scaled quantities, without trailing zeros.

    Raises:
        ValueError: If the factor or a quantity is not a finite number, or a
            line has no text after the quantity.
    """
    scale = _to_decimal(factor, 'factor')
    scaled: list[str] = []
    for line in ingredients:
        parts = line.split(maxsplit=1)
        if len(parts) != 2:
            msg = f'Invalid ingredient line: {line!r}'
            raise ValueError(msg)
        amount, rest = parts
        quantity = _to_decimal(amount, 'quantity') * scale
        scaled.append(f'{format(quantity.normalize(), "f")} {rest}')
    return scaled


tests: list[tuple[list[str], float, list[str]]] = [
    (['2 C Flour', '1.5 T Sugar'], 2, ['4 C Flour', '3 T Sugar']),
    (['4 T Flour', '1 C Milk', '2 T Oil'], 1.5, ['6 T Flour', '1.5 C Milk', '3 T Oil']),
    (['3 C Milk', '2 C Oats'], 0.5, ['1.5 C Milk', '1 C Oats']),
    (
        [
            '2 C All-purpose Flour',
            '1 t Baking Soda',
            '1 t Salt',
            '1 C Butter',
            '0.5 C Sugar',
            '0.5 C Brown Sugar',
            '1 t Vanilla Extract',
            '2 C Chocolate Chips',
        ],
        2.5,
        [
            '5 C All-purpose Flour',
            '2.5 t Baking Soda',
            '2.5 t Salt',
            '2.5 C Butter',
            '1.25 C Sugar',
            '1.25 C Brown Sugar',
            '2.5 t Vanilla Extract',
            '5 C Chocolate Chips',
        ],
    ),
]


@pytest.mark.parametrize(('ingredients', 'scale', 'expected'), tests)
def test_scale_recipe(
    ingredients: list[str], scale: float, expected: list[str]
) -> None:
    """Test scale_recipe function."""
    assert scale_recipe(ingredients, scale) == expected


if __name__ == '__main__':
    ingredients, scale, expected = tests[0]
    print(scale_recipe(ingredients, scale))
