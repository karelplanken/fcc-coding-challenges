# Daily Coding challenge #115 (2025-12-03) - freeCodeCamp.org
# Markdown Ordered List Item Converter
# Given a string representing an ordered list item in Markdown, return the equivalent
# HTML string.

# A valid ordered list item in Markdown must:

# Start with zero or more spaces, followed by
# A number (1 or greater) and a period (.), followed by
# At least one space, and then
# The list item text.
# If the string doesn't have the exact format above, return "Invalid format". Otherwise,
# wrap the list item text in li tags and return the string.

# For example, given "1. My item", return "<li>My item</li>"

# Note: The console may not display HTML tags in strings when logging messages. Check
# the browser console to see logs with tags included.
import re

from pytest import mark


def convert_list_item(markdown: str) -> str:
    match = re.match(r'^\s*([1-9]\d*)\.\s+(.+)$', markdown)
    return f'<li>{match.group(2)}</li>' if match else 'Invalid format'


# import re

# MARKDOWN_LIST_PATTERN = re.compile(r'^\s*([1-9]\d*)\.\s+(.+)$')

# def convert_list_item(markdown: str) -> str:
#     match = MARKDOWN_LIST_PATTERN.match(markdown)
#     return f'<li>{match.group(2)}</li>' if match else 'Invalid format'

# def convert_list_item(markdown: str) -> str:
#     match = MARKDOWN_LIST_PATTERN.match(markdown)

#     if not match:
#         return "Invalid format"

#     number, text = match.groups()

#     if int(number) < 1:
#         return "Invalid format"

#     return f"<li>{text}</li>"

tests = [
    ('1. My item', '<li>My item</li>'),
    (' 1.  Another item', '<li>Another item</li>'),
    ('1 . invalid item', 'Invalid format'),
    ('2. list item text', '<li>list item text</li>'),
    ('. invalid again', 'Invalid format'),
    ('A. last invalid', 'Invalid format'),
    ('0. My item', 'Invalid format'),
]


@mark.parametrize('markdown,expected', tests)
def test_convert_list_item(markdown: str, expected: str) -> None:
    assert convert_list_item(markdown) == expected


if __name__ == '__main__':
    markdown, expected = tests[0]
    print(convert_list_item(markdown))
