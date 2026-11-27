Description of daily coding challenge number 111 (2025-11-29) from freeCodeCamp.org

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
