# Daily Coding challenge #265 (2026-05-02) - freeCodeCamp.org
# Deepest Brackets
# Given a string containing balanced brackets, return the content of the deepest nested
# brackets.

# Brackets can be any of the three types: (), [], and {}.
# The input will always have a single deepest group.
# For example, given "(hello (world))", return "world".
from pytest import mark

OPENING = set('([{')
CLOSING = set(')]}')


def get_deepest_brackets(s: str) -> str:
    depth = max_depth = 0
    deepest_open = 0

    for i, char in enumerate(s):
        if char in OPENING:
            depth += 1
            if depth > max_depth:
                max_depth = depth
                deepest_open = i
        elif char in CLOSING:
            depth -= 1

    start = deepest_open + 1
    end = next(i for i, c in enumerate(s[start:], start) if c in CLOSING)
    return s[start:end]


tests = [
    ('(hello (world))', 'world'),
    ('[outer [inner] outer]', 'inner'),
    ('{a{b}c{d{e}f}g}', 'e'),
    ('[the {quick (brown [fox] jumped) over (the) lazy} dog]', 'fox'),
    ('f[(r)e{e}C{o[(d){e(C)}a]m}]p', 'C'),
]


@mark.parametrize('s, expected', tests)
def test(s: str, expected: str) -> None:
    assert get_deepest_brackets(s) == expected


if __name__ == '__main__':
    s, expected = tests[4]
    print(get_deepest_brackets(s))
