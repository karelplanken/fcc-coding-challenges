# Daily Coding challenge #101 (2025-11-19) - freeCodeCamp.org
# Markdown Heading Converter
# Given a string representing a Markdown heading, return the equivalent HTML heading.

# A valid Markdown heading must:

# Start with zero or more spaces, followed by
# 1 to 6 hash characters (#) in a row, then
# At least one space. And finally,
# The heading text.
# The number of hash symbols determines the heading level. For example, one hash symbol
# corresponds to an h1 tag, and six hash symbols correspond to an h6 tag.

# If the given string doesn't have the exact format above, return "Invalid format".

# For example, given "# My level 1 heading", return "<h1>My level 1 heading</h1>".

# Note: The console may not display HTML tags in strings when logging messages. Check
# the browser console to see logs with tags included.
import re

from pytest import mark


def convert(heading: str) -> str:
    pattern = r'(?:\s*)(#+)(?:\s+)(.+)'
    match = re.match(pattern, heading)
    h_level = None
    if match:
        level, text = match.groups()
        h_level = len(level)

    if h_level and h_level <= 6:
        return f'<h{h_level}>{text}</h{h_level}>'

    return 'Invalid format'


tests = [
    ('# My level 1 heading', '<h1>My level 1 heading</h1>'),
    ('My heading', 'Invalid format'),
    ('##### My level 5 heading', '<h5>My level 5 heading</h5>'),
    ('#My heading', 'Invalid format'),
    ('  ###  My level 3 heading', '<h3>My level 3 heading</h3>'),
    ('####### My level 7 heading', 'Invalid format'),
    ('## My #2 heading', '<h2>My #2 heading</h2>'),
]


@mark.parametrize('heading, expected', tests)
def test_convert(heading: str, expected: str) -> None:
    assert convert(heading) == expected


if __name__ == '__main__':
    heading, expected = tests[0]
    print(convert(heading))
