# Daily Coding challenge #226 (2026-03-24) - freeCodeCamp.org
# Passing Exam Count
# Given an array of student exam scores and the score needed to pass it, return the
# number of students that passed the exam.
from pytest import mark


def passing_count(scores: list[int], passing_score: int) -> int:
    return sum(score >= passing_score for score in scores)


tests = [
    ([90, 85, 75, 60, 50], 70, 3),
    ([100, 80, 75, 88, 72, 74, 79, 71, 60, 92], 75, 6),
    ([79, 60, 88, 72, 74, 59, 75, 71, 80, 92], 60, 9),
    ([76, 79, 80, 70, 71, 65, 79, 78, 59, 72], 85, 0),
    (
        [
            84,
            65,
            98,
            53,
            58,
            71,
            91,
            80,
            92,
            70,
            73,
            83,
            86,
            69,
            84,
            77,
            72,
            58,
            69,
            75,
            66,
            68,
            72,
            96,
            90,
            63,
            88,
            63,
            80,
            67,
        ],
        60,
        27,
    ),
]


@mark.parametrize('scores, passing_score, expected', tests)
def test_solution(scores: list[int], passing_score: int, expected: int) -> None:
    assert passing_count(scores, passing_score) == expected


if __name__ == '__main__':
    scores, passing_score, expected = tests[0]
    print(passing_count(scores, passing_score))
