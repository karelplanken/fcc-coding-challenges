# Daily Coding challenge #66 (2025-10-15) - freeCodeCamp.org
# HTML Tag Stripper
# Given a string of HTML code, remove the tags and return the plain text content.

# The input string will contain only valid HTML.
# HTML tags may be nested.
# Remove the tags and any attributes.
# For example, '<a href="#">Click here</a>' should return "Click here".
import re

from pytest import mark


def strip_tags(html: str) -> str:
    """Remove HTML tags from a string and return plain text content."""
    return re.sub(r'<[^>]*>', '', html)


# Less eficient alternative using findall:
# def strip_tags(html: str) -> str:
#     matches = re.findall(r'>([^<]*)<', html)
#     return ''.join(matches)

tests = [
    ('<a href="#">Click here</a>', 'Click here'),
    ('<p class="center">Hello <b>World</b>!</p>', 'Hello World!'),
    ('<img src="cat.jpg" alt="Cat">', ''),
    (
        '<main id="main"><section class="section">section</section><section '
        + 'class="section">section</section></main>',
        'sectionsection',
    ),
]


@mark.parametrize('html, expected', tests)
def test_strip_tags(html: str, expected: str) -> None:
    assert strip_tags(html) == expected


if __name__ == '__main__':
    html, expected = tests[3]
    print(strip_tags(html))
