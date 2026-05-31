# Daily Coding challenge #292 (2026-05-29) - freeCodeCamp.org
# Wider Aspect Ratio
# Given two strings for different image dimensions, return the aspect ratio of the
# image with a greater width-to-height ratio.

# The given strings will be in the format "WxH", for example, "1920x1080".
# The aspect ratio is the ratio of width to height, reduced to the lowest whole
# numbers. For example, "1920x1080" reduces to "16:9".
# Return a string in format "W:H", for example, "16:9".
from dataclasses import dataclass, field
from math import gcd

from pytest import mark


@dataclass(order=True)
class ImageDimension:
    aspect_ratio: float = field(init=False)
    width: int
    height: int

    def __post_init__(self) -> None:
        self.aspect_ratio = self.width / self.height

    def __str__(self) -> str:
        ar_gcd = gcd(self.width, self.height)
        return f'{self.width // ar_gcd}:{self.height // ar_gcd}'


def get_wider_aspect_ratio(a: str, b: str) -> str:
    img_dim = max(
        ImageDimension(*map(int, a.split('x'))), ImageDimension(*map(int, b.split('x')))
    )
    return str(img_dim)


tests = [
    ('1920x1080', '80000x60000', '16:9'),
    ('1080x1350', '2048x1536', '4:3'),
    ('640x480', '2440x1220', '2:1'),
    ('360x640', '1080x1920', '9:16'),
    ('3440x1440', '2048x858', '43:18'),
    ('12345x61234', '12534x51234', '2089:8539'),
]


@mark.parametrize('a, b, expected', tests)
def test_get_wider_aspect_ratio(a: str, b: str, expected: str) -> None:
    assert get_wider_aspect_ratio(a, b) == expected


if __name__ == '__main__':
    a, b, expected = tests[0]
    print(get_wider_aspect_ratio(a, b))
