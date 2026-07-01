# Daily Coding challenge #309 (2026-06-15) - freeCodeCamp.org
# Number Sort
# Given a string of numbers separated by commas, return an array of the numbers sorted
# from smallest to largest.
from pytest import mark


def sort_numbers(s: str) -> list[int]:
    return sorted(map(int, s.split(',')))


tests = [
    ('3,1,2', [1, 2, 3]),
    ('5,3,8,1,9,2', [1, 2, 3, 5, 8, 9]),
    ('12,61,49,80,19,50,77,38', [12, 19, 38, 49, 50, 61, 77, 80]),
    ('0,6,-19,44,-2,7,0', [-19, -2, 0, 0, 6, 7, 44]),
]


@mark.parametrize('s, expected', tests)
def test_sort_numbers(s: str, expected: list[int]) -> None:
    assert sort_numbers(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(sort_numbers(s))
