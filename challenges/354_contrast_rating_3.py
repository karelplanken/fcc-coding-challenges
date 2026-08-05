# Daily Coding challenge #354 (2026-07-30) - freeCodeCamp.org
# Contrast Rating 3
# Given two arrays representing RGB values and a boolean indicating whether the text is
# large, return the WCAG contrast rating using the following method:
#
# First, convert each RGB value to relative luminance:
#
# - Divide each channel [R, G, B] by 255 to get a value between 0 and 1
# - Apply the gamma correction formula to each channel:
#   - If the channel value is less than or equal to 0.04045: channel / 12.92
#   - Otherwise: ((channel + 0.055) / 1.055) ^ 2.4
# - Calculate luminance: 0.2126 * R + 0.7152 * G + 0.0722 * B
#
# Then, calculate the contrast ratio by adding 0.05 to each luminance value, then
# dividing the lighter one by the darker one. The lighter one will always be the first
# argument.
#
# Return the rating based on the contrast ratio using the following table:
#
# | Rating | Normal Text | Large Text |
# |--------|-------------|------------|
# | "AAA" | 7.0+ | 4.5+ |
# | "AA" | 4.5+ | 3.0+ |
# | "Fail" | below 4.5 | below 3.0 |
from bisect import bisect_right
from types import MappingProxyType

from pytest import mark

# breakpoints[i] and labels[i] are index-aligned (same length, ascending order) —
# bisect_right finds the last breakpoint <= ratio
RATINGS = MappingProxyType({
    False: ((0.0, 4.5, 7.0), ('Fail', 'AA', 'AAA')),
    True: ((0.0, 3.0, 4.5), ('Fail', 'AA', 'AAA')),
})

for breakpoints, labels in RATINGS.values():
    assert len(breakpoints) == len(labels), (
        'breakpoints and labels must be index-aligned'
    )


def compute_contrast_ratio(lighter_luminance: float, darker_luminance: float) -> float:
    return (lighter_luminance + 0.05) / (darker_luminance + 0.05)


def gamma_correct(channel: float) -> float:
    linear = channel / 255
    return linear / 12.92 if linear <= 0.04045 else ((linear + 0.055) / 1.055) ** 2.4


def compute_luminance(rgb: list[int]) -> float:
    r, g, b = (gamma_correct(channel) for channel in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def get_contrast_rating(rgb1: list[int], rgb2: list[int], is_large_text: bool) -> str:
    l1, l2 = compute_luminance(rgb1), compute_luminance(rgb2)
    lighter_luminance, darker_luminance = (l1, l2) if l1 > l2 else (l2, l1)
    contrast_ratio = compute_contrast_ratio(lighter_luminance, darker_luminance)
    breakpoints, labels = RATINGS[is_large_text]
    idx = bisect_right(breakpoints, contrast_ratio) - 1
    if idx < 0:
        raise ValueError(
            f'rating cannot be determined for {rgb1=}, {rgb2=}, and {is_large_text=}'
        )
    return labels[idx]


tests = [
    ([255, 255, 255], [0, 0, 0], False, 'AAA'),
    ([215, 188, 188], [55, 55, 55], False, 'AA'),
    ([143, 144, 210], [46, 47, 61], False, 'Fail'),
    ([167, 167, 210], [53, 10, 53], True, 'AAA'),
    ([135, 147, 155], [60, 70, 90], True, 'AA'),
    ([125, 210, 195], [105, 130, 90], True, 'Fail'),
]


@mark.parametrize('rgb1, rgb2, is_large_text, expected', tests)
def test_get_contrast_rating(
    rgb1: list[int], rgb2: list[int], is_large_text: bool, expected: str
) -> None:
    assert get_contrast_rating(rgb1, rgb2, is_large_text) == expected


if __name__ == '__main__':
    rgb1, rgb2, is_large_text, expected = tests[5]
    print(get_contrast_rating(rgb1, rgb2, is_large_text))
