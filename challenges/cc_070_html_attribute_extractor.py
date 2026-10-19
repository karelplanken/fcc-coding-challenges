"""Daily Coding Challenge #70 (2025-10-19) - freeCodeCamp.org."""

# HTML Attribute Extractor
# Given a string of a valid HTML element, return the attributes of the element using
# the following criteria:

# You will only be given one element.
# Attributes will be in the format: attribute="value".
# Return an array of strings with each attribute property and value, separated by a
# comma, in this format: ["attribute1, value1", "attribute2, value2"].
# Return attributes in the order they are given.
# If no attributes are found, return an empty array.
import re

from pytest import mark

# Attribute names: anything except whitespace, quotes, '>', '/', '=' (per HTML spec).
_NAME = r'[^\s"\'>/=]+'
_START_TAG = re.compile(rf'<[^\s/>]+((?:\s+{_NAME}="[^"]*")*)')
_ATTRIBUTE = re.compile(rf'({_NAME})="([^"]*)"')


def extract_attributes(element: str) -> list[str]:
    """Extract attributes from the start tag of an HTML element.

    Assumes valid HTML with attributes in the format attribute="value". Only the
    start tag is scanned, so attribute-like text in the element's content is
    ignored. For production code, use the standard library's html.parser instead:
    it handles single-quoted, unquoted and boolean attributes and entity
    decoding, which a regex can't do reliably.

    Args:
        element: A string representing a single HTML element.

    Returns:
        A list of "attribute, value" strings in source order; an empty list if
        the element has no attributes.
    """
    start_tag = _START_TAG.match(element)
    if start_tag is None:
        return []
    return [f'{name}, {value}' for name, value in _ATTRIBUTE.findall(start_tag[1])]


tests: list[tuple[str, list[str]]] = [
    ('<span class="red"></span>', ['class, red']),
    ('<meta charset="UTF-8" />', ['charset, UTF-8']),
    ('<p>Lorem ipsum dolor sit amet</p>', []),
    (
        '<input name="email" type="email" required="true" />',
        ['name, email', 'type, email', 'required, true'],
    ),
    (
        '<button id="submit" class="btn btn-primary">Submit</button>',
        ['id, submit', 'class, btn btn-primary'],
    ),
]


@mark.parametrize('element, expected', tests)
def test_extract_attributes(element: str, expected: list[str]) -> None:
    """Test extract_attributes function."""
    assert extract_attributes(element) == expected


if __name__ == '__main__':
    element, expected = tests[0]
    print(extract_attributes(element))
