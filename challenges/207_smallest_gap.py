# Daily Coding challenge #207 (2026-03-05) - freeCodeCamp.org
# Smallest Gap
# Given a string, return the substring between the two identical characters that have
# the smallest number of characters between them (smallest gap).

# There will always be at least one pair of matching characters.
# The returned substring should exclude the matching characters.
# If two or more gaps are the same length, return the characters from the first one.
# For example, given "ABCDAC", return "DA".

# Only "A" and "C" repeat in the string.
# The number of characters between the two "A" characters is 3, and between the "C"
# characters is 2.
# So return the string between the two "C" characters.
from pytest import mark


def smallest_gap(s: str) -> str:
    min_gap = None

    for i, char in enumerate(s):
        j = s.find(char, i + 1)
        if j != -1:
            gap = s[i + 1 : j]
            if min_gap is None or len(gap) < len(min_gap):
                min_gap = gap

    return min_gap or ''


tests = [
    ('ABCDAC', 'DA'),
    ('racecar', 'e'),
    ('A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4', '#q6e&rkf(p'),
    ('Hello World', ''),
    ('The quick brown fox jumps over the lazy dog.', 'fox'),
]


@mark.parametrize('s, expected', tests)
def test(s: str, expected: str) -> None:
    assert smallest_gap(s) == expected


if __name__ == '__main__':
    s, expected = tests[4]
    print(smallest_gap(s))
