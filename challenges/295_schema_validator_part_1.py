# Daily Coding challenge #295 (2026-06-01) - freeCodeCamp.org
# Schema Validator Part 1
# Given an object (JavaScript) or dictionary (Python), determine if it matches the
# following schema:
# {
#   username: string
# }
# Extra keys are allowed
from pytest import mark

USERNAME = 'username'


def is_valid_schema(obj: dict[str, object]) -> bool:
    return isinstance(obj.get(USERNAME), str)


tests: list[tuple[dict[str, object], bool]] = [
    ({'username': 'bob'}, True),
    ({'username': 'jen', 'posts': 30}, True),
    ({'username': ''}, True),
    ({'username': 7}, False),
    ({'posts': 25}, False),
]


@mark.parametrize('obj, expected', tests)
def test_is_valid_schema(obj: dict[str, object], expected: bool) -> None:
    assert is_valid_schema(obj) == expected


if __name__ == '__main__':
    obj, expected = tests[0]
    print(is_valid_schema(obj))
