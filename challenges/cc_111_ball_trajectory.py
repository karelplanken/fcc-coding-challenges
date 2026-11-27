"""Daily Coding Challenge #111 (2025-11-29) - freeCodeCamp.org."""

# Ball Trajectory
# Today's challenge is inspired by the video game Pong, which was released November 29,
# 1972.
#
# Given a matrix (array of arrays) that includes the location of the ball (2), and the
# previous location of the ball (1), return the matrix indices for the next location of
# the ball.
#
# - The ball always moves in a straight line.
# - The movement direction is determined by how the ball moved from 1 to 2.
# - The edges of the matrix are considered walls. If the ball hits a:
#   - top or bottom wall, it bounces by reversing its vertical direction.
#   - left or right wall, it bounces by reversing its horizontal direction.
#   - corner, it bounces by reversing both directions.
from dataclasses import dataclass

from pytest import mark


@dataclass
class Coordinate:
    """Class to represent a coordinate in the matrix."""

    x: int
    y: int

    def __sub__(self, other: Coordinate) -> Coordinate:
        """Subtract two coordinates to get the velocity vector.

        Args:
            other: The other coordinate to subtract from this one.

        Returns:
            A new Coordinate representing the difference (velocity) between the two.
        """
        return Coordinate(self.x - other.x, self.y - other.y)

    def __add__(self, other: Coordinate) -> Coordinate:
        """Add two coordinates to get the next position.

        Args:
            other: The other coordinate to add to this one.

        Returns:
            A new Coordinate representing the sum of the two coordinates.
        """
        return Coordinate(self.x + other.x, self.y + other.y)


def _find_positions(matrix: list[list[int]]) -> tuple[Coordinate, Coordinate]:
    """Find the previous (1) and current (2) ball positions.

    Args:
        matrix: The game area.

    Returns:
        Tuple containing the previous and current ball positions.

    Raises:
        ValueError: If the matrix does not contain both 1 and 2.
    """
    prev_pos = curr_pos = None

    for y, row in enumerate(matrix):
        for x, val in enumerate(row):
            if val == 1:
                prev_pos = Coordinate(x, y)
            elif val == 2:
                curr_pos = Coordinate(x, y)

    if not (prev_pos and curr_pos):
        msg = 'Matrix must contain both 1 (previous position) and 2 (current position).'
        raise ValueError(msg)

    return prev_pos, curr_pos


def _calculate_next_position(pos: int, velocity: int, max_val: int) -> int:
    """Calculate the next position of the ball, considering bounces.

    Args:
        pos: Current position of the ball (x or y coordinate).
        velocity: The velocity of the ball (change in position).
        max_val: The maximum value for the position (width or height of the matrix).

    Returns:
        The next position of the ball after considering bounces.
    """
    next_pos = pos + velocity

    if 0 <= next_pos < max_val:
        return next_pos

    # Handle bounce
    if next_pos < 0:
        return -next_pos
    else:  # next_pos >= max_val
        return 2 * (max_val - 1) - next_pos


def get_next_location(matrix: list[list[int]]) -> list[int]:
    """Get the next location of the ball in the matrix.

    Args:
        matrix: The game area.

    Returns:
        The next y and x coordinates of the ball.
    """
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    prev_pos, curr_pos = _find_positions(matrix)
    velocity = curr_pos - prev_pos

    next_x = _calculate_next_position(curr_pos.x, velocity.x, n_cols)
    next_y = _calculate_next_position(curr_pos.y, velocity.y, n_rows)

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
    """Test get_next_location function."""
    assert get_next_location(matrix) == expected


if __name__ == '__main__':
    matrix, expected = tests[0]
    print(get_next_location(matrix))
