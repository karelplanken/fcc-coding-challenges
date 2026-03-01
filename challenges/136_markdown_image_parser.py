# Daily Coding challenge #136 (2025-12-24) - freeCodeCamp.org
# Markdown Image Parser
# Given a string of an image in Markdown, return the equivalent HTML string.

# A Markdown image has the following format: "![alt text](image_url)". Where:
# alt text is the description of the image (the alt attribute value).
# image_url is the source URL of the image (the src attribute value).
# Return a string of the HTML img tag with the src set to the image URL and the alt set
# to the alt text.

# For example, given "![Cute cat](cat.png)" return '<img src="cat.png" alt="Cute cat">';

# Make sure the tag, order of attributes, spacing, and quote usage is the same as above.
# Note: The console may not display HTML tags in strings when logging messages — check
# the browser console to see logs with tags included.
import re

from pytest import mark


def parse_image(markdown: str) -> str:
    print(re.findall(r'(?<=\[).+?(?=\])|(?<=\().+?(?=\))', markdown))
    alt_text, source_url = re.findall(r'(?<=\[).+(?=\])|(?<=\().+(?=\))', markdown)
    return f'<img src="{source_url}" alt="{alt_text}">'


tests = [
    ('![Cute cat](cat.png)', '<img src="cat.png" alt="Cute cat">'),
    (
        '![Rocket Ship](https://freecodecamp.org/cdn/rocket-ship.jpg)',
        '<img src="https://freecodecamp.org/cdn/rocket-ship.jpg" alt="Rocket Ship">',
    ),
    (
        '![Cute cats!](https://freecodecamp.org/cats.jpeg)',
        '<img src="https://freecodecamp.org/cats.jpeg" alt="Cute cats!">',
    ),
]


@mark.parametrize('markdown, expected', tests)
def test_parse_image(markdown: str, expected: str) -> None:
    assert parse_image(markdown) == expected


if __name__ == '__main__':
    markdown, expected = tests[2]
    print(parse_image(markdown))
