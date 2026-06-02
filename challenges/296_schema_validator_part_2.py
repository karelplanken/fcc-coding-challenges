# Daily Coding challenge #296 (2026-06-02) - freeCodeCamp.org
# Schema Validator Part 2
# Given an object (JavaScript) or dictionary (Python), determine if it matches the
# following schema:
# {
#   username: string,
#   posts: number,
#   verified: boolean
# }
# Extra keys are allowed
from collections.abc import Callable, Mapping
from types import MappingProxyType

from pytest import mark

USERNAME = 'username'
POSTS = 'posts'
VERIFIED = 'verified'

RULES: Mapping[str, Callable[[dict[str, object]], bool]] = MappingProxyType({
    USERNAME: lambda d: isinstance(d.get(USERNAME), str),
    POSTS: lambda d: (
        isinstance(d.get(POSTS), int) and not isinstance(d.get(POSTS), bool)
    ),
    VERIFIED: lambda d: isinstance(d.get(VERIFIED), bool),
})


def is_valid_schema(obj: dict[str, object]) -> bool:
    return all(rule(obj) for rule in RULES.values())


tests: list[tuple[dict[str, object], bool]] = [
    ({'username': 'alice', 'posts': 10, 'verified': False}, True),
    ({'username': 'carol', 'posts': 15, 'verified': True, 'followers': 25}, True),
    ({'username': 'frank', 'posts': '21', 'verified': True}, False),
    ({'username': 'sam', 'posts': 17, 'verified': 'false'}, False),
    ({'username': 'bill', 'verified': True}, False),
    ({'username': 'fred', 'verified': True}, False),
    ({'username': 5, 'posts': 10, 'verified': True}, False),
]


@mark.parametrize('obj, expected', tests)
def test_is_valid_schema(obj: dict[str, object], expected: bool) -> None:
    assert is_valid_schema(obj) == expected


if __name__ == '__main__':
    obj, expected = tests[0]
    print(is_valid_schema(obj))
