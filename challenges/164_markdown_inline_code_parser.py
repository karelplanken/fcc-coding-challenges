# Daily Coding challenge #164 (2026-01-21) - freeCodeCamp.org
# Markdown Inline Code Parser
# Given a string of Markdown that includes one or more inline code blocks, return the 
# equivalent HTML string.

# Inline code blocks in Markdown use a single backtick (`) at the start and end of the 
# code block text.

# Return the given string with all code blocks converted to HTML code tags.

# For example, given the string "Use `let` to declare the variable.", 
# return "Use <code>let</code> to declare the variable.".

# Note: The console may not display HTML tags in strings when logging messages. 
# Check the browser console to see logs with tags included.
import re

from pytest import mark


def parse_inline_code(markdown: str) -> str:
    return re.sub(r'`([^`]*?)`', r'<code>\1</code>', markdown)


tests = [
    (
        'Use `let` to declare the variable.',
        'Use <code>let</code> to declare the variable.',
    ),
    (
        'Use `let` or `const` to declare a variable.',
        'Use <code>let</code> or <code>const</code> to declare a variable.',
    ),
    (
        'Run `npm install` then `npm start`.',
        'Run <code>npm install</code> then <code>npm start</code>.',
    ),
]

@mark.parametrize('input_str, expected', tests)
def test_parse_inline_code(input_str: str, expected: str) -> None:
    assert parse_inline_code(input_str) == expected


if __name__ == '__main__':
    input_str, expected = tests[1]
    print(parse_inline_code(input_str))