# Daily Coding challenge #299 (2026-06-05) - freeCodeCamp.org
# Schema Validator Part 5
# Given an object (JavaScript) or dictionary (Python), determine if it matches the
# following schema:
# Roles = "user" | "creator" | "moderator" | "staff" | "admin"
# {
#   username: string,
#   posts: number,
#   verified: boolean,
#   role: Roles,
#   supporter?: boolean,
#   badges: string[]
# }
# The pipe (|) symbol means "or". role must be one of the listed Roles values.
# The question mark (?) after supporter means that the field is optional, but is the
# specified type if it exists.
# The brackets [] after string means that badges should be an array of strings
# (or empty).
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
BADGES = 'badges'


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


def valid_badges(d: Schema) -> bool:
    return type(badges := d.get(BADGES)) is list and all(
        type(badge) is str for badge in badges
    )


RULES: MappingProxyType[str, Callable[[Schema], bool]] = MappingProxyType({
    USERNAME: valid_username,
    POSTS: valid_posts,
    VERIFIED: valid_verified,
    ROLE: valid_role,
    SUPPORTER: valid_supporter,
    BADGES: valid_badges,
})


def is_valid_schema(obj: Schema) -> bool:
    return all(rule(obj) for rule in RULES.values())


tests = [
    (
        {
            'username': 'gill',
            'posts': 12,
            'verified': False,
            'role': 'creator',
            'supporter': False,
            'badges': ['early-adopter', 'popular'],
        },
        True,
    ),
    (
        {
            'username': 'tonya',
            'posts': 299,
            'verified': True,
            'role': 'moderator',
            'supporter': True,
            'badges': ['streak-master', 'veteran'],
            'followers': 1233,
        },
        True,
    ),
    (
        {
            'username': 'zara',
            'posts': 0,
            'verified': False,
            'role': 'user',
            'supporter': False,
            'badges': [],
        },
        True,
    ),
    (
        {
            'username': 'nicole',
            'posts': 65,
            'verified': True,
            'role': 'admin',
            'supporter': False,
            'badges': ['first-post', 18],
        },
        False,
    ),
    (
        {
            'username': 'tim',
            'posts': 25,
            'verified': True,
            'role': 'staff',
            'supporter': False,
        },
        False,
    ),
    (
        {
            'username': 'charlie',
            'posts': 0,
            'verified': False,
            'role': 'user',
            'supporter': 'no',
            'badges': ['first-post', 'anniversary'],
        },
        False,
    ),
    (
        {
            'username': 'wanda',
            'posts': 15,
            'verified': True,
            'role': 'friend',
            'supporter': True,
            'badges': ['popular'],
        },
        False,
    ),
    (
        {
            'username': 'guy',
            'posts': 5,
            'verified': 'false',
            'role': 'staff',
            'supporter': True,
            'badges': ['helper'],
        },
        False,
    ),
    (
        {
            'username': 'carrie',
            'verified': True,
            'role': 'moderator',
            'supporter': True,
            'badges': ['helper', 'sharer'],
        },
        False,
    ),
    (
        {
            'username': True,
            'posts': 75,
            'verified': True,
            'role': 'creator',
            'supporter': True,
            'badges': ['veteran'],
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
