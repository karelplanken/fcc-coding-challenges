# Daily Coding challenge #183 (2026-02-09) - freeCodeCamp.org
# 2026 Winter Games Day 4: Ski Jumping
# Given distance points, style points, a wind compensation value, and K-point bonus
# value, calculate your score for the ski jump and determine if you won a medal or not.

# Your score is calculated by summing the above four values.
# The current total scores of the other jumpers are:

# 165.5
# 172.0
# 158.0
# 180.0
# 169.5
# 175.0
# 162.0
# 170.0
# If your score is the best, return "Gold"
# If it's second best, return "Silver"
# If it's third best, return "Bronze"
# Otherwise, return "No Medal"
from bisect import bisect_left

from pytest import mark


def ski_jump_medal(
    distance_points: float, style_points: float, wind_comp: float, k_point_bonus: float
) -> str:
    OTHER_SCORES = [158.0, 162.0, 165.5, 169.5, 170.0, 172.0, 175.0, 180.0]

    my_score = distance_points + style_points + wind_comp + k_point_bonus

    # Count how many scores I beat
    scores_beaten = bisect_left(OTHER_SCORES, my_score)

    # My rank is: (total jumpers) - (scores I beat)
    my_rank = len(OTHER_SCORES) + 1 - scores_beaten

    match my_rank:
        case 1:
            return 'Gold'
        case 2:
            return 'Silver'
        case 3:
            return 'Bronze'
        case _:
            return 'No Medal'


tests = [
    (125.0, 58.0, 0.0, 6.0, 'Gold'),
    (119.0, 50.0, 1.0, 4.0, 'Bronze'),
    (122.0, 52.0, -1.0, 4.0, 'Silver'),
    (118.0, 50.5, -1.5, 4.0, 'No Medal'),
    (124.0, 50.5, 2.0, 5.0, 'Gold'),
    (119.0, 49.5, 0.0, 3.0, 'No Medal'),
]


@mark.parametrize(
    'distance_points, style_points, wind_comp, k_point_bonus, expected', tests
)
def test_solution(
    distance_points: float,
    style_points: float,
    wind_comp: float,
    k_point_bonus: float,
    expected: str,
) -> None:
    assert (
        ski_jump_medal(distance_points, style_points, wind_comp, k_point_bonus)
        == expected
    )


if __name__ == '__main__':
    distance_points, style_points, wind_comp, k_point_bonus, expected = tests[1]
    print(ski_jump_medal(distance_points, style_points, wind_comp, k_point_bonus))
