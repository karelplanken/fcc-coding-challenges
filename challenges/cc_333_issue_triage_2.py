"""Daily Coding Challenge #333 (2026-07-09) - freeCodeCamp.org."""

# Issue Triage 2
# Given an issue title and an array of current labels, return an updated array of labels
# based on the following rules:

# If the issue doesn't have any labels, add:
# "bug" and "needs triage" if the title contains "error" or "bug"
# "enhancement" and "discussing" if the title contains "feature" or "add"

# Otherwise, if the given labels contain:
# "needs triage" and the title contains "simple" or "easy", remove "needs triage" and
# add "good first issue"
# "discussing" and the title contains "planned" or "next", remove "discussing" and
# add "on the roadmap"
# Otherwise, if "needs triage" or "discussing" is present, remove it and
# add "help wanted"
# If the title contains:
# "security", add a "critical" label
from pytest import mark


def triage_issue(title: str, labels: list[str]) -> list[str]:
    labels = list(labels)  # don't mutate the caller's list

    if not labels:
        if 'error' in title or 'bug' in title:
            labels = ['bug', 'needs triage']
        if 'feature' in title or 'add' in title:
            labels = ['enhancement', 'discussing']
    else:
        if 'needs triage' in labels:
            labels.remove('needs triage')
            labels.append(
                'good first issue'
                if 'simple' in title or 'easy' in title
                else 'help wanted'
            )
        if 'discussing' in labels:
            labels.remove('discussing')
            labels.append(
                'on the roadmap'
                if 'planned' in title or 'next' in title
                else 'help wanted'
            )

    if 'security' in title:
        labels.append('critical')

    return labels


# from collections.abc import Callable
# Handler = Callable[[str, list[str]], list[str]]


# def _no_labels(title: str, labels: list[str]) -> list[str]:
#     if 'error' in title or 'bug' in title:
#         labels = ['bug', 'needs triage']
#     if 'feature' in title or 'add' in title:
#         labels = ['enhancement', 'discussing']
#     return labels


# def _needs_triage(title: str, labels: list[str]) -> list[str]:
#     labels.remove('needs triage')
#     labels.append(
#         'good first issue' if 'simple' in title or 'easy' in title else 'help wanted'
#     )
#     return labels


# def _discussing(title: str, labels: list[str]) -> list[str]:
#     labels.remove('discussing')
#     labels.append(
#         'on the roadmap' if 'planned' in title or 'next' in title else 'help wanted'
#     )
#     return labels


# RULES: list[tuple[Callable[[list[str]], bool], Handler]] = [
#     (lambda lbls: 'needs triage' in lbls, _needs_triage),
#     (lambda lbls: 'discussing' in lbls, _discussing),
# ]


# def triage_issue(title: str, labels: list[str]) -> list[str]:
#     if not labels:
#         labels = _no_labels(title, labels)
#     else:
#         for predicate, handler in RULES:
#             if predicate(labels):
#                 labels = handler(title, labels)
#     if 'security' in title:
#         labels.append('critical')
#     return labels


tests: list[tuple[str, list[str], list[str]]] = [
    ('app crashes with error', [], ['bug', 'needs triage']),
    ('app crashes with error', ['bug', 'needs triage'], ['bug', 'help wanted']),
    ('add dark mode', [], ['enhancement', 'discussing']),
    ('add dark mode', ['enhancement', 'discussing'], ['enhancement', 'help wanted']),
    ('xss security bug', [], ['bug', 'needs triage', 'critical']),
    ('security vulnerability in auth', [], ['critical']),
    ('easy a11y fix', ['bug', 'needs triage'], ['bug', 'good first issue']),
    (
        'planned api migration',
        ['enhancement', 'discussing'],
        ['enhancement', 'on the roadmap'],
    ),
    (
        'improve security',
        ['enhancement', 'discussing'],
        ['enhancement', 'help wanted', 'critical'],
    ),
]


@mark.parametrize('title, labels, expected', tests)
def test_triage_issue(title: str, labels: list[str], expected: list[str]) -> None:
    """Test triage_issue function."""
    assert sorted(triage_issue(title, labels)) == sorted(expected)


if __name__ == '__main__':
    title, labels, expected = tests[0]
    print(triage_issue(title, labels))
