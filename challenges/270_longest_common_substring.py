# Daily Coding challenge #270 (2026-05-07) - freeCodeCamp.org
# Longest Common Substring
# Given a string, return the longest substring that appears more than once.

# The substrings can overlap.
from pytest import mark


def get_longest_substring(s: str) -> str | None:
    chars = len(s)
    return max(
        (
            s[i:j]
            for i in range(chars)
            for j in range(i + 1, chars)
            if s[i:j] in s[i + 1 :]
        ),
        key=len,
    )


tests = [
    ('abracadabra', 'abra'),
    ('hello world hello', 'hello'),
    ('mississippi', 'issi'),
    ('ha ha ha ha ha ha ha', 'ha ha ha ha ha ha'),
    (
        'the quick brown fox jumped over the lazy dog that the quick brown fox jumped '
        + 'over',
        'the quick brown fox jumped over',
    ),
]


@mark.parametrize('s, expected', tests)
def test_get_longest_substring(s: str, expected: str) -> None:
    assert get_longest_substring(s) == expected


if __name__ == '__main__':
    s, expected = tests[4]
    print(get_longest_substring(s))
