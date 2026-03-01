# Daily Coding challenge #65 (2025-10-14) - freeCodeCamp.org
# String Count
# Given two strings, determine how many times the second string appears in the first.

# The pattern string can overlap in the first string. For example, "aaa" contains "aa"
# twice. The first two a's and the second two.
from pytest import mark


def count(text: str, parameter: str) -> int:
    parameter_length = len(parameter)
    return sum(
        1
        for i in range(len(text) - parameter_length + 1)
        if parameter == text[i : parameter_length + i]
    )


# Speed champion alternative:
# def count(text: str, parameter: str) -> int:
#     """Fastest for most cases - uses optimized built-in method."""
#     if not parameter:
#         return 0

#     count = 0
#     start = 0
#     while True:
#         pos = text.find(parameter, start)
#         if pos == -1:
#             break
#         count += 1
#         start = pos + 1
#     return count


tests = [
    ('abcdefg', 'def', 1),
    ('hello', 'world', 0),
    ('mississippi', 'iss', 2),
    ('she sells seashells by the seashore', 'sh', 3),
    ('101010101010101010101', '101', 10),
]


@mark.parametrize('text, parameter, expected', tests)
def test_count(text: str, parameter: str, expected: int) -> None:
    assert count(text, parameter) == expected


if __name__ == '__main__':
    text, parameter, expected = tests[4]
    print(count(text, parameter))
