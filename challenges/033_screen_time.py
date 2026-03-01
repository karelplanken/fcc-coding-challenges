# Daily Coding challenge #33 (2025-09-12) - freeCodeCamp.org
# Screen Time
# Given an input array of seven integers, representing a week's time, where each
# integer is the amount of hours spent on your phone that day, determine if it is too
# much screen time based on these constraints:

# If any single day has 10 hours or more, it's too much.
# If the average of any three days in a row is greater than or equal to 8 hours, it’s
# too much.
# If the average of the seven days is greater than or equal to 6 hours, it's too much.
from pytest import mark


def too_much_screen_time(hours: list[int]) -> bool:
    return (
        max(hours) >= 10
        or sum(hours) / 7 >= 6
        or any(sum(hours[i : i + 3]) >= 24 for i in range(5))
    )


tests = [
    ([1, 2, 3, 4, 5, 6, 7], False),
    ([7, 8, 8, 4, 2, 2, 3], False),
    ([5, 6, 6, 6, 6, 6, 6], False),
    ([1, 2, 3, 11, 1, 3, 4], True),
    ([1, 2, 3, 10, 2, 1, 0], True),
    ([3, 3, 5, 8, 8, 9, 4], True),
    ([3, 9, 4, 8, 5, 7, 6], True),
]


@mark.parametrize('hours, expected', tests)
def test_too_much_screen_time(hours: list[int], expected: bool) -> None:
    assert too_much_screen_time(hours) == expected


if __name__ == '__main__':
    hours, expected = tests[0]
    print(too_much_screen_time(hours))
