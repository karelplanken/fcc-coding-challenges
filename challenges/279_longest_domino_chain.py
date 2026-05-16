# Daily Coding challenge #279 (2026-05-16) - freeCodeCamp.org
# Longest Domino Chain
# Given a 2D array representing a set of dominoes, return the longest valid chain.
# Each domino is a pair of numbers from 0–6, e.g. [3, 2].
# A chain is valid when the second number of each domino matches the first number of
# the next.
# The first number of the first domino and the second number of the last one don't need
# to match anything.
# Any domino can be flipped, so [3, 2] can be played as [2, 3].
# There is always exactly one longest valid chain.
# For example, given [[1, 2], [4, 5], [2, 3]], return [[1, 2], [2, 3]].


# Solution employing depth-first search (DFS) to explore all possible chains and keep
# track of the longest one found. The DFS function takes the current chain, the
# remaining dominoes, and the best chain found so far. It iterates through the
# remaining dominoes, checking if they can be added to the current chain (either in
# original or flipped orientation). If a domino can be added, it is appended to the
# chain, and the DFS function is called recursively with the updated chain and
# remaining dominoes. After exploring that path, the domino is removed from the chain
# (backtracking) to explore other possibilities. The main function initializes the best
# chain and starts the DFS for each domino in both orientations.
from pytest import mark


def dfs(
    chain: list[list[int]], remaining: list[list[int]], best: list[list[int]]
) -> list[list[int]]:
    best = chain.copy() if len(chain) > len(best) else best
    rest = []

    for idx, domino in enumerate(remaining):
        rest = remaining[:idx] + remaining[idx + 1 :]

        if domino[0] == chain[-1][1]:
            chain.append(domino)
            best = dfs(chain, rest, best)
            chain.pop()

        if domino[1] == chain[-1][1] and len(set(domino)) != 1:
            chain.append(domino[::-1])
            best = dfs(chain, rest, best)
            chain.pop()

    return best


def get_longest_chain(dominoes: list[list[int]]) -> list[list[int]]:
    best = []

    for idx, domino in enumerate(dominoes):
        best = dfs([domino], dominoes[:idx] + dominoes[idx + 1 :], best)
        if len(set(domino)) != 1:
            best = dfs([domino[::-1]], dominoes[:idx] + dominoes[idx + 1 :], best)

    return best


tests = [
    ([[1, 2], [4, 5], [2, 3]], [[1, 2], [2, 3]]),
    ([[2, 1], [4, 3], [5, 3]], [[4, 3], [3, 5]]),
    ([[1, 2], [3, 4], [2, 3], [4, 0]], [[1, 2], [2, 3], [3, 4], [4, 0]]),
    (
        [[6, 6], [6, 1], [1, 1], [0, 3], [2, 3], [4, 1], [5, 6]],
        [[4, 1], [1, 1], [1, 6], [6, 6], [6, 5]],
    ),
    (
        [[0, 4], [3, 3], [0, 3], [5, 6], [4, 5], [4, 2], [5, 5], [1, 2], [4, 4]],
        [[3, 3], [3, 0], [0, 4], [4, 4], [4, 5], [5, 5], [5, 6]],
    ),
]


@mark.parametrize('dominoes, expected', tests)
def test_get_longest_chain(
    dominoes: list[list[int]],
    expected: list[list[int]],
) -> None:
    assert get_longest_chain(dominoes) == expected


if __name__ == '__main__':
    dominoes, expected = tests[4]
    print(get_longest_chain(dominoes))
