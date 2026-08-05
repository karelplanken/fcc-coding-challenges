# Daily Coding challenge #337 (2026-07-13) - freeCodeCamp.org
# Tally Counter
# Given a string of tally marks, return the total count represented.
#
# - Each pipe `"|"` represents one count.
# - Every fifth mark is represented as a forward slash `"/"`, completing a group of five
#   (`"||||/"`).
# - Groups are separated by a space.
from pytest import mark


def is_valid_tally(groups: list[str]) -> bool:
    if not groups:
        return False
    *completed, last = groups
    if any(group != '||||/' for group in completed):
        return False
    return last == '||||/' or (1 <= len(last) <= 4 and set(last) == {'|'})


def get_tally_count(s: str) -> int:
    groups = s.split()
    if not is_valid_tally(groups):
        raise ValueError('invalid tally string')
    return sum(5 if g == '||||/' else len(g) for g in groups)


tests = [
    ('||||', 4),
    ('||||/', 5),
    ('||||/ |||', 8),
    ('||||/ ||||/ ||||/ ||', 17),
    ('||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ |', 41),
]


@mark.parametrize('s, expected', tests)
def test_get_tally_count(s: str, expected: int) -> None:
    assert get_tally_count(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(get_tally_count(s))
