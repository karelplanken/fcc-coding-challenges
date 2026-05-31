# Daily Coding challenge #277 (2026-05-14) - freeCodeCamp.org
# Mirror Image
# Given two strings, determine if the second string is a mirror image of the first.
# A mirror image is formed by reversing the string and replacing each character with
# its mirror equivalent.
# Symmetric characters look like themselves in a mirror:
# W, T, Y, U, I, O, H, A, X, V, M, w, o, x, v, 0, 8, =, +, :, |, -, _, *, ^, !, ., and
# the space ( ).
# Mirrored pairs swap with each other in a mirror:
# Character	Swaps with
# [	]
# {	}
# <	>
# b	d
# p	q
# (	)
# If either string includes a character not in the lists above, it doesn't have mirror
# image that can be created from the characters.
# For example, the mirrored image of "[HOW]" is "[WOH]".
from types import MappingProxyType

from pytest import mark

SYMMETRIC_CHARS = frozenset('WTYUIOHAXVMwoxv08=+:|-_*^!. ')

SWAPPED_CHARS = MappingProxyType({
    '[': ']',
    '{': '}',
    '<': '>',
    'b': 'd',
    'p': 'q',
    '(': ')',
})

MIRROR_MAP = MappingProxyType(
    SWAPPED_CHARS
    | {v: k for k, v in SWAPPED_CHARS.items()}
    | {c: c for c in SYMMETRIC_CHARS}
)


def is_mirror_image(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    s1_mirrored = (MIRROR_MAP.get(char) for char in reversed(s1))

    return all(m is not None and m == s for m, s in zip(s1_mirrored, s2))


# def is_mirror_image(s1: str, s2: str) -> bool:
#     if len(s1) != len(s2):
#         return False
#     for c1, c2 in zip(reversed(s1), s2):
#         m = MIRROR_MAP.get(c1)
#         if m is None or m != c2 or c2 not in MIRROR_MAP:
#             return False
#     return True


tests = [
    ('[HOW]', '[WOH]', True),
    ('MOM', 'MOM', True),
    ('vow', 'wov', True),
    ('TIM', 'TIM', False),
    ('{WOW}', '}WOW{', False),
    ('XXVII', 'IIV%X', False),
    ('><(((*>', '<*)))><', True),
    (
        'WTYUIOHAXVMwoxv08=+:|-_*^!.[]{}<>bdpq()',
        '()pqbd<>{}[].!^*_-|:+=80vxowMVXAHOIUYTW',
        True,
    ),
]


@mark.parametrize('s1, s2, expected', tests)
def test(s1: str, s2: str, expected: bool) -> None:
    assert is_mirror_image(s1, s2) == expected


if __name__ == '__main__':
    s1, s2, expected = tests[0]
    print(is_mirror_image(s1, s2))
