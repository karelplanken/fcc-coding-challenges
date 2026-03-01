# Daily Coding challenge #193 (2026-02-19) - freeCodeCamp.org
# 2026 Winter Games Day 14: Ski Mountaineering
# Given the snow depth and slope of a mountain, determine if there's an avalanche risk.

# The snow depth values are "Shallow", "Moderate", or "Deep".
# Slope values are "Gentle", "Steep", or "Very Steep".
# Return "Safe" or "Risky" based on this table:

#               "Shallow"	"Moderate"	"Deep"
# "Gentle"	    "Safe"	    "Safe"	    "Safe"
# "Steep"	    "Safe"	    "Risky"	    "Risky"
# "Very Steep"	"Safe"	    "Risky"	    "Risky"
from types import MappingProxyType

from pytest import mark

AVALAANCHE_RISK = MappingProxyType(
    {
        ('Shallow', 'Gentle'): 'Safe',
        ('Shallow', 'Steep'): 'Safe',
        ('Shallow', 'Very Steep'): 'Safe',
        ('Moderate', 'Gentle'): 'Safe',
        ('Moderate', 'Steep'): 'Risky',
        ('Moderate', 'Very Steep'): 'Risky',
        ('Deep', 'Gentle'): 'Safe',
        ('Deep', 'Steep'): 'Risky',
        ('Deep', 'Very Steep'): 'Risky',
    }
)


def avalanche_risk(snow_depth: str, slope: str) -> str:
    return AVALAANCHE_RISK[snow_depth, slope]


tests = [
    ('Shallow', 'Gentle', 'Safe'),
    ('Shallow', 'Steep', 'Safe'),
    ('Shallow', 'Very Steep', 'Safe'),
    ('Moderate', 'Gentle', 'Safe'),
    ('Moderate', 'Steep', 'Risky'),
    ('Moderate', 'Very Steep', 'Risky'),
    ('Deep', 'Gentle', 'Safe'),
    ('Deep', 'Steep', 'Risky'),
    ('Deep', 'Very Steep', 'Risky'),
]


@mark.parametrize('snow_depth, slope, expected', tests)
def test_avalanche_risk(snow_depth: str, slope: str, expected: str) -> None:
    assert avalanche_risk(snow_depth, slope) == expected


if __name__ == '__main__':
    snow_depth, slope, expected = tests[0]
    print(avalanche_risk(snow_depth, slope))
