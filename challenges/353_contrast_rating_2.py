# Daily Coding challenge #353 (2026-07-29) - freeCodeCamp.org
# Contrast Rating 2
# Given two relative luminance values and a boolean indicating whether the text is
# large, return the WCAG contrast rating using the following method:
#
# Calculate the contrast ratio by adding 0.05 to each luminance value, then dividing the
# lighter one by the darker one. The lighter one will always be the first argument.
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


def get_contrast_rating(l1: float, l2: float, is_large_text: bool) -> str:
    contrast_ratio = compute_contrast_ratio(l1, l2)
    breakpoints, labels = RATINGS[is_large_text]
    idx = bisect_right(breakpoints, contrast_ratio) - 1
    if idx < 0:
        raise ValueError(
            f'rating cannot be determined for {l1=}, {l2=}, and {is_large_text=}'
        )
    return labels[idx]


tests = [
    (1.0, 0.0, False, 'AAA'),
    (0.9015, 0.1364, False, 'AA'),
    (0.8965, 0.1628, False, 'Fail'),
    (0.7469, 0.0957, True, 'AAA'),
    (0.7489, 0.2018, True, 'AA'),
    (0.6571, 0.1974, True, 'Fail'),
]


@mark.parametrize('l1, l2, is_large_text, expected', tests)
def test_get_contrast_rating(
    l1: float, l2: float, is_large_text: bool, expected: str
) -> None:
    assert get_contrast_rating(l1, l2, is_large_text) == expected


if __name__ == '__main__':
    l1, l2, is_large_text, expected = tests[2]
    print(get_contrast_rating(l1, l2, is_large_text))
