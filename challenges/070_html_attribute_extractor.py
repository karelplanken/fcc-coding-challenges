# Daily Coding challenge #70 (2025-10-19) - freeCodeCamp.org
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


def extract_attributes(element: str) -> list[str]:
    pattern = r'(\w+)="([^"]*)"'
    matches = re.findall(pattern, element)

    return [f'{attribute}, {value}' for attribute, value in matches]


tests = [
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
def test(element: str, expected: list[str]) -> None:
    assert extract_attributes(element) == expected


if __name__ == '__main__':
    element, expected = tests[2]
    print(extract_attributes(element))
