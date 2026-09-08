"""Daily Coding Challenge #23 (2025-09-02) - freeCodeCamp.org."""

# RGB to Hex
# Given a CSS rgb(r, g, b) color string, return its hexadecimal equivalent.
#
# Here are some example outputs for a given input:
#
# | Input               | Output    |
# |---------------------|-----------|
# | "rgb(255, 255, 255)"| "#ffffff" |
# | "rgb(1, 2, 3)"      | "#010203" |
#
# - Make any letters lowercase.
# - Return a # followed by six characters. Don't use any shorthand values.
import re

from pytest import mark

_PATTERN = re.compile(r'rgb\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)')


def rgb_to_hex(rgb: str) -> str:
    """Convert RGB color string to hexadecimal equivalent.

    Args:
        rgb: A CSS rgb(r, g, b) color string.

    Returns:
        The hexadecimal equivalent of the RGB color.

    Raises:
        ValueError: If the input does not match the rgb(...) format, or any channel
            value is outside the 0-255 range.
    """
    match = _PATTERN.match(rgb)
    if not match:
        msg = f'invalid RGB format: {rgb}'
        raise ValueError(msg)

    r, g, b = (int(v) for v in match.groups())
    # Validate channel values are within the range [0, 255] for specific error messages
    # else use something like `if not all(0 <= v <= 255 for v in (r, g, b)):` to check
    # all channels at once
    for name, value in (('r', r), ('g', g), ('b', b)):
        if not 0 <= value <= 255:
            msg = f'channel {name}={value} out of range [0, 255]: {rgb}'
            raise ValueError(msg)

    return f'#{r:02x}{g:02x}{b:02x}'


tests = [
    ('rgb(255, 255, 255)', '#ffffff'),
    ('rgb(1, 11, 111)', '#010b6f'),
    ('rgb(173, 216, 230)', '#add8e6'),
    ('rgb(79, 123, 201)', '#4f7bc9'),
]


@mark.parametrize('rgb, expected', tests)
def test_rgb_to_hex(rgb: str, expected: str) -> None:
    """Test rgb_to_hex function."""
    assert rgb_to_hex(rgb) == expected


if __name__ == '__main__':
    rgb, expected = tests[0]
    print(rgb_to_hex(rgb))
