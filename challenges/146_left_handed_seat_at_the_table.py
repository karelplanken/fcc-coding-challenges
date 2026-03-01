# Daily Coding challenge #146 (2026-01-03) - freeCodeCamp.org
# Left-Handed Seat at the Table
# Given a 4x2 matrix (array of arrays) representing the seating arrangement for a meal,
# determine how many seats a left-handed person can sit at.

# A left-handed person cannot sit where a right-handed person would be in the seat to
# the immediate left of them.
# In the given matrix:

# An "R" is a seat occupied by a right-handed person.
# An "L" is a seat occupied by a left-handed person.
# An "U" is an unoccupied seat.
# Only unoccupied seats are available to sit at.
# The seats in the top row are facing "down", and the seats in the bottom row are
# facing "up" (like a table), so left and right are relative to the seat's orientation.
# Corner seats only have one seat next to them.
# For example, in the given matrix:

# [
#   ["U", "R", "U", "L"],
#   ["U", "R", "R", "R"]
# ]
# The top-left seat is cannot be sat in because there's a right-handed person to the
# left. The other two open seats can be sat in because there isn't a right-handed
# person to the left.
from pytest import mark


def find_left_handed_seats(table: list[list[str]]) -> int:
    top_row, bottom_row = table
    count = 0

    # Top row: faces down, left is at i-1
    for i, seat in enumerate(top_row):
        if seat == 'U' and (i == len(top_row) - 1 or top_row[i + 1] != 'R'):
            count += 1

    # Bottom row: faces up, left is at i+1
    for i, seat in enumerate(bottom_row):
        if seat == 'U' and (i == 0 or bottom_row[i - 1] != 'R'):
            count += 1

    return count


# Tricky solution with normalization of seats, so we can just check the next seat to
# the right, notice that bottom and top are chained in one list, this solution is not
# very readable
# def find_left_handed_seats(table: list[list[str]]) -> int:
#     bottom, top = table
#     normalized_seats = [*bottom, *reversed(top)]
#     left_handed_seats = 0
#     for i, seat in enumerate(normalized_seats):
#         if i == len(normalized_seats) - 1:
#             left_handed_seats += 1 if seat == 'U' else 0
#         elif seat == 'U' and normalized_seats[i + 1] != 'R':
#             left_handed_seats += 1

#     return left_handed_seats

tests = [
    ([['U', 'R', 'U', 'L'], ['U', 'R', 'R', 'R']], 2),
    ([['U', 'U', 'U', 'U'], ['U', 'U', 'U', 'U']], 8),
    ([['U', 'R', 'U', 'R'], ['L', 'R', 'R', 'U']], 0),
    ([['L', 'U', 'R', 'R'], ['L', 'U', 'R', 'R']], 1),
    ([['U', 'R', 'U', 'U'], ['U', 'U', 'L', 'U']], 5),
]


@mark.parametrize(('table', 'expected'), tests)
def test_find_left_handed_seats(table: list[list[str]], expected: int) -> None:
    assert find_left_handed_seats(table) == expected


if __name__ == '__main__':
    table, expected = tests[0]
    print(find_left_handed_seats(table))
