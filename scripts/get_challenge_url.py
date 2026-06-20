import json
import os
import re
import sys
import urllib.request
from datetime import UTC, date, datetime, timedelta, timezone
from typing import Final

SERIES_START: Final[date] = date(2025, 8, 11)
DATE_PATTERN: Final[re.Pattern[str]] = re.compile(r'^\d{4}-\d{2}-\d{2}$')
NUMBER_PATTERN: Final[re.Pattern[str]] = re.compile(r'^\d+$')
GITHUB_SEARCH_URL_TEMPLATE: Final[str] = (
    'https://api.github.com/search/code'
    '?q=dashedName:+challenge-{number}+repo:freeCodeCamp/freeCodeCamp'
)
GITHUB_CONTENTS_URL_TEMPLATE: Final[str] = (
    'https://api.github.com/repos/freeCodeCamp/freeCodeCamp/contents/{path}'
)

PYTHON_CHALLENGE_PATH_SEGMENT: Final[str] = 'daily-coding-challenges-python'
USAGE: Final[str] = ('Usage: uv run scripts/get_challenge_url.py [YYYY-MM-DD|NUMBER]')
CENTRAL_STANDARD_OFFSET: Final[timedelta] = timedelta(hours=-6)
CENTRAL_DAYLIGHT_OFFSET: Final[timedelta] = timedelta(hours=-5)


def nth_weekday_of_month(year: int, month: int, weekday: int, occurrence: int) -> date:
    first_day = date(year, month, 1)
    days_until_weekday = (weekday - first_day.weekday()) % 7
    return first_day + timedelta(days=days_until_weekday + (occurrence - 1) * 7)


def is_us_central_daylight_saving(moment_utc: datetime) -> bool:
    second_sunday_in_march = nth_weekday_of_month(moment_utc.year, 3, 6, 2)
    first_sunday_in_november = nth_weekday_of_month(moment_utc.year, 11, 6, 1)

    daylight_saving_start_utc = datetime(
        second_sunday_in_march.year,
        second_sunday_in_march.month,
        second_sunday_in_march.day,
        8,
        tzinfo=UTC,
    )
    daylight_saving_end_utc = datetime(
        first_sunday_in_november.year,
        first_sunday_in_november.month,
        first_sunday_in_november.day,
        7,
        tzinfo=UTC,
    )

    return daylight_saving_start_utc <= moment_utc < daylight_saving_end_utc


def get_us_central_today() -> date:
    now_utc = datetime.now(UTC)
    offset = CENTRAL_DAYLIGHT_OFFSET
    if not is_us_central_daylight_saving(now_utc):
        offset = CENTRAL_STANDARD_OFFSET
    return now_utc.astimezone(timezone(offset)).date()


def challenge_number_for_date(target_date: date) -> int:
    return (target_date - SERIES_START).days + 1


def max_available_challenge_number() -> int:
    return challenge_number_for_date(get_us_central_today())


def parse_target_number(argv: list[str]) -> int:
    if len(argv) > 2:
        raise ValueError(USAGE)

    maximum_number = max_available_challenge_number()

    if len(argv) == 1:
        return maximum_number

    argument = argv[1]
    if DATE_PATTERN.fullmatch(argument):
        target_date = date.fromisoformat(argument)
        target_number = challenge_number_for_date(target_date)
    elif NUMBER_PATTERN.fullmatch(argument):
        target_number = int(argument)
    else:
        raise ValueError(USAGE)

    if target_number < 1:
        raise ValueError(
            f'Error: challenge must be on or after {SERIES_START.isoformat()}.'
        )
    if target_number > maximum_number:
        raise ValueError(
            'Error: challenge is not available yet. '
            f'Maximum available challenge number is {maximum_number}.'
        )

    return target_number


def get_github_token() -> str:
    github_token = os.environ.get('GITHUB_TOKEN')
    if github_token is None or github_token == '':
        raise ValueError('Error: GITHUB_TOKEN is not set.')
    return github_token


def read_json_response(url: str, github_token: str) -> object:
    request = urllib.request.Request(
        url,
        headers={
            'Authorization': f'token {github_token}',
            'Accept': 'application/vnd.github+json',
        },
    )
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read().decode('utf-8'))


def extract_python_challenge_path(response_data: object) -> str:
    if not isinstance(response_data, dict):
        raise ValueError('Error: unexpected response from GitHub search API.')

    items = response_data.get('items')
    if not isinstance(items, list):
        raise ValueError('Error: unexpected response from GitHub search API.')

    for item in items:
        if not isinstance(item, dict):
            continue
        path = item.get('path')
        if isinstance(path, str) and PYTHON_CHALLENGE_PATH_SEGMENT in path:
            return path

    raise ValueError('Error: no Python challenge result found.')


def extract_download_url(response_data: object) -> str:
    if not isinstance(response_data, dict):
        raise ValueError('Error: unexpected response from GitHub contents API.')

    download_url = response_data.get('download_url')
    if not isinstance(download_url, str) or download_url == '':
        raise ValueError('Error: missing download URL in GitHub contents API response.')

    return download_url


def main(argv: list[str]) -> int:
    try:
        target_number = parse_target_number(argv)
        github_token = get_github_token()
        search_url = GITHUB_SEARCH_URL_TEMPLATE.format(number=target_number)
        response_data = read_json_response(search_url, github_token)
        challenge_path = extract_python_challenge_path(response_data)
        contents_url = GITHUB_CONTENTS_URL_TEMPLATE.format(path=challenge_path)
        contents_response = read_json_response(contents_url, github_token)
        download_url = extract_download_url(contents_response)
    except ValueError as error:
        print('ValueError')
        print(error, file=sys.stderr)
        return 1
    except OSError as error:
        print('OSError')
        print(f'Error: failed to query GitHub API: {error}', file=sys.stderr)
        return 1

    print(download_url)
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
