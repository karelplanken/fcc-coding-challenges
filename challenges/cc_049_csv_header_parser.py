"""Daily Coding Challenge #49 (2025-09-28) - freeCodeCamp.org."""

# CSV Header Parser
# Given the first line of a comma-separated values (CSV) file, return an array
# containing the headings.
#
# - The first line of a CSV file contains headings separated by commas.
# - Remove any leading or trailing whitespace from each heading.
from pytest import mark


def get_headings(csv: str) -> list[str]:
    """Split the first line of a CSV file into whitespace-trimmed headings.

    Note that this function splits on every comma, so quoted fields such as
    '"city, country"' are not supported. The standard-library ``csv`` module handles
    quoting, embedded commas and escaped quotes, and would be more robust. However, the
    challenge only asks for comma splitting, and its parameter name ``csv`` shadows
    that module inside the function.

    Args:
        csv: The first line of a CSV file.

    Returns:
        The headings, in order, with surrounding whitespace removed.
        An empty list if the line is empty or contains only whitespace.
    """
    if not csv.strip():
        return []
    return [heading.strip() for heading in csv.split(',')]


tests = [
    ('name,age,city', ['name', 'age', 'city']),
    ('first name,last name,phone', ['first name', 'last name', 'phone']),
    ('username , email , signup date ', ['username', 'email', 'signup date']),
]


@mark.parametrize('csv, expected', tests)
def test_get_headings(csv: str, expected: list[str]) -> None:
    """Test get_headings function."""
    assert get_headings(csv) == expected


if __name__ == '__main__':
    csv, expected = tests[0]
    print(get_headings(csv))
