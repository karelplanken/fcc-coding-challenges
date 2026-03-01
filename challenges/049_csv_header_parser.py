# Daily Coding challenge #49 (2025-09-28) - freeCodeCamp.org
# CSV Header Parser
# Given the first line of a comma-separated values (CSV) file, return an array
# containing the headings.

# The first line of a CSV file contains headings separated by commas.
# Remove any leading or trailing whitespace from each heading.
from pytest import mark


def get_headings(csv: str) -> list[str]:
    return [header.strip() for header in csv.split(',')]
    # Slightly slower than list comprehension, has list() conversion overhead
    # return list(map(str.strip, csv.split(',')))


tests = [
    ('name,age,city', ['name', 'age', 'city']),
    ('first name,last name,phone', ['first name', 'last name', 'phone']),
    ('username , email , signup date ', ['username', 'email', 'signup date']),
]


@mark.parametrize('csv, expected', tests)
def test_get_headings(csv: str, expected: list[str]) -> None:
    assert get_headings(csv) == expected


if __name__ == '__main__':
    csv, expected = tests[0]
    print(get_headings(csv))
