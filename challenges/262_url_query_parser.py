# Daily Coding challenge #262 (2026-04-29) - freeCodeCamp.org
# URL Query Parser
# Given a URL that contains a query string, parse the query string into an object
# (or dictionary) of key-value pairs.
# The query string begins after the "?",
# each parameter is separated by "&",
# each key/value pair is separated by "="
# For example, given "https://example.com/search?name=Alice&age=30", return:
# {
#   "name": "Alice",
#   "age": "30"
# }
# All values should be returned as strings.
from pytest import mark


def parse_url_query(url: str) -> dict[str, str]:
    query_string = url[url.index('?') + 1 :]
    pairs = (param.split('=', maxsplit=1) for param in query_string.split('&'))
    return {key: value for key, value in pairs}


tests = [
    ('https://example.com/search?name=Alice&age=30', {'name': 'Alice', 'age': '30'}),
    (
        'https://freecodecamp.org/learn?skill=programming&language=python',
        {'skill': 'programming', 'language': 'python'},
    ),
    (
        'https://freecodecamp.org/items?category=books&sort=asc&page=2',
        {'category': 'books', 'sort': 'asc', 'page': '2'},
    ),
    (
        'https://example.com?redirect=freecodecamp.org/learn&when=now',
        {'redirect': 'freecodecamp.org/learn', 'when': 'now'},
    ),
]


@mark.parametrize('url, expected', tests)
def test_parse_url_query(url: str, expected: dict[str, str]) -> None:
    assert parse_url_query(url) == expected


if __name__ == '__main__':
    url, expected = tests[3]
    print(parse_url_query(url))
