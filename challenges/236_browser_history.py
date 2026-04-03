# Daily Coding challenge #236 (2026-04-03) - freeCodeCamp.org
# Browser History
# Given an array of browser commands, return an array with two values: the history as
# an array of URLs, and the index of the current page.

# Valid commands are:

# "URL" - Where URL is a web address ("freecodecamp.org" for example). Navigates to the
# given URL, adds it to the history at the next position, and discards any forward
# history.
# "Back" - moves to the previous page in history, or stays on the current page if there
# isn't one.
# "Forward" - moves to the next page in history, or stays on the current page if there
# isn't one.
# For example, given ["freecodecamp.org", "freecodecamp.org/learn", "Back"],
# return [["freecodecamp.org", "freecodecamp.org/learn"], 0].
from pytest import mark


# Returns [history, current_index] — list shape is fixed by external test contract.
# Ideally this would return a tuple[list[str], int] or NamedTuple for precise typing.
def get_browser_history(commands: list[str]) -> list[list[str] | int]:
    history: list[str] = []
    current = -1

    for command in commands:
        if command == 'Back':
            if current > 0:
                current -= 1
        elif command == 'Forward':
            if current < len(history) - 1:
                current += 1
        else:
            del history[current + 1 :]
            history.append(command)
            current += 1

    return [history, current]


tests = [
    (
        ['freecodecamp.org', 'freecodecamp.org/learn', 'Back'],
        [['freecodecamp.org', 'freecodecamp.org/learn'], 0],
    ),
    (
        ['example.com', 'example.com/about', 'example.com/contact', 'example.com/blog'],
        [
            [
                'example.com',
                'example.com/about',
                'example.com/contact',
                'example.com/blog',
            ],
            3,
        ],
    ),
    (
        [
            'example.com',
            'example.com/about',
            'Back',
            'example.com/contact',
            'example.com/blog',
            'Back',
            'Back',
            'Forward',
        ],
        [['example.com', 'example.com/contact', 'example.com/blog'], 1],
    ),
    (
        [
            'example.com',
            'example.com/about',
            'example.com/contact',
            'example.com/blog',
            'Back',
            'Back',
            'Forward',
            'freecodecamp.org',
        ],
        [
            [
                'example.com',
                'example.com/about',
                'example.com/contact',
                'freecodecamp.org',
            ],
            3,
        ],
    ),
    (
        ['example.com', 'example.com/about', 'Back', 'Back'],
        [['example.com', 'example.com/about'], 0],
    ),
    (
        ['example.com', 'example.com/about', 'Forward'],
        [['example.com', 'example.com/about'], 1],
    ),
]


@mark.parametrize('commands, expected', tests)
def test_solution(commands: list[str], expected: list[list[str] | int]) -> None:
    assert get_browser_history(commands) == expected


if __name__ == '__main__':
    commands, expected = tests[2]
    print(get_browser_history(commands))
