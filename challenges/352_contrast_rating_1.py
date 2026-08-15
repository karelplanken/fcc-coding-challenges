# Daily Coding challenge #352 (2026-07-28) - freeCodeCamp.org
# Contrast Rating 1
# Given a contrast ratio and a boolean indicating whether the text is large, return the
# WCAG rating using the following table:
#
# | Rating | Normal Text | Large Text |
# |--------|-------------|------------|
# | "AAA" | 7.0+ | 4.5+ |
# | "AA" | 4.5+ | 3.0+ |
# | "Fail" | below 4.5 | below 3.0 |
# Daily Coding challenge #352 (2026-07-28) - freeCodeCamp.org
# Contrast Rating 1
# Given a contrast ratio and a boolean indicating whether the text is large, return the
# WCAG rating using the following table:
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


def get_contrast_rating(ratio: str, is_large_text: bool) -> str:
    contrast_ratio = float(ratio)
    breakpoints, labels = RATINGS[is_large_text]
    idx = bisect_right(breakpoints, contrast_ratio) - 1
    if idx < 0:
        raise ValueError(
            f'rating cannot be determined for {ratio=} and {is_large_text=}'
        )
    return labels[idx]


tests = [
    ('7.5', False, 'AAA'),
    ('4.8', False, 'AA'),
    ('4.2', False, 'Fail'),
    ('4.5', True, 'AAA'),
    ('3.0', True, 'AA'),
    ('2.7', False, 'Fail'),
]


@mark.parametrize('ratio, is_large_text, expected', tests)
def test_get_contrast_rating(ratio: str, is_large_text: bool, expected: str) -> None:
    assert get_contrast_rating(ratio, is_large_text) == expected


if __name__ == '__main__':
    ratio, is_large_text, expected = tests[0]
    print(get_contrast_rating(ratio, is_large_text))
