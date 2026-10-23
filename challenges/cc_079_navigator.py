"""Daily Coding Challenge #79 (2025-10-28) - freeCodeCamp.org."""

# Navigator
# On October 28, 1994, Netscape Navigator was released, helping millions explore the
# early web.
#
# Given an array of browser commands you executed on Netscape Navigator, return the
# current page you are on after executing all the commands using the following rules:
#
# - You always start on the "Home" page, which will not be included in the commands
#   array.
# - Valid commands are:
#   - "Visit Page": Where "Page" is the name of the page you are visiting. For example,
# "Visit About" takes you to the "About" page. When you visit a new page, make sure to
# discard any forward history you have.
#   - "Back": Takes you to the previous page in your history or stays on the current
# page if there isn't one.
#   - "Forward": Takes you forward in the history to the page you came from or stays on
# the current page if there isn't one.
#
# For example, given ["Visit About Us", "Back", "Forward"], return "About Us".
from pytest import mark

_START_PAGE = 'Home'
_VISIT_PREFIX = 'Visit '
_BACK_COMMAND = 'Back'
_FORWARD_COMMAND = 'Forward'


def navigate(commands: list[str]) -> str:
    """Return the current page after executing all commands.

    Page names are taken verbatim after 'Visit ', so a whitespace-only name
    (e.g. 'Visit  ', page ' ') is accepted; only an empty name is rejected.

    Args:
        commands: Browser commands, executed in order.

    Returns:
        The name of the page shown after the last command.

    Raises:
        ValueError: If a command is not 'Back', 'Forward' or 'Visit <page>'.
    """
    history = [_START_PAGE]
    current = 0

    for command in commands:
        if command == _BACK_COMMAND:
            current = max(current - 1, 0)
        elif command == _FORWARD_COMMAND:
            current = min(current + 1, len(history) - 1)
        elif command.startswith(_VISIT_PREFIX):
            page = command.removeprefix(_VISIT_PREFIX)
            if not page:
                msg = f'missing page name: {command!r}'
                raise ValueError(msg)
            del history[current + 1 :]  # visiting discards forward history
            history.append(page)
            current += 1
        else:
            msg = f'invalid command: {command!r}'
            raise ValueError(msg)

    return history[current]


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
    """Test navigate function."""
    assert navigate(commands) == expected


if __name__ == '__main__':
    commands, expected = tests[0]
    print(navigate(commands))
