# Daily Coding challenge #129 (2025-12-17) - freeCodeCamp.org
# Markdown Blockquote Parser
# Given a string that includes a blockquote in Markdown, return the equivalent HTML
# string.

# A blockquote in Markdown is any line that:

# Starts with zero or more spaces
# Followed by a greater-than sign (>)
# Then, one or more spaces
# And finally, the blockquote text.
# Return the blockquote text surrounded by opening and closing HTML blockquote tags.

# For example, given "> This is a quote",
# return <blockquote>This is a quote</blockquote>.

# Note: The console may not display HTML tags in strings when logging messages.
# Check the browser console to see logs with tags included.
import re

from pytest import mark

pattern = re.compile(r'^ *> +(.*)$')


def parse_blockquote(markdown: str) -> str | None:
    match = pattern.match(markdown)
    return f'<blockquote>{match.group(1)}</blockquote>' if match else None


tests = [
    ('> This is a quote', '<blockquote>This is a quote</blockquote>'),
    (' > This is also a quote', '<blockquote>This is also a quote</blockquote>'),
    ('  >    So  Is  This', '<blockquote>So  Is  This</blockquote>'),
]


@mark.parametrize('markdown, expected', tests)
def test_parse_blockquote(markdown: str, expected: str) -> None:
    assert parse_blockquote(markdown) == expected


if __name__ == '__main__':
    markdwon, expected = tests[0]
    print(parse_blockquote(markdwon))
