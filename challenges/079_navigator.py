# Daily Coding challenge #79 (2025-10-28) - freeCodeCamp.org
# Navigator
# On October 28, 1994, Netscape Navigator was released, helping millions explore the
# early web.

# Given an array of browser commands you executed on Netscape Navigator, return the
# current page you are on after executing all the commands using the following rules:

# You always start on the "Home" page, which will not be included in the commands array.
# Valid commands are:
# "Visit Page": Where "Page" is the name of the page you are visiting. For example, "
# Visit About" takes you to the "About" page. When you visit a new page, make sure to
# discard any forward history you have.
# "Back": Takes you to the previous page in your history or stays on the current page
# if there isn't one.
# "Forward": Takes you forward in the history to the page you came from or stays on the
# current page if there isn't one.
# For example, given ["Visit About Us", "Back", "Forward"], return "About Us".
from pytest import mark


def navigate(commands: list[str]) -> str:
    path = ['Home']
    current_idx = 0

    for command in commands:
        # Next page and delete forward history:
        if command.startswith('Visit '):
            page_name = command[6:]
            path = path[: current_idx + 1]
            path.append(page_name)
            current_idx += 1
        elif command == 'Back':
            # Decrement current_idx if possible:
            current_idx = max(0, current_idx - 1)
        elif command == 'Forward':
            # Increment current_idx if possible:
            current_idx = min(current_idx + 1, len(path) - 1)

    return path[current_idx]


tests = [
    (['Visit About Us', 'Back', 'Forward'], 'About Us'),
    (['Forward'], 'Home'),
    (['Back'], 'Home'),
    (['Visit About Us', 'Visit Gallery'], 'Gallery'),
    (['Visit About Us', 'Visit Gallery', 'Back', 'Back'], 'Home'),
    (['Visit About', 'Visit Gallery', 'Back', 'Visit Contact', 'Forward'], 'Contact'),
    (
        ['Visit About Us', 'Visit Visit Us', 'Forward', 'Visit Contact Us', 'Back'],
        'Visit Us',
    ),
]


@mark.parametrize('commands, expected', tests)
def test_navigate(commands: list[str], expected: str) -> None:
    assert navigate(commands) == expected


if __name__ == '__main__':
    commands, expected = tests[6]
    print(navigate(commands))
