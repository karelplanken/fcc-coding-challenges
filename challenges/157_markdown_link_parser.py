# Daily Coding challenge #157 (2026-01-14) - freeCodeCamp.org
# Markdown Link Parser
# Given the string of a link in Markdown, return the equivalent HTML string.

# A Markdown image has the following format: "[link_text](link_url)". Return the string
# of the HTML `a` tag with the `href` set to the link_url and the link_text as the tag
# content.

# For example, given "[freeCodeCamp](https://freecodecamp.org/)" return
# '<a href="https://freecodecamp.org/">freeCodeCamp</a>';

# Note: The console may not display HTML tags in strings when logging messages — check
# the browser console to see logs with tags included.
import re

from pytest import mark


def parse_link(markdown: str) -> str:
    match = re.match(r'^\[(.+?)\]\((https?://[^\s)]+)\)$', markdown)

    if not match:
        raise ValueError(f'Invalid markdown link: {markdown}')

    text, url = match.groups()
    return f'<a href="{url}">{text}</a>'


# # Alternative using re.sub, more verbose, overly complex, and less efficient
# def parse_link(markdown: str) -> str:
#     pattern = r'^\[(.+?)\]\((https?://[^\s)]+)\)$'
#     def replacer(match: re.Match) -> str:
#         text, url = match.group(1), match.group(2)
#         return f'<a href="{url}">{text}</a>'
#     result = re.sub(pattern, replacer, markdown)
#     if result == markdown:
#         raise ValueError(f'Invalid markdown link: {markdown}')
#     return result


tests = [
    (
        '[freeCodeCamp](https://freecodecamp.org/)',
        '<a href="https://freecodecamp.org/">freeCodeCamp</a>',
    ),
    (
        '[Donate to our charity.](https://www.freecodecamp.org/donate/)',
        '<a href="https://www.freecodecamp.org/donate/">Donate to our charity.</a>',
    ),
    (
        '[Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.](https://github.com/freeCodeCamp/freeCodeCamp/)',
        '<a href="https://github.com/freeCodeCamp/freeCodeCamp/">'
        + 'Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.</a>',
    ),
]


@mark.parametrize('markdown, expected', tests)
def test_parse_link(markdown: str, expected: str) -> None:
    assert parse_link(markdown) == expected


if __name__ == '__main__':
    markdown, expected = tests[0]
    print(parse_link(markdown))
