# Daily Coding challenge #23 (2025-09-02) - freeCodeCamp.org
# RGB to Hex
# Given a CSS rgb(r, g, b) color string, return its hexadecimal equivalent.

# Here are some example outputs for a given input:

# Input	Output
# "rgb(255, 255, 255)"	"#ffffff"
# "rgb(1, 2, 3)"	"#010203"
# Make any letters lowercase.
# Return a # followed by six characters. Don't use any shorthand values.
from pytest import mark


def rgb_to_hex(rgb: str) -> str:
    return '#' + ''.join(f'{int(color):02x}' for color in rgb[4:-1].split(', '))


tests = [
    ('rgb(255, 255, 255)', '#ffffff'),
    ('rgb(1, 11, 111)', '#010b6f'),
    ('rgb(173, 216, 230)', '#add8e6'),
    ('rgb(79, 123, 201)', '#4f7bc9'),
]


@mark.parametrize('rgb, expected', tests)
def test_rgb_to_hex(rgb: str, expected: str) -> None:
    assert rgb_to_hex(rgb) == expected


if __name__ == '__main__':
    rgb, expected = tests[0]
    print(rgb_to_hex(rgb))
