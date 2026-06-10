# Daily Coding challenge #304 (2026-06-10) - freeCodeCamp.org
# Itinerary Arrangements
# Given an array of at least two optional stops for a day trip, return the number of
# valid itinerary arrangements.

# The itinerary always includes "breakfast", "lunch", and "dinner", these will not be
# passed in as arguments. The optional stops can be placed anywhere in the itinerary,
# subject to the following rules:

# "breakfast" is always first, with at least one stop before "lunch".
# "lunch" must appear before "dinner", with at least one stop in between.
# At most, one optional stop may appear after "dinner".
# Return the number of valid arrangements.
# Solution 1: Closed-form formula
#
# A valid itinerary has the shape:
#   [breakfast]
#   [slot A: >=1 stop]
#   [lunch]
#   [slot B: >=1 stop]
#   [dinner]
#   [slot C: 0 or 1 stop]
#
# For any split (a, b, c) of n stops across slots A, B, C, the number of ordered
# arrangements is always n! — the multinomial coefficient (n! / a!b!c!) times the
# per-slot orderings (a! * b! * c!) cancel exactly to n!.
#
# So the answer is n! * (number of valid splits).
#
# Valid splits: a + b + c = n, a >= 1, b >= 1, c in {0, 1}
#   c = 0: a + b = n,     a >= 1, b >= 1  ->  n-1 solutions
#   c = 1: a + b = n-1,   a >= 1, b >= 1  ->  n-2 solutions
#   total: (n-1) + (n-2) = 2n-3
#
# Final formula: n! * (2n - 3)
from math import factorial

from pytest import mark


def get_itinerary_count(stops: list[str]) -> int:
    n = len(stops)
    return factorial(n) * (2 * n - 3)


# Solution 2: Brute force using itertools.permutations
#
# For each ordered permutation of the optional stops, count how many ways
# to insert lunch and dinner as dividers, splitting the stops into 3 groups:
#   [breakfast] [i stops] [lunch] [j stops] [dinner] [remaining stops]
# where i >= 1, j >= 1, and remaining <= 1.
#
# Each unique (permutation, i, j) that satisfies the constraints is one valid itinerary.
# Summing over all permutations gives the total count.
# This is O(n! * n^2) — only feasible for small n, but useful for verifying the formula.
# from itertools import permutations

# from pytest import mark


# def get_itinerary_count(stops: list[str]) -> int:
#     count = 0

#     for perm in permutations(stops):
#         n = len(perm)
#         for i in range(1, n + 1):  # i stops before lunch (>= 1)
#             for j in range(1, n - i + 1):  # j stops before dinner (>= 1)
#                 after = n - i - j  # remainder after dinner
#                 if after <= 1:
#                     count += 1

#     return count


tests = [
    (['library', 'park'], 2),
    (['library', 'park', 'arcade'], 18),
    (['library', 'park', 'arcade', 'store'], 120),
    (['library', 'park', 'arcade', 'store', 'cafe'], 840),
    (['library', 'park', 'arcade', 'store', 'cafe', 'market', 'museum'], 55440),
]


@mark.parametrize('stops, expected', tests)
def test_get_itinerary_count(stops: list[str], expected: int) -> None:
    assert get_itinerary_count(stops) == expected


if __name__ == '__main__':
    stops, expected = tests[0]
    print(get_itinerary_count(stops))
