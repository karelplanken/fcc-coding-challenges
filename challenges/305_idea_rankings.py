# Daily Coding challenge #305 (2026-06-11) - freeCodeCamp.org
# Idea Rankings
# Given a 2D array where each inner array contains (in this order) an idea name, an
# optimistic estimate, a realistic estimate, and a pessimistic estimate (in days),
# return an array of the idea names sorted by expected time to completion, shortest
# first.
# Calculate the expected time to completion for each idea using the following formula:
# expected = ((optimistic + 4 * realistic + pessimistic) / 6) * length of idea name
from pytest import mark


class Idea:
    def __init__(
        self, name: str, optimistic: int, realistic: int, pessimistic: int
    ) -> None:
        self.name = name
        self.expected_completion_time: float = (
            (optimistic + 4 * realistic + pessimistic) / 6
        ) * len(name)

    @classmethod
    def from_raw(cls, row: list[str | int]) -> Idea:
        name, opt, real, pess = row
        assert isinstance(name, str)
        assert isinstance(opt, int)
        assert isinstance(real, int)
        assert isinstance(pess, int)
        return cls(name, opt, real, pess)


def analyze_ideas(ideas: list[list[str | int]]) -> list[str]:
    return [
        idea.name
        for idea in sorted(
            (Idea.from_raw(row) for row in ideas),
            key=lambda x: x.expected_completion_time,
        )
    ]


tests: list[tuple[list[list[str | int]], list[str]]] = [
    (
        [
            ['Add logging', 2, 5, 15],
            ['SEO optimization', 4, 8, 20],
            ['Fix bug', 1, 3, 5],
        ],
        ['Fix bug', 'Add logging', 'SEO optimization'],
    ),
    (
        [
            ['Dark mode', 1, 3, 8],
            ['Real-time collaboration feature', 6, 12, 20],
            ['Add tooltip', 1, 2, 4],
        ],
        ['Add tooltip', 'Dark mode', 'Real-time collaboration feature'],
    ),
    (
        [
            ['Update user profile page', 3, 7, 14],
            ['Add pagination', 2, 5, 10],
            ['Add tags', 2, 3, 6],
            ['Fix login bug', 1, 4, 8],
        ],
        ['Add tags', 'Fix login bug', 'Add pagination', 'Update user profile page'],
    ),
    (
        [
            ['Migrate database', 14, 25, 40],
            ['Add chat assistant', 8, 15, 24],
            ['Redesign onboarding flow', 3, 7, 13],
            ['Add language support', 6, 11, 18],
        ],
        [
            'Redesign onboarding flow',
            'Add language support',
            'Add chat assistant',
            'Migrate database',
        ],
    ),
    (
        [
            ['Add email notifications', 3, 7, 10],
            ['Migrate deployment flow', 6, 10, 16],
            ['Add push notifications', 2, 6, 10],
            ['Optimize continuous integration', 5, 8, 15],
            ['Analyze user patterns', 5, 10, 18],
            ['Create onboarding curriculum', 6, 15, 25],
        ],
        [
            'Add push notifications',
            'Add email notifications',
            'Analyze user patterns',
            'Migrate deployment flow',
            'Optimize continuous integration',
            'Create onboarding curriculum',
        ],
    ),
]


@mark.parametrize('ideas, expected', tests)
def test_analyze_ideas(ideas: list[list[str | int]], expected: list[str]) -> None:
    assert analyze_ideas(ideas) == expected


if __name__ == '__main__':
    ideas, expected = tests[0]
    print(analyze_ideas(ideas))
