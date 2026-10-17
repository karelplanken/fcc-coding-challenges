"""Daily Coding Challenge #69 (2025-10-18) - freeCodeCamp.org."""

# Missing Socks
# Given an integer representing the number of pairs of socks you started with, and
# another integer representing how many wash cycles you have gone through, return the
# number of complete pairs of socks you currently have using the following constraints:
#
# - Every 2 wash cycles, you lose a single sock.
# - Every 3 wash cycles, you find a single missing sock.
# - Every 5 wash cycles, a single sock is worn out and must be thrown away.
# - Every 10 wash cycles, you buy a pair of socks.
# - You can never have less than zero total socks.
# - Rules can overlap. For example, on wash cycle 10, you will lose a single sock, throw
#   away a single sock, and buy a new pair of socks.
# - Return the number of complete pairs of socks.
from pytest import mark


def sock_pairs(pairs: int, cycles: int) -> int:
    """Return the number of complete pairs of socks after a number of wash cycles.

    Rules that trigger on the same cycle all apply. Within a cycle, losses are
    applied before gains, and the sock count never drops below zero, so socks
    found or bought in a cycle cannot offset a loss that has already hit zero.

    Args:
        pairs: The number of pairs of socks you started with.
        cycles: The number of wash cycles you have gone through.

    Returns:
        The number of complete pairs of socks after the given number of cycles.

    Raises:
        ValueError: If ``pairs`` or ``cycles`` is negative.
    """
    if pairs < 0:
        msg = f'pairs must be non-negative, got {pairs}'
        raise ValueError(msg)
    if cycles < 0:
        msg = f'cycles must be non-negative, got {cycles}'
        raise ValueError(msg)

    socks = 2 * pairs

    for cycle in range(1, cycles + 1):
        # Losses first; the order matters once the count reaches zero.
        if cycle % 2 == 0 and socks > 0:  # lose a sock
            socks -= 1
        if cycle % 5 == 0 and socks > 0:  # throw away a worn-out sock
            socks -= 1

        if cycle % 3 == 0:  # find a missing sock
            socks += 1
        if cycle % 10 == 0:  # buy a new pair
            socks += 2

    return socks // 2


tests = [
    (2, 5, 1),
    (1, 2, 0),
    (5, 11, 4),
    (6, 25, 3),
    (1, 8, 0),
]


@mark.parametrize('pairs, cycles, expected', tests)
def test_sock_pairs(pairs: int, cycles: int, expected: int) -> None:
    """Test sock_pairs function."""
    assert sock_pairs(pairs, cycles) == expected


if __name__ == '__main__':
    pairs, cycles, expected = tests[0]
    print(sock_pairs(pairs, cycles))
