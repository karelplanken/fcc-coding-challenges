# Daily Coding challenge #122 (2025-12-10) - freeCodeCamp.org
# Markdown Bold Parser
# Given a string that may include some bold text in Markdown,
# return the equivalent HTML string.

# Bold text in Markdown is any text that starts and ends with two
# asterisks (**) or two underscores (__).
# There cannot be any spaces between the text and the asterisks or underscores,
# but there can be spaces in the text itself.
# Convert all bold occurrences to HTML b tags and return the string.
# For example, given "**This is bold**", return "<b>This is bold</b>".

# Note: The console may not display HTML tags in strings when logging messages.
# Check the browser console to see logs with tags included.
import re

from pytest import mark


def parse_bold(markdown: str) -> str:
    # Match ** or __ followed by non-space, then any chars,
    # then non-space, then ** or __
    # Uses negative lookahead/lookbehind to ensure no spaces at boundaries
    pattern = r'(\*\*|__)(?! )(.*?)(?<! )\1'
    return re.sub(pattern, r'<b>\2</b>', markdown)


tests = [
    ('**This is bold**', '<b>This is bold</b>'),
    ('__This is also bold__', '<b>This is also bold</b>'),
    ('**This is not bold **', '**This is not bold **'),
    ('__ This is also not bold__', '__ This is also not bold__'),
    (
        'The **quick** brown fox __jumps__ over the **lazy** dog.',
        'The <b>quick</b> brown fox <b>jumps</b> over the <b>lazy</b> dog.',
    ),
    ('**This is NOT bold__', '**This is NOT bold__'),
]


@mark.parametrize('markdown,expected', tests)
def test_parse_bold(markdown: str, expected: str) -> None:
    assert parse_bold(markdown) == expected


if __name__ == '__main__':
    markdown, expected = tests[0]
    print(parse_bold(markdown))
