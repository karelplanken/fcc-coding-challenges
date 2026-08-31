"""Daily Coding Challenge #336 (2026-07-12) - freeCodeCamp.org."""

# Horoscope Match
# Given two star sign strings, return their compatibility percentage.
#
# The signs are arranged in a wheel of 12 positions in this order: "Aries",
# "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio",
# "Sagittarius", "Capricorn", "Aquarius", "Pisces", wrapping back to "Aries"
# after "Pisces". Find the shortest distance between the two signs and return the
# compatibility:
#
# | Distance | Compatibility |
# |----------|---------------|
# | 0 | "100%" |
# | 1 | "40%" |
# | 2 | "80%" |
# | 3 | "30%" |
# | 4 | "90%" |
# | 5 | "20%" |
# | 6 | "50%" |
from collections.abc import Mapping
from types import MappingProxyType
from typing import Final

from pytest import mark

# Ordered source of truth
STAR_SIGNS: Final[tuple[str, ...]] = (
    'Aries',
    'Taurus',
    'Gemini',
    'Cancer',
    'Leo',
    'Virgo',
    'Libra',
    'Scorpio',
    'Sagittarius',
    'Capricorn',
    'Aquarius',
    'Pisces',
)

SIGN_POSITION: Final[Mapping[str, int]] = MappingProxyType({
    sign: i for i, sign in enumerate(STAR_SIGNS)
})

NUM_SIGNS: Final[int] = len(STAR_SIGNS)

# Index == circular distance, so a tuple is a more honest fit than a dict here.
COMPATIBILITY: Final[tuple[str, ...]] = (
    '100%',
    '40%',
    '80%',
    '30%',
    '90%',
    '20%',
    '50%',
)


def horoscope_match(sign1: str, sign2: str) -> str:
    diff = abs(SIGN_POSITION[sign1] - SIGN_POSITION[sign2])
    distance = min(diff, NUM_SIGNS - diff)
    return COMPATIBILITY[distance]


tests = [
    ('Libra', 'Sagittarius', '80%'),
    ('Gemini', 'Scorpio', '20%'),
    ('Pisces', 'Aries', '40%'),
    ('Capricorn', 'Cancer', '50%'),
    ('Aquarius', 'Aquarius', '100%'),
    ('Virgo', 'Taurus', '90%'),
    ('Leo', 'Scorpio', '30%'),
]


@mark.parametrize('sign1, sign2, expected', tests)
def test_horoscope_match(sign1: str, sign2: str, expected: str) -> None:
    """Test horoscope_match function."""
    assert horoscope_match(sign1, sign2) == expected


if __name__ == '__main__':
    sign1, sign2, expected = tests[0]
    print(horoscope_match(sign1, sign2))
