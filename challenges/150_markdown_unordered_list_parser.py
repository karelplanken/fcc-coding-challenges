# Daily Coding challenge #150 (2026-01-07) - freeCodeCamp.org
# Markdown Unordered List Parser
# Given the string of a valid unordered list in Markdown, return the equivalent HTML
# string.

# An unordered list consists of one or more list items. A valid list item appears on
# its own line and:
# Starts with a dash ("-"), followed by
# At least one space, and then
# The list item text.
# The list is given as a single string with new lines separated by the newline
# character ("\n"). Do not include the newline characters in the item text.
# Wrap each list item in HTML li tags, and the whole list of items in ul tags.
# For example, given "- Item A\n- Item B",
# return "<ul><li>Item A</li><li>Item B</li></ul>".
# Note: The console may not display HTML tags in strings when logging messages. Check
# the browser console to see logs with tags included.
import re

from pytest import mark


def parse_unordered_list(markdown: str) -> str:
    pattern = r'-\s+(.*)$'
    matches = re.findall(pattern, markdown, re.MULTILINE)
    return f'<ul>{"".join(f"<li>{match}</li>" for match in matches)}</ul>'


tests = [
    ('- Item A\n- Item B', '<ul><li>Item A</li><li>Item B</li></ul>'),
    ('-  JavaScript\n-  Python', '<ul><li>JavaScript</li><li>Python</li></ul>'),
    (
        '- 2 C Flour\n- 1/2 C Sugar\n- 1 Tsp Vanilla',
        '<ul><li>2 C Flour</li><li>1/2 C Sugar</li><li>1 Tsp Vanilla</li></ul>',
    ),
    ('- A-1\n- A-2\n- B-1', '<ul><li>A-1</li><li>A-2</li><li>B-1</li></ul>'),
]


@mark.parametrize(('markdown', 'expected'), tests)
def test_parse_unordered_list(markdown: str, expected: str) -> None:
    assert parse_unordered_list(markdown) == expected


if __name__ == '__main__':
    markdown, expected = tests[0]
    print(parse_unordered_list(markdown))
