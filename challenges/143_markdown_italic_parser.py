# Daily Coding challenge #143 (2025-12-31) - freeCodeCamp.org
# Markdown Italic Parser
# Given a string that may include some italic text in Markdown, return the equivalent
# HTML string.

# Italic text in Markdown is any text that starts and ends with a single asterisk (*)
# or a single underscore (_).
# There cannot be any spaces between the text and the asterisk or underscore, but there
# can be spaces in the text itself.
# Convert all italic occurrences to HTML i tags and return the string.
# For example, given "*This is italic*", return "<i>This is italic</i>".

# Note: The console may not display HTML tags in strings when logging messages. Check
# the browser console to see logs with tags included.
import re

from pytest import mark


def parse_italics(markdown: str) -> str:
    """Convert Markdown italic syntax to HTML <i> tags.

    Handles both * and _ delimiters. Text must not have spaces adjacent
    to delimiters. Delimiters must match (no mixing * and _).
    """
    # Pattern explanation:
    # ([*_])           - Capture the opening delimiter (* or _)
    # (\S(?:.*?\S)?)   - Capture content: non-space, optional middle, non-space end
    # \1               - Backreference: closing delimiter must match opening
    pattern = r'([*_])(\S(?:.*?\S)?)\1'

    return re.sub(pattern, r'<i>\2</i>', markdown)


tests = [
    ('*This is italic*', '<i>This is italic</i>'),
    ('_This is also italic_', '<i>This is also italic</i>'),
    ('*This is not italic *', '*This is not italic *'),
    ('_ This is also not italic_', '_ This is also not italic_'),
    (
        'The *quick* brown fox _jumps_ over the *lazy* dog.',
        'The <i>quick</i> brown fox <i>jumps</i> over the <i>lazy</i> dog.',
    ),
    ('*This is not italic_', '*This is not italic_'),
]


@mark.parametrize('markdown, expected', tests)
def test_parse_italics(markdown: str, expected: str) -> None:
    assert parse_italics(markdown) == expected


if __name__ == '__main__':
    markdown, expected = tests[4]
    print(parse_italics(markdown))
