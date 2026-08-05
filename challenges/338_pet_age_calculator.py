# Daily Coding challenge #338 (2026-07-14) - freeCodeCamp.org
# Pet Age Calculator
# Given a pet type and age in human years, return the equivalent age in pet years using
# the following conversion table:
#
# | Pet | Multiplier |
# |-----|-----------|
# | "dog" | 7 |
# | "cat" | 6 |
# | "rabbit" | 8 |
# | "hamster" | 30 |
# | "guinea pig" | 12 |
# | "goldfish" | 6 |
# | "bird" | 5 |
from types import MappingProxyType

from pytest import mark

PET_AGE_FACTOR = MappingProxyType({
    'dog': 7,
    'cat': 6,
    'rabbit': 8,
    'hamster': 30,
    'guinea pig': 12,
    'goldfish': 6,
    'bird': 5,
})


def pet_years(pet: str, age: int) -> int:
    factor = PET_AGE_FACTOR.get(pet)
    if factor is None:
        raise ValueError(f'pet {pet} does not exist.')
    return factor * age


tests = [
    ('dog', 5, 35),
    ('cat', 9, 54),
    ('rabbit', 3, 24),
    ('hamster', 4, 120),
    ('guinea pig', 5, 60),
    ('goldfish', 2, 12),
    ('bird', 1, 5),
]


@mark.parametrize('pet, age, expected', tests)
def test_pet_years(pet: str, age: int, expected: int) -> None:
    assert pet_years(pet, age) == expected


if __name__ == '__main__':
    pet, age, expected = tests[0]
    print(pet_years(pet, age))
