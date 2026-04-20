# Daily Coding challenge #253 (2026-04-20) - freeCodeCamp.org
# Acronym Finder
# Given a string representing an acronym, return the full name of the organization it
# belongs to from the list below:

# "National Avocado Storage Authority"
# "Cats Infiltration Agency"
# "Fluffy Beanbag Inspectors"
# "Department Of Jelly"
# "Wild Honey Organization"
# "Eating Pancakes Administration"
# Each letter in the given acronym should match the first letter of each word in the
# organization it belongs to, in the same order.
from types import MappingProxyType

from pytest import mark

ORGANIZATIONS = (
    'National Avocado Storage Authority',
    'Cats Infiltration Agency',
    'Fluffy Beanbag Inspectors',
    'Department Of Jelly',
    'Wild Honey Organization',
    'Eating Pancakes Administration',
)


def _to_acronym(full_name: str) -> str:
    return ''.join(word[0] for word in full_name.split())


_ORG_BY_ACRONYM = MappingProxyType(
    {_to_acronym(full_name): full_name for full_name in ORGANIZATIONS}
)


def find_org(acronym: str) -> str:
    return _ORG_BY_ACRONYM[acronym]


tests = [
    ('NASA', 'National Avocado Storage Authority'),
    ('CIA', 'Cats Infiltration Agency'),
    ('FBI', 'Fluffy Beanbag Inspectors'),
    ('DOJ', 'Department Of Jelly'),
    ('WHO', 'Wild Honey Organization'),
    ('EPA', 'Eating Pancakes Administration'),
]


@mark.parametrize('acronym, expected', tests)
def test(acronym: str, expected: str) -> None:
    assert find_org(acronym) == expected


if __name__ == '__main__':
    acronym, expected = tests[0]
    print(find_org(acronym))
