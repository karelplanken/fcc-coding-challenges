# Daily Coding challenge #153 (2026-01-10) - freeCodeCamp.org
# Tic-Tac-Toe
# Given a 3×3 matrix (an array of arrays) representing a completed Tic-Tac-Toe game,
# determine the winner.

# Each element in the given matrix is either an "X" or "O".
# A player wins if they have three of their characters in a row - horizontally,
# vertically, or diagonally.

# Return:

# "X wins" if player X has three in a row.
# "O wins" if player O has three in a row.
# "Draw" if no player has three in a row.
from pytest import mark


def tic_tac_toe(board: list[list[str]], dim: int = 3) -> str:
    def check_winner(line: list[str]) -> str | None:
        """Check if a line has a winner and return the result."""
        if len(winner := set(line)) == 1:
            return f'{winner.pop()} wins'
        return None

    # Check rows
    for row in board:
        if result := check_winner(row):
            return result

    # Check columns
    for col in range(dim):
        column = [board[row][col] for row in range(dim)]
        if result := check_winner(column):
            return result

    # Check main diagonal (top-left to bottom-right)
    main_diagonal = [board[i][i] for i in range(dim)]
    if result := check_winner(main_diagonal):
        return result

    # Check anti-diagonal (top-right to bottom-left)
    anti_diagonal = [board[i][j] for i, j in zip(range(dim), reversed(range(dim)))]
    if result := check_winner(anti_diagonal):
        return result

    return 'Draw'


tests = [
    ([['X', 'X', 'X'], ['O', 'O', 'X'], ['O', 'X', 'O']], 'X wins'),
    ([['X', 'O', 'X'], ['X', 'O', 'X'], ['O', 'O', 'X']], 'O wins'),
    ([['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']], 'Draw'),
    ([['X', 'X', 'O'], ['X', 'O', 'X'], ['O', 'X', 'X']], 'O wins'),
    ([['X', 'O', 'O'], ['O', 'X', 'O'], ['O', 'X', 'X']], 'X wins'),
    ([['O', 'X', 'X'], ['X', 'O', 'O'], ['X', 'O', 'X']], 'Draw'),
]


@mark.parametrize(('board', 'expected'), tests)
def test_tic_tac_toe(board: list[list[str]], expected: str) -> None:
    assert tic_tac_toe(board) == expected


# if __name__ == '__main__':
#     board, expected = tests[5]
#     print(tic_tac_toe(board))
