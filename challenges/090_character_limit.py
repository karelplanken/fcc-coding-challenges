# Daily Coding challenge #90 (2025-11-08) - freeCodeCamp.org
# Character Limit
# In this challenge, you are given a string and need to determine if it fits in a
# social media post. Return the following strings based on the rules given:

# "short post" if it fits within a 40-character limit.
# "long post" if it's greater than 40 characters and fits within an 80-character limit.
# "invalid post" if it's too long to fit within either limit.
from pytest import mark


def can_post(message: str) -> str:
    chars = len(message)
    if chars > 80:
        return 'invalid post'
    elif chars > 40:
        return 'long post'
    else:
        return 'short post'


# Short but discouraged because of nested ternary:
# def can_post(message: str) -> str:
#     chars = len(message)
#     return (
#         'invalid post' if chars > 80 else 'long post' if chars > 40 else 'short post'
#     )


tests = [
    ('Hello world', 'short post'),
    ('This is a longer message but still under eighty characters.', 'long post'),
    (
        'This message is too long to fit into either of the character limits for a'
        + ' social media post.',
        'invalid post',
    ),
]


@mark.parametrize(('message', 'expected'), tests)
def test_can_post(message: str, expected: str) -> None:
    assert can_post(message) == expected


if __name__ == '__main__':
    message, expected = tests[0]
    print(can_post(message))
