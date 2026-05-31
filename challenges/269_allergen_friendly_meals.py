# Daily Coding challenge #269 (2026-05-06) - freeCodeCamp.org
# Allergen Friendly Meals
# Given an array of meals and an array of allergens to avoid, return the names of all
# the meals that contain none of the given allergens.

# Each meal is in the format [meal, allergens], where meal is the name of the meal, and
# allergens is an array of the allergens the meal contains. For example,
# ["pasta", ["wheat", "milk"]].
# Allergens to avoid will be an array of strings.
# Return safe meal names in the same order given. If no meal is safe, return an empty
# array.
from typing import cast

from pytest import mark


def get_allergen_friendly_meals(
    meals: list[list[str | list[str]]], allergens: list[str]
) -> list[str]:

    allergen_set = set(allergens)  # O(1) lookups vs O(k) list scans

    safe_meals: list[str] = []
    for meal, meal_allergens in meals:
        if not allergen_set.intersection(cast(list[str], meal_allergens)):
            safe_meals.append(cast(str, meal))

    return safe_meals


tests: list[tuple[list[list[str | list[str]]], list[str], list[str]]] = [
    ([['pasta', ['wheat', 'milk']], ['salad', ['nuts']]], ['milk'], ['salad']),
    (
        [
            ['steak', ['soy']],
            ['fried rice', []],
            ['fish tacos', ['fish', 'wheat']],
            ['chicken parmesan', ['wheat', 'milk']],
        ],
        ['soy', 'fish'],
        ['fried rice', 'chicken parmesan'],
    ),
    (
        [
            ['oatmeal', ['nuts']],
            ['pancakes', ['wheat', 'milk']],
            ['granola', []],
            ['yogurt', ['milk']],
            ['eggs', ['eggs', 'milk']],
            ['toast', ['wheat']],
        ],
        ['eggs', 'milk'],
        ['oatmeal', 'granola', 'toast'],
    ),
    (
        [
            ['oatmeal', ['nuts']],
            ['pancakes', ['wheat', 'milk']],
            ['granola', []],
            ['yogurt', ['milk']],
            ['eggs', ['eggs', 'milk']],
            ['toast', ['wheat']],
        ],
        ['wheat', 'nuts'],
        ['granola', 'yogurt', 'eggs'],
    ),
]


@mark.parametrize('meals, allergens, expected', tests)
def test(
    meals: list[list[str | list[str]]], allergens: list[str], expected: list[str]
) -> None:
    assert get_allergen_friendly_meals(meals, allergens) == expected


if __name__ == '__main__':
    meals, allergens, expected = tests[0]
    print(get_allergen_friendly_meals(meals, allergens))
