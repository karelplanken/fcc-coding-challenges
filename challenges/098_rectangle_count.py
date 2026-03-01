# Daily Coding challenge #98 (2025-11-16) - freeCodeCamp.org
# Rectangle Count
# Given two positive integers representing the width and height of a rectangle,
# determine how many rectangles can fit in the given one.

# Only count rectangles with integer width and height.
# For example, given 1 and 3, return 6. Three 1x1 rectangles, two 1x2 rectangles,
# and one 1x3 rectangle.
from pytest import mark


def count_rectangles(width: int, height: int) -> int:
    return (width * (width + 1) // 2) * (height * (height + 1) // 2)


tests = [
    (1, 3, 6),
    (3, 2, 18),
    (1, 2, 3),
    (5, 4, 150),
    (11, 19, 12540),
]


@mark.parametrize('width, height, expected', tests)
def test_count_rectangle(width: int, height: int, expected: int) -> None:
    assert count_rectangles(width, height) == expected


if __name__ == '__main__':
    width, height, expected = tests[0]
    # print(count_rectangles(width, height))
    count_rectangles(width, height)
