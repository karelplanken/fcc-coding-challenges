# Daily Coding challenge #298 (2026-06-04) - freeCodeCamp.org
# Schema Validator Part 4
# Given an object (JavaScript) or dictionary (Python), determine if it matches the
# following schema:
# Roles = "user" | "creator" | "moderator" | "staff" | "admin"
# {
#   username: string,
#   posts: number,
#   verified: boolean,
#   role: Roles,
#   supporter?: boolean
# }
# The pipe (|) symbol means "or". role must be one of the listed Roles values.
# The question mark (?) after supporter means that the field is optional, but is the
# specified type if it exists.
# Extra keys are allowed
from collections.abc import Callable, Mapping
from types import MappingProxyType

from pytest import mark

Schema = Mapping[str, object]

USERNAME = 'username'
ROLE = 'role'
ROLES = frozenset({'user', 'creator', 'moderator', 'staff', 'admin'})
POSTS = 'posts'
VERIFIED = 'verified'
SUPPORTER = 'supporter'


def valid_username(d: Schema) -> bool:
    return type(d.get(USERNAME)) is str


def valid_posts(d: Schema) -> bool:
    return type(d.get(POSTS)) is int


def valid_verified(d: Schema) -> bool:
    return type(d.get(VERIFIED)) is bool


def valid_role(d: Schema) -> bool:
    return type(d.get(ROLE)) is str and d[ROLE] in ROLES


def valid_supporter(d: Schema) -> bool:
    return SUPPORTER not in d or type(d[SUPPORTER]) is bool


RULES: MappingProxyType[str, Callable[[Schema], bool]] = MappingProxyType({
    USERNAME: valid_username,
    POSTS: valid_posts,
    VERIFIED: valid_verified,
    ROLE: valid_role,
    SUPPORTER: valid_supporter,
})


def is_valid_schema(obj: Schema) -> bool:
    return all(rule(obj) for rule in RULES.values())


tests = [
    (
        {
            'username': 'vivian',
            'posts': 1,
            'verified': False,
            'role': 'user',
            'supporter': True,
        },
        True,
    ),
    ({'username': 'rudolph', 'posts': 15, 'verified': True, 'role': 'creator'}, True),
    (
        {
            'username': 'hernandez',
            'posts': 35,
            'verified': True,
            'role': 'moderator',
            'supporter': False,
            'followers': 55,
        },
        True,
    ),
    (
        {
            'username': 'julia',
            'posts': 50,
            'verified': True,
            'role': 'admin',
            'supporter': 'true',
        },
        False,
    ),
    (
        {
            'username': 'bernard',
            'posts': 0,
            'verified': True,
            'role': 'friend',
            'supporter': True,
        },
        False,
    ),
    (
        {
            'username': 'felix',
            'posts': 40,
            'verified': 'yes',
            'role': 'staff',
            'supporter': False,
        },
        False,
    ),
    (
        {
            'username': 'jimmy',
            'posts': True,
            'verified': False,
            'role': 'creator',
            'supporter': True,
        },
        False,
    ),
    (
        {
            'username': True,
            'posts': 30,
            'verified': True,
            'role': 'moderator',
            'supporter': False,
        },
        False,
    ),
]


@mark.parametrize('obj, expected', tests)
def test_is_valid_schema(obj: Schema, expected: bool) -> None:
    assert is_valid_schema(obj) == expected


if __name__ == '__main__':
    obj, expected = tests[0]
    print(is_valid_schema(obj))
