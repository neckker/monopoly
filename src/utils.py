from datetime import datetime, timezone


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def tmsnow() -> int:
    return int(utcnow().timestamp())
