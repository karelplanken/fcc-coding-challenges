# Daily Coding challenge #89 (2025-11-07) - freeCodeCamp.org
# Counting Cards
# A standard deck of playing cards has 13 unique cards in each suit. Given an integer
# representing the number of cards to pick from the deck, return the number of unique
# combinations of cards you can pick.

# Order does not matter. Picking card A then card B is the same as picking card B then
# card A. For example, given 52, return 1. There's only one combination of 52 cards to
# pick from a 52 card deck. And given 2, return 1326, There's 1326 card combinations
# you can end up with when picking 2 cards from the deck.
from pytest import mark


# STEP 1: Naive approach using the formula directly
def combinations_v1(cards: int) -> int:
    """Direct formula implementation - works but inefficient"""

    def factorial(n: int) -> int:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    # C(52, k) = 52! / (k! × (52-k)!)
    return factorial(52) // (factorial(cards) * factorial(52 - cards))


# STEP 2: Cancel out common terms
# Instead of: 52! / (k! × (52-k)!)
# Notice: 52! = 52 × 51 × ... × (52-k+1) × (52-k)!
# So: C(52,k) = [52 × 51 × ... × (52-k+1)] / k!


def combinations_v2(cards: int) -> int:
    """Optimized - compute only what we need"""
    k = cards

    # Numerator: 52 × 51 × ... × (52-k+1)
    numerator = 1
    for i in range(52, 52 - k, -1):
        numerator *= i

    # Denominator: k!
    denominator = 1
    for i in range(1, k + 1):
        denominator *= i

    return numerator // denominator


# STEP 3: Interleave multiply and divide to avoid huge numbers
def combinations_v3(cards: int) -> int:
    """Most efficient - avoids overflow"""
    k = min(cards, 52 - cards)  # Use symmetry: C(52,50) = C(52,2)

    result = 1
    for i in range(k):
        result = result * (52 - i) // (i + 1)

    return result


def combinations(cards: int) -> int:
    if not (0 <= cards <= 52):
        raise ValueError('cards must be between 0 and 52 inclusive')

    # Optimize: C(n,k) = C(n, n-k), so use the smaller value
    k = min(cards, 52 - cards)

    # Calculate C(52, k) = 52! / (k! * (52-k)!)
    # Simplified: (52 * 51 * ... * (52-k+1)) / (k * (k-1) * ... * 1)
    result = 1
    for i in range(k):
        result = result * (52 - i) // (i + 1)

    return result


tests = [
    (52, 1),
    (1, 52),
    (2, 1326),
    (5, 2598960),
    (10, 15820024220),
    (50, 1326),
]


@mark.parametrize(('cards', 'expected'), tests)
def test_combinations(cards: int, expected: int) -> None:
    assert combinations(cards) == expected


if __name__ == '__main__':
    cards, expected = tests[0]
    print(combinations(cards))
