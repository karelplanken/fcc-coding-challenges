# Daily Coding challenge #327 (2026-07-03) - freeCodeCamp.org
# Database Migration
# Given two database objects, return the second object with any missing properties from
# the first filled in.
#
# - Fields that already exist in the record should not be overwritten.
from typing import TypedDict, cast

from pytest import mark


class UserRecord(TypedDict, total=False):
    username: str
    email: str
    posts: int
    verified: bool
    role: str
    banned: bool


def migrate_record(schema: UserRecord, record: UserRecord) -> UserRecord:
    # record spread last so its keys win on collision (last-write-wins);
    # key order in the result doesn't matter since dict equality ignores it
    return cast(UserRecord, {**schema, **record})


tests: list[tuple[UserRecord, UserRecord, UserRecord]] = [
    (
        {'username': '', 'posts': 0},
        {'verified': True},
        {'username': '', 'posts': 0, 'verified': True},
    ),
    (
        {'username': '', 'posts': 0},
        {'username': 'camper', 'posts': 5},
        {'username': 'camper', 'posts': 5},
    ),
    (
        {'username': '', 'posts': 0, 'verified': False},
        {'username': 'camper'},
        {'username': 'camper', 'posts': 0, 'verified': False},
    ),
    (
        {'username': '', 'posts': 0},
        {'username': 'camper', 'role': 'admin'},
        {'username': 'camper', 'role': 'admin', 'posts': 0},
    ),
    (
        {
            'username': '',
            'email': '',
            'posts': 0,
            'verified': False,
            'role': 'user',
            'banned': False,
        },
        {'username': 'camper', 'email': 'camper@freecodecamp.org', 'role': 'admin'},
        {
            'username': 'camper',
            'email': 'camper@freecodecamp.org',
            'role': 'admin',
            'posts': 0,
            'verified': False,
            'banned': False,
        },
    ),
]


@mark.parametrize('schema, record, expected', tests)
def test_migrate_record(
    schema: UserRecord, record: UserRecord, expected: UserRecord
) -> None:
    assert migrate_record(schema, record) == expected


if __name__ == '__main__':
    schema, record, expected = tests[0]
    print(migrate_record(schema, record))
