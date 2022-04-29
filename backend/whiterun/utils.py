from datetime import datetime, timezone


def now_timestamp() -> int:
    return int(datetime.now(tz=timezone.utc).timestamp())
