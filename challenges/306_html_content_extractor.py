# Daily Coding challenge #306 (2026-06-12) - freeCodeCamp.org
# HTML Content Extractor
# Given a string of HTML, return the plain text content with all tags removed.
from html.parser import HTMLParser

from pytest import mark


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.chunks: list[str] = []

    def handle_data(self, data: str) -> None:
        self.chunks.append(data)


def extract_content(html: str) -> str:
    extractor = _TextExtractor()
    extractor.feed(html)
    return ''.join(extractor.chunks)


tests = [
    ('<p>hello world</p>', 'hello world'),
    ('<p>hello <span>world</span></p>', 'hello world'),
    ('<a href="example.com">Click me</a>', 'Click me'),
    (
        '<p><button onClick="learnToCode()">Learn</button> to <code>code<code> <br/>'
        + 'for <strong>free</strong> <br/>on <a href="https://freecodecamp.org/" '
        + 'target="_blank"><span class="highlight">freecodecamp</span>.org</a>',
        'Learn to code for free on freecodecamp.org',
    ),
    (
        '<div class="container"><h1 id="title">Welcome to <strong>My</strong> Website.'
        + '</h1><p>This is a <a href="https://example.com" target="_blank">link</a> to '
        + 'something <em>really</em> <span class="highlight">important</span>.</p><ul>'
        + '<li>Item <strong>one</strong></li><li>Item <em>two</em></li><li>Item three'
        + '</li></ul><img src="pic.jpg" alt="A picture"/><p class="footer">Contact us '
        + 'at <a href="mailto:hello@example.com">hello@example.com</a> for <span>more '
        + '<strong>info</strong></span>.</p></div>',
        'Welcome to My Website.This is a link to something really important.Item '
        + 'oneItem twoItem threeContact us at hello@example.com for more info.',
    ),
]


@mark.parametrize('html, expected', tests)
def test_extract_content(html: str, expected: str) -> None:
    assert extract_content(html) == expected


if __name__ == '__main__':
    html, expected = tests[0]
    print(extract_content(html))
