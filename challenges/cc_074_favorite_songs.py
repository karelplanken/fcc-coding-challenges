"""Daily Coding Challenge #74 (2025-10-23) - freeCodeCamp.org."""

# Favorite Songs
# Remember iPods? The first model came out 24 years ago today, on Oct. 23, 2001.
#
# Given an array of song objects representing your iPod playlist, return an array with
# the titles of the two most played songs, with the most played song first.
#
# - Each object will have a "title" property (string), and a "plays" property (integer).
from heapq import nlargest
from typing import TypedDict

from pytest import mark


class Song(TypedDict):
    """A song object with a title and number of plays."""

    title: str
    plays: int


_N_MOST_POPULAR = 2


def favorite_songs(playlist: list[Song]) -> list[str]:
    """Return the titles of the two most played songs in the playlist.

    Ties are broken by playlist order (earlier song first).

    Args:
        playlist: A list of song objects, each with a title and number of plays.

    Returns:
        The titles of the two most played songs, most played first. Fewer than
        two titles if the playlist is shorter.
    """
    top = nlargest(_N_MOST_POPULAR, playlist, key=lambda song: song['plays'])
    return [song['title'] for song in top]


tests: list[tuple[list[Song], list[str]]] = [
    (
        [
            {'title': 'Sync or Swim', 'plays': 3},
            {'title': 'Byte Me', 'plays': 1},
            {'title': 'Earbud Blues', 'plays': 2},
        ],
        ['Sync or Swim', 'Earbud Blues'],
    ),
    (
        [
            {'title': 'Skip Track', 'plays': 98},
            {'title': '99 Downloads', 'plays': 99},
            {'title': 'Clickwheel Love', 'plays': 100},
        ],
        ['Clickwheel Love', '99 Downloads'],
    ),
    (
        [
            {'title': 'Song A', 'plays': 42},
            {'title': 'Song B', 'plays': 99},
            {'title': 'Song C', 'plays': 75},
        ],
        ['Song B', 'Song C'],
    ),
]


@mark.parametrize('playlist, expected', tests)
def test_favorite_songs(playlist: list[Song], expected: list[str]) -> None:
    """Test favorite_songs function."""
    assert favorite_songs(playlist) == expected


if __name__ == '__main__':
    playlist, expected = tests[0]
    print(favorite_songs(playlist))
