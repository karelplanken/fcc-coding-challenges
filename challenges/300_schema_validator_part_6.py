# Daily Coding challenge #300 (2026-06-06) - freeCodeCamp.org
# Schema Validator Part 6
# Given an object (JavaScript) or dictionary (Python), determine if it matches the
# following schema:
# Roles = "user" | "creator" | "moderator" | "staff" | "admin"
# UserProfile = {
#   username: string,
#   posts: number,
#   verified: boolean,
#   role: Roles,
#   supporter?: boolean,
#   badges: string[]
# }
# {
#   users: UserProfile[]
# }
# The pipe (|) symbol means "or". role must be one of the listed Roles values.
# The question mark (?) after supporter means that the field is optional, but is the
# specified type if it exists.
# UserProfile[] denotes an array of UserProfile objects. An empty array is valid.
# Extra keys are allowed
from collections.abc import Callable, Mapping
from types import MappingProxyType
from typing import Any

from pytest import mark

UserProfile = Mapping[str, object]

USERS = 'users'
USERNAME = 'username'
ROLE = 'role'
ROLES = frozenset({'user', 'creator', 'moderator', 'staff', 'admin'})
POSTS = 'posts'
VERIFIED = 'verified'
SUPPORTER = 'supporter'
BADGES = 'badges'


def valid_userprofiles(user_profiles: list[UserProfile]) -> bool:
    return all(
        type(user_profile) is dict for user_profile in user_profiles
    )


def valid_username(d: UserProfile) -> bool:
    return type(d.get(USERNAME)) is str


def valid_posts(d: UserProfile) -> bool:
    return type(d.get(POSTS)) is int


def valid_verified(d: UserProfile) -> bool:
    return type(d.get(VERIFIED)) is bool


def valid_role(d: UserProfile) -> bool:
    return type(d.get(ROLE)) is str and d[ROLE] in ROLES


def valid_supporter(d: UserProfile) -> bool:
    return SUPPORTER not in d or type(d[SUPPORTER]) is bool


def valid_badges(d: UserProfile) -> bool:
    return type(badges := d.get(BADGES)) is list and all(
        type(badge) is str for badge in badges
    )


RULES: MappingProxyType[str, Callable[[UserProfile], bool]] = MappingProxyType({
    USERNAME: valid_username,
    POSTS: valid_posts,
    VERIFIED: valid_verified,
    ROLE: valid_role,
    SUPPORTER: valid_supporter,
    BADGES: valid_badges,
})


def is_valid_schema(obj: dict[str, list[UserProfile]]) -> bool:
    user_profiles = obj.get(USERS)
    if not isinstance(user_profiles, list):
        return False
    return valid_userprofiles(user_profiles) and all(
        rule(user_profile) for user_profile in user_profiles for rule in RULES.values()
    )


tests: list[tuple[dict[str, list[UserProfile] | Any], bool]] = [
    (
        {
            'users': [
                {
                    'username': 'ron',
                    'posts': 14,
                    'verified': True,
                    'role': 'creator',
                    'badges': ['early-adopter'],
                },
                {
                    'username': 'cher',
                    'posts': 25,
                    'verified': True,
                    'role': 'moderator',
                    'supporter': True,
                    'followers': 20,
                    'badges': ['helper'],
                },
            ]
        },
        True,
    ),
    ({'users': []}, True),
    (
        {
            'users': {
                'username': 'anne',
                'posts': 0,
                'verified': False,
                'role': 'user',
                'supporter': False,
                'badges': [],
            }
        },
        False,
    ),
    (
        {
            'users': [
                {
                    'username': 'tony',
                    'posts': 10,
                    'verified': True,
                    'role': 'creator',
                    'supporter': True,
                    'badges': ['liked', 6],
                }
            ]
        },
        False,
    ),
    (
        {
            'users': [
                {
                    'username': 'ursula',
                    'posts': 3,
                    'verified': False,
                    'role': 'user',
                    'supporter': 'false',
                    'badges': ['comeback'],
                }
            ]
        },
        False,
    ),
    (
        {
            'users': [
                {
                    'username': 'benny',
                    'posts': 55,
                    'verified': True,
                    'role': 'superstar',
                    'supporter': True,
                    'badges': ['veteran'],
                }
            ]
        },
        False,
    ),
    (
        {
            'users': [
                {
                    'username': 'chase',
                    'posts': 1,
                    'verified': 'yes',
                    'role': 'staff',
                    'supporter': False,
                    'badges': ['superstar'],
                }
            ]
        },
        False,
    ),
    (
        {
            'users': [
                {
                    'username': 'carla',
                    'posts': '10',
                    'verified': False,
                    'role': 'user',
                    'supporter': False,
                    'badges': ['newbie'],
                }
            ]
        },
        False,
    ),
    (
        {
            'users': [
                {
                    'posts': 4,
                    'verified': False,
                    'role': 'admin',
                    'supporter': False,
                    'badges': ['superuser', 'veteran'],
                }
            ]
        },
        False,
    ),
    (
        {
            'users': [
                {
                    'username': 'harold',
                    'posts': 80,
                    'verified': True,
                    'role': 'creator',
                    'supporter': True,
                    'badges': ['liked', 'hero'],
                },
                {
                    'username': 'kim',
                    'posts': 11,
                    'verified': False,
                    'role': 'admin',
                    'supporter': True,
                    'badges': ['first'],
                },
                {},
            ]
        },
        False,
    ),
]


@mark.parametrize('obj, expected', tests)
def test_is_valid_schema(obj: dict[str, list[UserProfile]], expected: bool) -> None:
    assert is_valid_schema(obj) == expected


if __name__ == '__main__':
    obj, expected = tests[3]
    print(is_valid_schema(obj), expected)
