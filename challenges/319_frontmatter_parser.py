# Daily Coding challenge #319 (2026-06-25) - freeCodeCamp.org
# Frontmatter Parser
# Given a string representing a frontmatter block, parse it and return an object
# (JavaScript) or dictionary (Python) with the keys and values.
#
# Frontmatter is wrapped in `---` delimiters and contains `key: value` pairs within
# them, one per line. For example:
#
# ---
# title: My Post
# draft: false
# views: 100
# ---
#
# Should return:
#
# {
#   title: "My Post",
#   draft: false,
#   views: 100
# }
#
# - Numbers, Booleans, and Strings should all be returned as their respective type.
# - The given string will have new lines separated with the newline character (`"\n"`).
#   The above example would be given as: `"---\ntitle: My Post\ndraft: false\nviews:
#   100\n---"`.
import re

from pytest import mark

# Delimiters
_FENCE = re.compile(r'^---\n|\n---$')
_LINE_SEP = '\n'
_KV_SEP = ': '

# Value-type patterns
_BOOL_FALSE = re.compile(r'^false$')
_BOOL_TRUE = re.compile(r'^true$')
_INT = re.compile(r'^\d+$')
_FLOAT = re.compile(r'^\d+\.\d+$')

BasicDataType = bool | int | float | str
BasicDataDict = dict[str, BasicDataType]


def _coerce(value: str) -> BasicDataType:
    if _BOOL_FALSE.match(value):
        return False
    if _BOOL_TRUE.match(value):
        return True
    if _INT.match(value):
        return int(value)
    if _FLOAT.match(value):
        return float(value)
    return value


def parse_frontmatter(s: str) -> BasicDataDict:
    body = _FENCE.sub('', s)
    lines = body.split(_LINE_SEP)
    pairs = [line.split(_KV_SEP, maxsplit=1) for line in lines]
    return {key: _coerce(value) for key, value in pairs}


tests = [
    (
        '---\ntitle: My Post\ndraft: false\nviews: 100\n---',
        {'title': 'My Post', 'draft': False, 'views': 100},
    ),
    (
        '---\nid: 6a174db57256a112f932195c\ntitle: My Book\nlocale: en\nwordCount: '
        + '10000\npublished: false\n---',
        {
            'id': '6a174db57256a112f932195c',
            'title': 'My Book',
            'locale': 'en',
            'wordCount': 10000,
            'published': False,
        },
    ),
    (
        '---\nversion: 1.0.0\nurl: https://example.com\nprivate: true\n---',
        {'version': '1.0.0', 'url': 'https://example.com', 'private': True},
    ),
    ('---\nrating: 4.5\nprice: 9.99\n---', {'rating': 4.5, 'price': 9.99}),
]


@mark.parametrize('s, expected', tests)
def test_parse_frontmatter(s: str, expected: BasicDataDict) -> None:
    assert parse_frontmatter(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(parse_frontmatter(s))
