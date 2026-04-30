# Daily Coding challenge #235 (2026-04-02) - freeCodeCamp.org
# Capitalized Fibonacci
# Given a string, return a new string where each letter is capitalized if its index is
# a Fibonacci number, and lowercased otherwise.

# The Fibonacci sequence is a series of numbers where each number is the sum of the two
# preceding ones. The first 10 numbers in the sequence are
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

# The first character is at index 0.
# If the index of non-letter characters is a Fibonacci number, leave it unchanged.
from collections.abc import Iterator

from pytest import mark


def fibonacci_indices(limit: int) -> Iterator[int]:
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


def capitalize_fibonacci(s: str) -> str:
    fib_set = set(fibonacci_indices(len(s)))
    return ''.join(
        char.upper() if i in fib_set else char.lower() for i, char in enumerate(s)
    )


tests = [
    ('hello world', 'HELLo woRld'),
    ('HELLO WORLD', 'HELLo woRld'),
    ('hello, world!', 'HELLo, wOrld!'),
    (
        'The quick brown fox jumped over the lazy dog.',
        'THE qUicK broWn fox jUmped over thE lazy dog.',
    ),
    (
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar ex '
        + 'nibh, vel ullamcorper ligula egestas quis. Integer tincidunt fringilla '
        + 'accumsan. Integer et metus placerat, gravida felis at, pellentesque nisl.',
        'LOREm ipSum dOlor sit amet, consecTetur adipiscing elit. proin pulvinar ex '
        + 'nibh, vel ullaMcorper ligula egestas quis. integer tincidunt fringillA '
        + 'accumsan. integer et metus placerat, gravida felis at, pellentesque nisl.',
    ),
]


@mark.parametrize('s, expected', tests)
def test_solution(s: str, expected: str) -> None:
    assert capitalize_fibonacci(s) == expected


if __name__ == '__main__':
    s, expected = tests[2]
    print(capitalize_fibonacci(s))
