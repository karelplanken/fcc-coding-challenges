"""Daily Coding Challenge #94 (2025-11-12) - freeCodeCamp.org."""

# Email Signature Generator
# Given strings for a person's name, title, and company, return an email signature as a
# single string using the following rules:
#
# - The name should appear first, preceded by a prefix that depends on the first letter
#   of the name. For names starting with (case-insensitive):
#   - A-I: Use >> as the prefix.
#   - J-R: Use -- as the prefix.
#   - S-Z: Use :: as the prefix.
# - A comma and space (, ) should follow the name.
# - The title and company should follow the comma and space, separated by " at " (with
#   spaces around it).
#
# For example, given "Quinn Waverly", "Founder and CEO", and "TechCo" return "--Quinn
# Waverly, Founder and CEO at TechCo".
from string import ascii_lowercase

from pytest import mark


def generate_signature(name: str, title: str, company: str) -> str:
    """Generate an email signature based on the given name, title, and company.

    Args:
        name: The person's name.
        title: The person's title.
        company: The company the person works for.

    Returns:
        The email signature.

    Raises:
        ValueError: If the name is empty or does not start with an ASCII letter.
    """
    first_letter = name[:1].lower()
    if not first_letter or first_letter not in ascii_lowercase:
        msg = f'Name must start with an ASCII letter: {name!r}'
        raise ValueError(msg)

    if first_letter <= 'i':
        prefix = '>>'
    elif first_letter <= 'r':
        prefix = '--'
    else:
        prefix = '::'

    return f'{prefix}{name}, {title} at {company}'


tests = [
    (
        'Quinn Waverly',
        'Founder and CEO',
        'TechCo',
        '--Quinn Waverly, Founder and CEO at TechCo',
    ),
    ('Alice Reed', 'Engineer', 'TechCo', '>>Alice Reed, Engineer at TechCo'),
    (
        'Tina Vaughn',
        'Developer',
        'example.com',
        '::Tina Vaughn, Developer at example.com',
    ),
    ('B. B.', 'Product Tester', 'AcmeCorp', '>>B. B., Product Tester at AcmeCorp'),
    (
        'windstorm',
        'Cloud Architect',
        'Atmospheronics',
        '::windstorm, Cloud Architect at Atmospheronics',
    ),
]


@mark.parametrize(('name', 'title', 'company', 'expected'), tests)
def test_generate_signature(name: str, title: str, company: str, expected: str) -> None:
    """Test generate_signature function."""
    assert generate_signature(name, title, company) == expected


if __name__ == '__main__':
    name, title, company, expected = tests[0]
    print(generate_signature(name, title, company))
