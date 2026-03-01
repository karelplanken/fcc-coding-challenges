# Daily Coding challenge #172 (2026-01-29) - freeCodeCamp.org
# Letters-Numbers
# Given a string containing only letters and numbers, return a new string where a hyphen
# (-) is inserted every time the string switches from a letter to a number, or a number
# to a letter.
from pytest import mark


def separate_letters_and_numbers(s: str) -> str:
    if not s:
        return s

    def get_separator(prev: str, curr: str) -> str:
        is_transition = (prev.isdigit() and curr.isalpha()) or (
            prev.isalpha() and curr.isdigit()
        )
        return '-' if is_transition else ''

    return s[0] + ''.join(
        get_separator(s[i - 1], s[i]) + s[i] for i in range(1, len(s))
    )


# def separate_letters_and_numbers(s: str) -> str:
#     return s[0] + ''.join(
#         [
#             '-' + s[i]
#             if (s[i].isdigit() and s[i - 1].isalpha())
#             or (s[i].isalpha() and s[i - 1].isdigit())
#             else s[i]
#             for i in range(1, len(s))
#         ]
#     )


tests = [
    ('ABC123', 'ABC-123'),
    ('Route66', 'Route-66'),
    ('H3LL0W0RLD', 'H-3-LL-0-W-0-RLD'),
    ('a1b2c3d4', 'a-1-b-2-c-3-d-4'),
]


@mark.parametrize('s, expected', tests)
def test_separate_letters_and_numbers(s: str, expected: str) -> None:
    assert separate_letters_and_numbers(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(separate_letters_and_numbers(s))
