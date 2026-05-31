# Daily Coding challenge #283 (2026-05-20) - freeCodeCamp.org
# String Zipper
# Given two strings, return a new string that interleaves their characters one at a
# time. If one string is longer, append the remaining characters at the end.
# Begin with the first character of the first string.
from itertools import zip_longest

from pytest import mark


def zip_strings(a: str, b: str) -> str:
    return ''.join(c for pair in zip_longest(a, b, fillvalue='') for c in pair)


tests = [
    ('abc', '123', 'a1b2c3'),
    ('acegikmoqsuwy', 'bdfhjlnprtvxz', 'abcdefghijklmnopqrstuvwxyz'),
    ('day', 'night', 'dnaiyght'),
    ('python', 'javascript', 'pjyatvhaosncript'),
    ('feCdCm', 'reoeap', 'freeCodeCamp'),
]


@mark.parametrize('a, b, expected', tests)
def test_zip_strings(a: str, b: str, expected: str) -> None:
    assert zip_strings(a, b) == expected


if __name__ == '__main__':
    a, b, expected = tests[4]
    print(zip_strings(a, b))
