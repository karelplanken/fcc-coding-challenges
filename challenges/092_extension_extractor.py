# Daily Coding challenge #92 (2025-11-10) - freeCodeCamp.org
# Extension Extractor
# Given a string representing a filename, return the extension of the file.

# The extension is the part of the filename that comes after the last period (.).
# If the filename does not contain a period or ends with a period, return "none".
# The extension should be returned as-is, preserving case.
from pytest import mark


def get_extension(filename: str) -> str:
    separator = '.'
    if filename.endswith(separator) or separator not in filename:
        return 'none'

    _, extension = filename.rsplit(separator, maxsplit=1)

    return extension


tests = [
    ('document.txt', 'txt'),
    ('README', 'none'),
    ('image.PNG', 'PNG'),
    ('.gitignore', 'gitignore'),
    ('archive.tar.gz', 'gz'),
    ('final.draft.', 'none'),
]


@mark.parametrize(('filename', 'expected'), tests)
def test_get_extension(filename: str, expected: str) -> None:
    assert get_extension(filename) == expected


if __name__ == '__main__':
    filename, expected = tests[0]
    print(get_extension(filename))
