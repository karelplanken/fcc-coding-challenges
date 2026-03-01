# Daily Coding challenge #51 (2025-09-30) - freeCodeCamp.org
# Phone Number Formatter
# Given a string of eleven digits, return the string as a phone number in
# this format: "+D (DDD) DDD-DDDD".
from pytest import mark


def format_number(number: str) -> str:
    return f'+{number[0]} ({number[1:4]}) {number[4:7]}-{number[7:]}'


tests = [
    ('05552340182', '+0 (555) 234-0182'),
    ('15554354792', '+1 (555) 435-4792'),
]


@mark.parametrize('number, expected', tests)
def test_format_number(number: str, expected: str) -> None:
    assert format_number(number) == expected


if __name__ == '__main__':
    number, expected = tests[0]
    print(format_number(number))
