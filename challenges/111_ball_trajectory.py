# Daily Coding challenge #111 (2025-11-29) - freeCodeCamp.org
# Ball Trajectory
# Today's challenge is inspired by the video game Pong, which was released
# November 29, 1972.

# Given a matrix (array of arrays) that includes the location of the ball (2), and
# the previous location of the ball (1), return the matrix indices for the next
# location of the ball.

# The ball always moves in a straight line.
# The movement direction is determined by how the ball moved from 1 to 2.
# The edges of the matrix are considered walls. If the balls hits a:
# top or bottom wall, it bounces by reversing its vertical direction.
# left or right wall, it bounces by reversing its horizontal direction.
# corner, it bounces by reversing both directions.


# from dataclasses import dataclass


# @dataclass
# class Coordinate:
#     x: int
#     y: int

#     def __sub__(self, other: Coordinate) -> tuple[int, int]:
#         return (self.x - other.x, self.y - other.y)


# @dataclass
# class Velocity:
#     x: int
#     y: int


# def get_next_location(matrix: list[list[int]]) -> list[int]:
#     n_cols = len(matrix[0])
#     n_rows = len(matrix)

#     start_coordinate = Coordinate(0, 0)
#     end_coordinate = Coordinate(0, 0)

#     for y, row in enumerate(matrix):
#         for x, column in enumerate(row):
#             if column == 1:
#                 start_coordinate = Coordinate(x, y)
#             if column == 2:
#                 end_coordinate = Coordinate(x, y)

#     velocity = Velocity(*end_coordinate - start_coordinate)

#     next_coordinate = Coordinate(0, 0)

#     # Horizontal movement
#     # Travels to the right
#     if velocity.x > 0:
#         if end_coordinate.x + velocity.x < n_cols:
#             # Proceed
#             next_coordinate.x = end_coordinate.x + velocity.x
#         else:
#             # Bounce
#             next_coordinate.x = (n_cols - 1) - (
#                 (n_cols - 1) - end_coordinate.x + velocity.x
#             )
#     # Travels to the left
#     elif velocity.x < 0:
#         if end_coordinate.x + velocity.x >= 0:
#             # Proceed
#             next_coordinate.x = end_coordinate.x + velocity.x
#         else:
#             # Bounce
#             next_coordinate.x = -1 * (end_coordinate.x + velocity.x)
#     else:
#         # No horizontal movement
#         next_coordinate.x = end_coordinate.x

#     # Vertical movement
#     # Travels upwards
#     if velocity.y < 0:
#         if end_coordinate.y + velocity.y >= 0:
#             # Proceed
#             next_coordinate.y = end_coordinate.y + velocity.y
#         else:
#             # Bounce
#             next_coordinate.y = -1 * (end_coordinate.y + velocity.y)
#     # Travels downwards
#     elif velocity.y > 0:
#         if end_coordinate.y + velocity.y < n_rows:
#             # Proceed
#             next_coordinate.y = end_coordinate.y + velocity.y
#         else:
#             # Bounce
#             next_coordinate.y = (n_rows - 1) - (
#                 (n_rows - 1) - end_coordinate.y + velocity.y
#             )

#     else:
#         next_coordinate.y = end_coordinate.y

#     return [next_coordinate.y, next_coordinate.x]
from dataclasses import dataclass

from pytest import mark


@dataclass
class Coordinate:
    x: int
    y: int

    def __sub__(self, other: Coordinate) -> Coordinate:
        return Coordinate(self.x - other.x, self.y - other.y)

    def __add__(self, other: Coordinate) -> Coordinate:
        return Coordinate(self.x + other.x, self.y + other.y)


def find_positions(matrix: list[list[int]]) -> tuple[Coordinate, Coordinate]:
    """Find the previous (1) and current (2) ball positions."""
    for y, row in enumerate(matrix):
        for x, val in enumerate(row):
            if val == 1:
                prev_pos = Coordinate(x, y)
            elif val == 2:
                curr_pos = Coordinate(x, y)
    return prev_pos, curr_pos


def calculate_next_position(pos: int, velocity: int, max_val: int) -> int:
    """Calculate next position along one axis with wall bounce logic."""
    next_pos = pos + velocity

    if 0 <= next_pos < max_val:
        return next_pos

    # Handle bounce
    if next_pos < 0:
        return -next_pos
    else:  # next_pos >= max_val
        return 2 * (max_val - 1) - next_pos


def get_next_location(matrix: list[list[int]]) -> list[int]:
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    prev_pos, curr_pos = find_positions(matrix)
    velocity = curr_pos - prev_pos

    next_x = calculate_next_position(curr_pos.x, velocity.x, n_cols)
    next_y = calculate_next_position(curr_pos.y, velocity.y, n_rows)

    return [next_y, next_x]


tests = [
    ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 2, 0], [0, 0, 0, 0]], [2, 3]),
    ([[0, 0, 0, 0], [0, 0, 1, 0], [0, 2, 0, 0], [0, 0, 0, 0]], [3, 0]),
    ([[0, 2, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [1, 2]),
    ([[0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 1, 0, 0]], [1, 1]),
    ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 2]], [2, 2]),
]


@mark.parametrize(('matrix', 'expected'), tests)
def test_get_next_location(matrix: list[list[int]], expected: list[int]) -> None:
    assert get_next_location(matrix) == expected


if __name__ == '__main__':
    matrix, expected = tests[0]
    print(get_next_location(matrix))
