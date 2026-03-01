# Daily Coding challenge #69 (2025-10-18) - freeCodeCamp.org
# Missing Socks
# Given an integer representing the number of pairs of socks you started with, and
# another integer representing how many wash cycles you have gone through, return the
# number of complete pairs of socks you currently have using the following constraints:

# Every 2 wash cycles, you lose a single sock.
# Every 3 wash cycles, you find a single missing sock.
# Every 5 wash cycles, a single sock is worn out and must be thrown away.
# Every 10 wash cycles, you buy a pair of socks.
# You can never have less than zero total socks.
# Rules can overlap. For example, on wash cycle 10, you will lose a single sock, throw
# away a single sock, and buy a new pair of socks.
# Return the number of complete pairs of socks.
from pytest import mark


def sock_pairs(pairs: int, cycles: int) -> int:
    """Correct iterative approach - respects zero floor at each cycle.
    We're apparently:
    Washing our towels, shirts, and underwear (anything but socks)
    Losing imaginary socks from an empty drawer every 2 cycles
    Finding socks under the couch every 3 cycles (even when we had none!)
    Wearing out non-existent socks every 5 cycles
    Going shopping for new socks every 10 cycles

    The description should explicitly state what happens when rules apply at 0 socks!
    """
    socks = pairs * 2

    for cycle in range(1, cycles + 1):
        # Lose socks:
        if cycle % 2 == 0 and socks > 0:
            socks -= 1
        if cycle % 5 == 0 and socks > 0:
            socks -= 1

        # Gain socks:
        if cycle % 3 == 0:
            socks += 1

        if cycle % 10 == 0:
            socks += 2

    return socks // 2


# Using the "table-driven strategy pattern with lambdas" or "data-driven configuration":
# Incorrect approach - does not respect zero floor at each cycle.
# def sock_pairs(pairs: int, cycles: int) -> int:
#     SOCK_WASHING_CONSTRAINTS = [
#         lambda: (cycles // 2) * -1,
#         lambda: (cycles // 3) * 1,
#         lambda: (cycles // 5) * -1,
#         lambda: (cycles // 10) * 2,
#     ]

#     pairs_left = (
#         pairs * 2 + sum(constraint() for constraint in SOCK_WASHING_CONSTRAINTS)
#     ) // 2

#     if pairs_left < 0:
#         return 0

#     return pairs_left

# Correct solution using the lambda pattern:
# def sock_pairs(pairs: int, cycles: int) -> int:
#     socks = pairs * 2

#     # Define rules as lambdas that take current sock count
#     RULES = [
#         (2, lambda s: max(0, s - 1)),  # Lose sock every 2 cycles
#         (5, lambda s: max(0, s - 1)),  # Worn out every 5 cycles
#         (3, lambda s: s + 1),  # Find sock every 3 cycles
#         (10, lambda s: s + 2),  # Buy pair every 10 cycles
#     ]

#     for cycle in range(1, cycles + 1):
#         for divisor, rule in RULES:
#             if cycle % divisor == 0:
#                 socks = rule(socks)

#     return socks // 2


tests = [
    (2, 5, 1),
    (1, 2, 0),
    (5, 11, 4),
    (6, 25, 3),
    (1, 8, 0),
]


@mark.parametrize('pairs, cycles, expected', tests)
def test_sock_pairs(pairs: int, cycles: int, expected: int) -> None:
    assert sock_pairs(pairs, cycles) == expected


if __name__ == '__main__':
    pairs, cycles, expected = tests[4]
    print(sock_pairs(pairs, cycles))
