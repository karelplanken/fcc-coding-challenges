# Daily Coding challenge #211 (2026-03-09) - freeCodeCamp.org
# Array Sum
# Given an array of numbers, return the sum of all the numbers.
from pytest import mark


def sum_array(numbers: list[int]) -> int:
    # Remark: sum([]) returns 0 gracefully
    return sum(numbers)


tests = [
    ([1, 2, 3, 4, 5], 15),
    ([42], 42),
    ([5, -2, 7, -3], 7),
    ([203, 145, -129, 6293, 523, -919, 845, 2434], 9395),
    ([0, 0], 0),
]


@mark.parametrize('numbers, expected', tests)
def test_sumarray(numbers: list[int], expected: int) -> None:
    assert sum_array(numbers) == expected


if __name__ == '__main__':
    numbers, expected = tests[0]
    print(sum_array(numbers))
