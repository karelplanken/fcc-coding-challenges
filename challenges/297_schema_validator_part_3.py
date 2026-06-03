# Daily Coding challenge #297 (2026-06-03) - freeCodeCamp.org
# Schema Validator Part 3
# Given an object (JavaScript) or dictionary (Python), determine if it matches the
# following schema:
# Roles = "user" | "creator" | "moderator" | "staff" | "admin"
# {
#   username: string,
#   posts: number,
#   verified: boolean,
#   role: Roles
# }
# The pipe (|) symbol means "or". role must be one of the listed Roles values.
# Extra keys are allowed.
from collections.abc import Callable
from types import MappingProxyType

from pytest import mark

USERNAME = 'username'
ROLE = 'role'
ROLES = frozenset(('user', 'creator', 'moderator', 'staff', 'admin'))
POSTS = 'posts'
VERIFIED = 'verified'

RULES: MappingProxyType[str, Callable[[dict[str, object]], bool]] = MappingProxyType({
    USERNAME: lambda d: type(d.get(USERNAME)) is str,
    POSTS: lambda d: type(d.get(POSTS)) is int,
    VERIFIED: lambda d: type(d.get(VERIFIED)) is bool,
    ROLE: lambda d: type(d.get(ROLE)) is str and d.get(ROLE) in ROLES,
})


def is_valid_schema(obj: dict[str, object]) -> bool:
    return all(rule(obj) for rule in RULES.values())


tests: list[tuple[dict[str, object], bool]] = [
    ({'username': 'henry', 'posts': 0, 'verified': True, 'role': 'staff'}, True),
    (
        {
            'username': 'sara',
            'posts': 45,
            'verified': False,
            'role': 'creator',
            'followers': 70,
        },
        True,
    ),
    ({'username': 'penelope', 'posts': 20, 'verified': True, 'role': 'admin'}, True),
    ({'username': 'kevin', 'posts': 0, 'verified': False, 'role': 'user'}, True),
    ({'username': 'george', 'posts': 15, 'verified': True, 'role': 'moderator'}, True),
    ({'username': 'david', 'posts': 0, 'verified': False, 'role': 'guest'}, False),
    ({'username': 'wendy', 'posts': 10, 'verified': True}, False),
    ({'username': 'fabian', 'posts': 1, 'verified': True, 'role': True}, False),
    ({'username': 8, 'posts': 1, 'verified': True, 'role': 'user'}, False),
    ({'username': 'penny', 'posts': '10', 'verified': True, 'role': 'staff'}, False),
    ({'username': 'john', 'posts': '1', 'verified': 'true', 'role': 'admin'}, False),
]


@mark.parametrize('obj, expected', tests)
def test_is_valid_schema(obj: dict[str, object], expected: bool) -> None:
    assert is_valid_schema(obj) == expected


if __name__ == '__main__':
    obj, expected = tests[0]
    print(is_valid_schema(obj))
