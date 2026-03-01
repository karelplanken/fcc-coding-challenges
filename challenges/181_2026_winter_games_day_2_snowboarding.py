# Daily Coding challenge #181 (2026-02-07) - freeCodeCamp.org
# 2026 Winter Games Day 2: Snowboarding
# Given a snowboarder's starting stance and a rotation in degrees, determine their
# landing stance.

# A snowboarder's stance is either "Regular" or "Goofy".
# Trick rotations are multiples of 90 degrees. Positive indicates clockwise rotation,
# and negative indicate counter-clockwise rotation.
# The landing stance flips every 180 degrees of rotation.
# For example, given "Regular" and 90, return "Regular". Given "Regular" and 180
# degrees, return "Goofy".
from pytest import mark


def get_landing_stance(start_stance: str, rotation: int) -> str:
    # Count how many 180° flips occurred
    flips = abs(rotation) // 180

    # Stance changes on odd number of flips
    if flips % 2 == 0:
        return start_stance

    # Flip the stance
    return 'Regular' if start_stance == 'Goofy' else 'Goofy'


tests = [
    ('Regular', 90, 'Regular'),
    ('Regular', 180, 'Goofy'),
    ('Goofy', -270, 'Regular'),
    ('Regular', 2340, 'Goofy'),
    ('Goofy', 2160, 'Goofy'),
    ('Goofy', -540, 'Regular'),
]


@mark.parametrize('start_stance, rotation, expected', tests)
def test_solution(start_stance: str, rotation: int, expected: str) -> None:
    assert get_landing_stance(start_stance, rotation) == expected


if __name__ == '__main__':
    start_stance, rotation, expected = tests[1]
    print(get_landing_stance(start_stance, rotation))
