# Daily Coding challenge #100 (2025-11-18) - freeCodeCamp.org
# 100 Characters
# Welcome to the 100th Daily Coding Challenge!

# Given a string, repeat its characters until the result is exactly 100 characters long.
#  If your repetitions go over 100 characters, trim the extra so it's exactly 100.
from pytest import mark


def one_hundred(chars: str) -> str:
    length = len(chars)
    return ''.join(chars[i % length] for i in range(100))


# def one_hundred(chars):
#     repeated = chars * (100 // len(chars) + 1)
#     return repeated[:100]

# def one_hundred(chars):
#     return (chars * 100)[:100]


tests = [
    (
        'One hundred ',
        'One hundred One hundred One hundred One hundred One hundred One hundred One '
        + 'hundred One hundred One ',
    ),
    (
        'freeCodeCamp ',
        'freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp '
        + 'freeCodeCamp freeCodeC',
    ),
    (
        'daily challenges ',
        'daily challenges daily challenges daily challenges daily challenges daily '
        + 'challenges daily challenge',
    ),
    (
        '!',
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',
    ),
]


@mark.parametrize(('chars', 'expected'), tests)
def test_one_hundred(chars: str, expected: str) -> None:
    assert one_hundred(chars) == expected


if __name__ == '__main__':
    chars, expected = tests[0]
    print(one_hundred(chars))
