# Daily Coding challenge #184 (2026-02-10) - freeCodeCamp.org
# 2026 Winter Games Day 5: Cross-Country Skiing
# Given an array of finish times for a cross-country ski race, convert them into times 
# behind the winner.

# Given times are strings in "H:MM:SS" format.
# Given times will be in order from fastest to slowest.
# The winners time (fastest time) should correspond to "0".
# Each other time should show the time behind the winner, in the format "+M:SS".
# For example, given ["1:25:32", "1:26:10", "1:27:05"], return ["0", "+0:38", "+1:33"].
from pytest import mark


def get_relative_results(results: list[str]) -> list[str]:

    def get_seconds(time_str: str) -> int:
        hours, minutes, seconds = map(int, time_str.split(':'))
        return hours * 3600 + minutes * 60 + seconds
    
    def get_time_string(total_seconds: int) -> str:
        minutes, seconds = divmod(total_seconds, 60)
        return f'+{minutes}:{seconds:02d}'
    
    fastest_time = get_seconds(results[0])

    seconds_behind_winner = [
        get_seconds(finish_time) - fastest_time for finish_time in results[1:]
    ]
    
    return ['0'] + [
        get_time_string(time_behind_winner)
        for time_behind_winner in seconds_behind_winner
    ]

tests = [
    (['1:25:32', '1:26:10', '1:27:05'], ['0', '+0:38', '+1:33']),
    (['1:00:01', '1:00:05', '1:00:10'], ['0', '+0:04', '+0:09']),
    (['1:10:06', '1:10:23', '1:10:48', '1:12:11'], ['0', '+0:17', '+0:42', '+2:05']),
    (
        [
            '0:49:13',
            '0:49:15',
            '0:50:14',
            '0:51:30',
            '0:51:58',
            '0:52:16',
            '0:53:12',
            '0:53:31',
            '0:56:19',
            '1:02:20',
        ],
        [
            '0',
            '+0:02',
            '+1:01',
            '+2:17',
            '+2:45',
            '+3:03',
            '+3:59',
            '+4:18',
            '+7:06',
            '+13:07',
        ],
    ),
    (
        [
            '2:01:15',
            '2:10:45',
            '2:10:53',
            '2:11:04',
            '2:11:55',
            '2:13:27',
            '2:14:30',
            '2:15:10',
        ],
        ['0', '+9:30', '+9:38', '+9:49', '+10:40', '+12:12', '+13:15', '+13:55'],
    ),
]

@mark.parametrize('results, expected', tests)
def test_solution(results: list[str], expected: list[str]) -> None:
    assert get_relative_results(results) == expected


if __name__ == '__main__':
    results, expected = tests[0]
    print(get_relative_results(results))