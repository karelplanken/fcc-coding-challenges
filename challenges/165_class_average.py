# Daily Coding challenge #165 (2026-01-22) - freeCodeCamp.org
# Class Average
# Given an array of exam scores (numbers), return the average score in form of a letter
# grade according to the following chart:

# Average Score	Letter Grade
# 97-100	"A+"
# 93-96	"A"
# 90-92	"A−"
# 87-89	"B+"
# 83-86	"B"
# 80-82	"B-"
# 77-79	"C+"
# 73–76	"C"
# 70-72	"C-"
# 67-69	"D+"
# 63-66	"D"
# 60–62	"D-"
# below 60	"F"
# Calculate the average by adding all scores in the array and dividing by the total
# number of scores.

# # Initial solution using namedtuple for clarity
# from bisect import bisect_right
# from collections import namedtuple
# from operator import attrgetter

# from pytest import mark

# LetterGrade = namedtuple('LetterGrade', ['score', 'letter'])

# LETTER_GRADES = [
#     LetterGrade(0, 'F'),
#     LetterGrade(60, 'D-'),
#     LetterGrade(63, 'D'),
#     LetterGrade(67, 'D+'),
#     LetterGrade(70, 'C-'),
#     LetterGrade(73, 'C'),
#     LetterGrade(77, 'C+'),
#     LetterGrade(80, 'B-'),
#     LetterGrade(83, 'B'),
#     LetterGrade(87, 'B+'),
#     LetterGrade(90, 'A-'),
#     LetterGrade(93, 'A'),
#     LetterGrade(97, 'A+'),
# ]

# SCORE_GETTER = attrgetter('score')


# def get_average_grade(scores: list[int]) -> str:
#     avg_score = sum(scores) / len(scores)
#     return LETTER_GRADES[
#         bisect_right(LETTER_GRADES, avg_score, key=SCORE_GETTER) - 1
#     ].letter


# Alternative: even more readable with dataclass
from bisect import bisect_right  # Left-inclusive ranges are used
from dataclasses import dataclass
from operator import attrgetter

from pytest import mark


@dataclass(frozen=True)
class GradeThreshold:
    score: float
    letter: str


GRADE_SCALE = [
    GradeThreshold(0, 'F'),
    GradeThreshold(60, 'D-'),
    GradeThreshold(63, 'D'),
    GradeThreshold(67, 'D+'),
    GradeThreshold(70, 'C-'),
    GradeThreshold(73, 'C'),
    GradeThreshold(77, 'C+'),
    GradeThreshold(80, 'B-'),
    GradeThreshold(83, 'B'),
    GradeThreshold(87, 'B+'),
    GradeThreshold(90, 'A-'),
    GradeThreshold(93, 'A'),
    GradeThreshold(97, 'A+'),
]

SCORE_GETTER = attrgetter('score')

def get_average_grade(scores: list[int]) -> str:
    avg_score = sum(scores) / len(scores)
    idx = bisect_right(GRADE_SCALE, avg_score, key=SCORE_GETTER) - 1
    return GRADE_SCALE[idx].letter

tests = [
    ([92, 91, 90, 94, 89, 93], 'A-'),
    ([84, 89, 85, 100, 91, 88, 79], 'B+'),
    ([63, 69, 65, 66, 71, 64, 65], 'D'),
    ([97, 98, 99, 100, 96, 97, 98, 99, 100], 'A+'),
    ([75, 100, 88, 79, 80, 78, 64, 60], 'C+'),
    ([45, 48, 50, 52, 100, 54, 56, 58, 59], 'F'),
]


@mark.parametrize('scores, expected', tests)
def test_get_average_grade(scores: list[int], expected: str) -> None:
    assert get_average_grade(scores) == expected


if __name__ == '__main__':
    scores, expected = tests[0]
    print(get_average_grade(scores))
