# Daily Coding challenge #155 (2026-01-12) - freeCodeCamp.org
# Plant the Crop
# Given an integer representing the size of your farm field, and "acres" or "hectares"
# representing the unit for the size of your farm field, and a type of crop, determine
# how many plants of that type you can fit in your field.

# 1 acre equals 4046.86 square meters.
# 1 hectare equals 10,000 square meters.
# Here's a list of crops that will be given as input and how much space a single plant
# takes:
# Crop	Space per plant
# "corn"	1 square meter
# "wheat"	0.1 square meters
# "soybeans"	0.5 square meters
# "tomatoes"	0.25 square meters
# "lettuce"	0.2 square meters
# Return the number of plants that fit in the field, rounded down to the nearest whole
# plant.
from types import MappingProxyType

from pytest import mark

TO_SQR_METER = MappingProxyType(
    {
        'acres': 4_046.86,
        'hectares': 10_000.00,
    }
)

CROP_SURFACE = MappingProxyType(
    {
        'corn': 1.0,
        'wheat': 0.1,
        'soybeans': 0.5,
        'tomatoes': 0.25,
        'lettuce': 0.2,
    }
)


def get_number_of_plants(field_size: int | float, unit: str, crop: str) -> int:
    return int(field_size * TO_SQR_METER[unit] / CROP_SURFACE[crop])


tests = [
    (1, 'acres', 'corn', 4046),
    (2, 'hectares', 'lettuce', 100000),
    (20, 'acres', 'soybeans', 161874),
    (3.75, 'hectares', 'tomatoes', 150000),
    (16.75, 'acres', 'tomatoes', 271139),
]


@mark.parametrize('field_size, unit, crop, expected', tests)
def test_get_number_of_plants(
    field_size: int, unit: str, crop: str, expected: int
) -> None:
    assert get_number_of_plants(field_size, unit, crop) == expected


if __name__ == '__main__':
    field_size, unit, crop, expected = tests[0]
    print(get_number_of_plants(field_size, unit, crop))
