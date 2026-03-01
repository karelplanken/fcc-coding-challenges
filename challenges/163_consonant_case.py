# Daily Coding challenge #163 (2026-01-20) - freeCodeCamp.org
# Consonant Case
# Given a string representing a variable name, convert it to consonant case using the
# following rules:

# All consonants should be converted to uppercase.
# All vowels (a, e, i, o, u in any case) should be converted to lowercase.
# All hyphens (-) should be converted to underscores (_).
from pytest import mark

VOWELS = frozenset({'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'})


def to_consonant_case(s: str) -> str:
    return ''.join(
        char.lower()
        if char in VOWELS
        else char.upper()
        if char.isalpha()
        else '_'
        if char == '-'
        else char
        for char in s
    )


tests = [
    ('helloworld', 'HeLLoWoRLD'),
    ('HELLOWORLD', 'HeLLoWoRLD'),
    ('_hElLO-WOrlD-', '_HeLLo_WoRLD_'),
    (
        '_~-generic_~-variable_~-name_~-here-~_',
        '_~_GeNeRiC_~_VaRiaBLe_~_NaMe_~_HeRe_~_',
    ),
]


@mark.parametrize('input_str, expected', tests)
def test_to_consonant_case(input_str: str, expected: str) -> None:
    assert to_consonant_case(input_str) == expected


if __name__ == '__main__':
    input_str, expected = tests[0]
    print(to_consonant_case(input_str))
