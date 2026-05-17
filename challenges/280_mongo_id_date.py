# Daily Coding challenge #280 (2026-05-17) - freeCodeCamp.org
# Mongo ID Date
# Given a MongoDB ID string, return its creation time as an ISO 8601 string.

# A MongoDB ID is a 24-character hex string. The first 8 characters represent a Unix
# timestamp (in seconds) encoded as a base-16 integer.
# For example, "6a094b50bcf86cd799439011" has a timestamp of "6a094b50" in hex, which
# is 1778994000 in decimal, representing a creation time of "2026-05-17T05:00:00.000Z".
from datetime import UTC, datetime

from pytest import mark


def mongo_id_to_date(s: str) -> str:
    dt = datetime.fromtimestamp(int(s[:8], 16), tz=UTC)
    return dt.strftime('%Y-%m-%dT%H:%M:%S.000Z')


tests = [
    ('6a094b50bcf86cd799439011', '2026-05-17T05:00:00.000Z'),
    ('695344eb1f4a4c1123042128', '2025-12-30T03:20:11.000Z'),
    ('386da62df34123ac54617e56', '2000-01-01T07:01:01.000Z'),
    ('69f571c3d7711807afd3dd55', '2026-05-02T03:38:43.000Z'),
    ('68adce01c0e1144d0a90295a', '2025-08-26T15:08:49.000Z'),
]


def dt_to_mongo_id_prefix(dt: datetime) -> str:
    # Mongo ObjectId uses 4-byte (8 hex chars) big-endian timestamp
    ts = int(dt.timestamp())
    return f'{ts:08x}' + '0000000000000000'  # pad to 24 chars


def test_roundtrip_with_milliseconds() -> None:
    dt = datetime(2026, 5, 17, 5, 0, 0, 123456, tzinfo=UTC)

    oid = dt_to_mongo_id_prefix(dt)
    result = mongo_id_to_date(oid)

    assert result == '2026-05-17T05:00:00.000Z'


@mark.parametrize('s, expected', tests)
def test(s: str, expected: str) -> None:
    assert mongo_id_to_date(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(mongo_id_to_date(s))
