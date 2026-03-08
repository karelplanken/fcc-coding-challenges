# Daily Coding challenge #210 (2026-03-08) - freeCodeCamp.org
# HSL Validator
# Given a string, determine whether it is a valid CSS hsl() color value.

# A valid HSL value must be in the format "hsl(h, s%, l%)", where:

# h (hue) must be a number between 0 and 360 (inclusive).
# s (saturation) must be a percentage between 0% and 100%.
# l (lightness) must be a percentage between 0% and 100%.
# Spaces are only allowed:

# After the opening parenthesis
# Before and/or after the commas
# Before and/or after closing parenthesis
# Optionally, the value can end with a semi-colon (";").

# For example, "hsl(240, 50%, 50%)" is a valid HSL value.
import re

from pytest import mark

pattern = re.compile(
    r'hsl\(\s*(?P<hue>\d{1,3})\s*,\s*(?P<saturation>\d{1,3})%\s*,\s*(?P<lightness>\d{1,3})%\s*\)\s*;?\s*'
)


def is_valid_hsl(hsl: str) -> bool:
    match = pattern.fullmatch(hsl)
    if not match:
        return False
    return (
        (0 <= int(match['hue']) <= 360)
        and (0 <= int(match['saturation']) <= 100)
        and (0 <= int(match['lightness']) <= 100)
    )


tests = [
    ('hsl(240, 50%, 50%)', True),
    ('hsl( 200 , 50% , 75% )', True),
    ('hsl(99,60%,80%);', True),
    ('hsl(0, 0%, 0%) ;', True),
    ('hsl(  10  ,  20%   ,  30%   )    ;', True),
    ('hsl(361, 50%, 80%)', False),
    ('hsl(300, 101%, 70%)', False),
    ('hsl(200, 55%, 75)', False),
    ('hsl (80, 20%, 10%)', False),
]


@mark.parametrize('hsl, expected', tests)
def test_solution(hsl: str, expected: bool) -> None:
    assert is_valid_hsl(hsl) == expected


if __name__ == '__main__':
    # hsl, expected = tests[0]
    # print(is_valid_hsl(hsl))
    print(is_valid_hsl('hsl(360, 09%, 09%)'))
