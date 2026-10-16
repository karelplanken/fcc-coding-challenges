"""Daily Coding Challenge #66 (2025-10-15) - freeCodeCamp.org."""

# HTML Tag Stripper
# Given a string of HTML code, remove the tags and return the plain text content.
#
# - The input string will contain only valid HTML.
# - HTML tags may be nested.
# - Remove the tags and any attributes.
#
# For example, '<a href="#">Click here</a>' should return "Click here".
import re

from pytest import mark

# A tag is '<' followed by any mix of: quoted strings (which may contain '>')
# or non-quote, non-'>' characters, then '>'. Comments are matched first
# because they may contain '>' and unbalanced quotes.
_TAG_RE = re.compile(
    r"""
    <!--.*?-->                      # comment
    |
    <(?:[^>"']|"[^"]*"|'[^']*')*>   # tag, honouring quoted attribute values
    """,
    re.DOTALL | re.VERBOSE,
)


def strip_tags(html: str) -> str:
    """Remove HTML tags, attributes and comments, returning the text content.

    Character entities (e.g. ``&amp;``) are left undecoded, and the text inside
    ``<script>``/``<style>`` elements is kept, since the spec does not say
    otherwise.

    Args:
        html: Valid HTML code to strip.

    Returns:
        The text content with all markup removed.
    """
    return _TAG_RE.sub('', html)


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
    """Test strip_tags function."""
    assert strip_tags(html) == expected


if __name__ == '__main__':
    html, expected = tests[0]
    print(strip_tags(html))
