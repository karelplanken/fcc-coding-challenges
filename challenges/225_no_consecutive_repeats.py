# Daily Coding challenge #225 (2026-03-23) - freeCodeCamp.org
# No Consecutive Repeats
# Given a string, determine if it has no repeating characters.

# A string has no repeats if it does not have the same character two or more times in
# a row.
from itertools import pairwise

from pytest import mark


def has_no_repeats(s: str) -> bool:
    return all(a != b for a, b in pairwise(s))


tests = [
    ('hi world', True),
    ('hello world', False),
    ('abcdefghijklmnopqrstuvwxyz', True),
    ('freeCodeCamp', False),
    ('The quick brown fox jumped over the lazy dog.', True),
    ('Mississippi', False),
]


@mark.parametrize('s, expected', tests)
def test_solution(s: str, expected: bool) -> None:
    assert has_no_repeats(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(has_no_repeats(s))
