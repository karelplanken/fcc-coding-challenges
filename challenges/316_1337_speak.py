# Daily Coding challenge #316 (2026-06-22) - freeCodeCamp.org
# 1337 Speak
# Given a lowercase string, return it translated into leet speak by replacing the
# letters below with their leet substitutions:
#
# | Letter | Leet |
# | - | - |
# | `a` | `4` |
# | `e` | `3` |
# | `g` | `9` |
# | `i` | `1` |
# | `l` | `1` |
# | `o` | `0` |
# | `s` | `5` |
# | `t` | `7` |
#
# - Characters with no substitution are left unchanged.
from types import MappingProxyType

from pytest import mark

_LEET = MappingProxyType({
    'a': '4',
    'e': '3',
    'g': '9',
    'i': '1',
    'l': '1',
    'o': '0',
    's': '5',
    't': '7',
})

# .copy() required: str.maketrans rejects MappingProxyType at runtime
_TABLE = str.maketrans(_LEET.copy())


def make_leet(s: str) -> str:
    return s.translate(_TABLE)


tests = [
    ('cool', 'c001'),
    ('leet', '1337'),
    ('hacker', 'h4ck3r'),
    ('satellite', '547311173'),
    ('abcdefghijklmnopqrstuvwxyz', '4bcd3f9h1jk1mn0pqr57uvwxyz'),
]


@mark.parametrize('s, expected', tests)
def test_make_leet(s: str, expected: str) -> None:
    assert make_leet(s) == expected


if __name__ == '__main__':
    s, expected = tests[4]
    print(make_leet(s))
