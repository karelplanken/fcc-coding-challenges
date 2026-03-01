# Daily Coding challenge #168 (2026-01-25) - freeCodeCamp.org
# Scaled Image
# Given a string representing the width and height of an image, and a number to scale
# the image, return the scaled width and height.

# The input string is in the format "WxH". For example, "800x600".
# The scale is a number to multiply the width and height by.
# Return the scaled dimensions in the same "WxH" format.
from pytest import mark


def scale_image(size: str, scale: float) -> str:
    width, height = (int(float(x) * scale) for x in size.split('x'))
    return f'{width}x{height}'


tests = [
    ('800x600', 2, '1600x1200'),
    ('100x100', 10, '1000x1000'),
    ('1024x768', 0.5, '512x384'),
    ('300x200', 1.5, '450x300'),
]


@mark.parametrize('size,scale,expected', tests)
def test_scale_image(size: str, scale: float, expected: str) -> None:
    assert scale_image(size, scale) == expected


if __name__ == '__main__':
    size, scale, expected = tests[0]
    print(scale_image(size, scale))
