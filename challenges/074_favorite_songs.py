# Daily Coding challenge #74 (2025-10-23) - freeCodeCamp.org
# Favorite Songs
# Remember iPods? The first model came out 24 years ago today, on Oct. 23, 2001.

# Given an array of song objects representing your iPod playlist, return an array with
# the titles of the two most played songs, with the most played song first.

# Each object will have a "title" property (string), and a "plays" property (integer).
from operator import itemgetter

from pytest import mark


def favorite_songs(
    playlist: list[dict[str, str]], n_most_popular: int = 2
) -> list[str]:
    return [
        song['title']
        for song in sorted(playlist, key=itemgetter('plays'), reverse=True)[
            :n_most_popular
        ]
    ]


tests = [
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
def test_favorite_songs(playlist: list[dict[str, str]], expected: list[str]) -> None:
    assert favorite_songs(playlist) == expected


if __name__ == '__main__':
    playlist, expected = tests[0]
    print(favorite_songs(playlist))
