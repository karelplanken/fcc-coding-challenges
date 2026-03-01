# Daily Coding challenge #139 (2025-12-27) - freeCodeCamp.org
# Rock, Paper, Scissors
# Given two strings, the first representing Player 1 and the second representing
# Player 2, determine the winner of a match of Rock, Paper, Scissors.

# The input strings will always be "Rock", "Paper", or "Scissors".
# "Rock" beats "Scissors".
# "Paper" beats "Rock".
# "Scissors" beats "Paper".
# Return:

# "Player 1 wins" if Player 1 wins.
# "Player 2 wins" if Player 2 wins.
# "Tie" if both players choose the same option.
from pytest import mark


# Circular linked list representation of game rules:
class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.beats: Node  # More descriptive than "next"
        self.loses_to: Node  # More descriptive than "previous"


def setup_rps_graph() -> dict[str, Node]:
    """Create circular linked list representing game rules."""
    rock = Node('Rock')
    paper = Node('Paper')
    scissors = Node('Scissors')

    # Rock beats Scissors, loses to Paper
    rock.beats = scissors
    rock.loses_to = paper

    # Scissors beats Paper, loses to Rock
    scissors.beats = paper
    scissors.loses_to = rock

    # Paper beats Rock, loses to Scissors
    paper.beats = rock
    paper.loses_to = scissors

    return {'Rock': rock, 'Paper': paper, 'Scissors': scissors}


RPS_GRAPH = setup_rps_graph()


def rock_paper_scissors(player1: str, player2: str) -> str:
    rps1 = RPS_GRAPH[player1]
    rps2 = RPS_GRAPH[player2]

    if rps1.beats.name == rps2.name:
        return 'Player 1 wins'
    if rps1.loses_to.name == rps2.name:
        return 'Player 2 wins'
    return 'Tie'


# Simple lookup: what does each choice beat?
# BEATS = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}


# def rock_paper_scissors(player1: str, player2: str) -> str:
#     if player1 == player2:
#         return 'Tie'
#     if BEATS[player1] == player2:
#         return 'Player 1 wins'
#     return 'Player 2 wins'


# # Map choices to numbers for modular arithmetic
# CHOICE_VALUE = {'Rock': 0, 'Paper': 1, 'Scissors': 2}


# def rock_paper_scissors(player1: str, player2: str) -> str:
#     diff = (CHOICE_VALUE[player1] - CHOICE_VALUE[player2]) % 3

#     if diff == 0:
#         return 'Tie'
#     if diff == 1:
#         return 'Player 1 wins'  # Fixed!
#     return 'Player 2 wins'


tests = [
    ('Rock', 'Rock', 'Tie'),
    ('Rock', 'Paper', 'Player 2 wins'),
    ('Scissors', 'Paper', 'Player 1 wins'),
    ('Rock', 'Scissors', 'Player 1 wins'),
    ('Scissors', 'Scissors', 'Tie'),
    ('Scissors', 'Rock', 'Player 2 wins'),
]


@mark.parametrize('player1, player2, expected', tests)
def test_rock_paper_scissors(player1: str, player2: str, expected: str) -> None:
    assert rock_paper_scissors(player1, player2) == expected


if __name__ == '__main__':
    player1, player2, expected = tests[1]
    print(rock_paper_scissors(player1, player2))
