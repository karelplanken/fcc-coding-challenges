# Daily Coding challenge #116 (2025-12-04) - freeCodeCamp.org
# Permutation Count
# Given a string, return the number of distinct permutations that can be formed from
# its characters.

# A permutation is any reordering of the characters in the string.
# Do not count duplicate permutations.
# If the string contains repeated characters, repeated arrangements should only
# be counted once.
# The string will contain only letters (A-Z, a-z).
# For example, given "abb", return 3 because there's three unique ways to arrange
# the letters: "abb", "bab", and "bba".

# Taken from https://www.geeksforgeeks.org/dsa/write-a-c-program-to-print-all-permutations-of-a-given-string/
# Python Program to generate all unique
# permutations of a string


# Recursive function to generate
# all permutations of string s
import math
from collections import Counter

from pytest import mark


def recursive_permutation(index: int, s: list[str], ans: list[str]) -> None:
    # Base Case
    if index == len(s):
        ans.append(''.join(s))
        return

    # Track which characters we've already used at this position
    used = set()

    # Swap the current index with all
    # possible indices and recur
    for i in range(index, len(s)):
        # Skip if we've already used this character at this position
        if s[i] in used:
            continue

        # Mark this character as used at this position
        used.add(s[i])

        # Make the choice: swap
        s[index], s[i] = s[i], s[index]

        # Explore: recurse with this choice
        recursive_permutation(index + 1, s, ans)

        # Undo the choice: backtrack
        s[index], s[i] = s[i], s[index]


# Function to find all unique permutations
def find_unique_permutation(s: str) -> list[str]:
    # Stores the final answer
    ans: list[str] = []

    recursive_permutation(0, list(s), ans)

    # sort the resultant list
    # ans.sort()

    return ans


# def count_permutations(s: str) -> int:
#     return len(find_unique_permutation(s))


def count_permutations(s: str) -> int:
    """
    Count unique permutations using the mathematical formula:
    n! / (n1! x n2! x ... x nk!)

    Where n is the total length and n1, n2, etc. are the
    frequencies of each character.
    """
    n = len(s)

    # Count frequency of each character
    freq = Counter(s)

    # Start with n!
    numerator = math.factorial(n)

    # Divide by the factorial of each character's frequency
    denominator = 1
    for count in freq.values():
        denominator *= math.factorial(count)

    return numerator // denominator


tests = [('abb', 3), ('abc', 6), ('racecar', 630), ('freecodecamp', 39916800)]


@mark.parametrize('s,expected', tests)
def test_count_permutations(s: str, expected: int) -> None:
    assert count_permutations(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(count_permutations(s))
