# Daily Coding challenge #285 (2026-05-22) - freeCodeCamp.org
# Meeting Time
# Given a 3D array representing availability windows for multiple people, return the
# earliest time where everyone has one hour free. If no such time exists, return "None".
# Each person's availability is an array of [start, end] integer pairs in 24-hour time.
# For example, [10, 12] would mean the person is available from 10 to 12. Start times
# range from 0-23, and end times range from 1-24.
# For example, given:
# [
#   [[10, 12], [15, 16]], // person 1
#   [[11, 14], [15, 16]]  // person 2
# ]
# Return 11, the start of their first shared free hour.
from pytest import mark


def get_meeting_time(availability: list[list[list[int]]]) -> int | str:
    persons_hours = [
        set(hour for start, end in windows for hour in range(start, end))
        for windows in availability
    ]
    common_hours = persons_hours[0].intersection(*persons_hours[1:])
    return min(common_hours, default='None')


tests = [
    ([[[10, 12], [15, 16]], [[11, 14], [15, 16]]], 11),
    ([[[9, 10], [12, 15]], [[10, 11], [13, 14]], [[9, 11], [10, 14]]], 13),
    ([[[7, 8], [9, 11], [12, 14], [15, 16]], [[8, 11], [12, 13], [14, 15]]], 9),
    (
        [
            [[7, 8], [10, 12], [13, 15]],
            [[8, 11], [12, 13], [14, 15]],
            [[6, 7], [8, 9], [12, 13]],
        ],
        'None',
    ),
    (
        [
            [[1, 3], [4, 6], [8, 10], [20, 23]],
            [[15, 16], [17, 18], [19, 22], [23, 24]],
            [[14, 16], [17, 23]],
            [[2, 4], [5, 6], [18, 19], [21, 22], [23, 24]],
        ],
        21,
    ),
]


@mark.parametrize('availability, expected', tests)
def test_get_meeting_time(
    availability: list[list[list[int]]], expected: int | str
) -> None:
    assert get_meeting_time(availability) == expected


if __name__ == '__main__':
    availability, expected = tests[3]
    print(get_meeting_time(availability))
