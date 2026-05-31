# Daily Coding challenge #286 (2026-05-23) - freeCodeCamp.org
# Open Issues
# Given an array of issue numbers and another array of pull request (PR) numbers,
# return an array of issues that remain open after all PRs have been merged.
# A PR closes an issue if their digits are a rotation of each other. For example, issue
# 123 would be closed by PR 231 or 312.
# A PR does not close an issue with the exact same number. For example, PR 123 does not
# close issue 123. So an issue with all the same number can't get closed.
# Either number may have leading zeros stripped. For example, PR 201 would close issue
# 12 (012, a rotation of 201). Similarily, issue 201 would be closed by PR 12.
# Return the remaining open issues in the order they were given.
from pytest import mark


def get_rotations(n: int, max_len: int) -> set[int]:
    s = str(n)
    rotations = set()
    for extra_zeros in range(max_len - len(s) + 1):
        padded = s + '0' * extra_zeros
        for i in range(len(padded)):
            rotation = padded[i:] + padded[:i]
            rotation = rotation.lstrip('0') or '0'
            if rotation != s:
                rotations.add(int(rotation))
    return rotations


def get_open_issues(issues: list[int], prs: list[int]) -> list[int]:
    max_len = max(len(str(n)) for n in issues + prs)
    prs_set = set(prs)

    return [
        issue for issue in issues if get_rotations(issue, max_len).isdisjoint(prs_set)
    ]


tests = [
    ([123, 234], [231], [234]),
    ([123, 345, 16], [345, 231], [345, 16]),
    ([456, 332, 12, 15], [201, 945, 180], [456, 332, 15]),
    ([12, 115, 296, 170, 24], [17, 18, 19, 20, 21], [115, 296, 24]),
    (
        [19, 95, 422, 395, 754, 102, 296, 709, 237, 4400, 1802],
        [395, 440, 9001, 95, 242, 21, 287, 169, 14],
        [95, 395, 754, 296, 709, 237, 1802],
    ),
]


@mark.parametrize('issues, prs, expected', tests)
def test_get_open_issues(
    issues: list[int], prs: list[int], expected: list[int]
) -> None:
    assert get_open_issues(issues, prs) == expected


if __name__ == '__main__':
    issues, prs, expected = tests[4]
    print(get_open_issues(issues, prs))
