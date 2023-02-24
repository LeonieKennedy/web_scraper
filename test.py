from datetime import datetime, time, timedelta
from random import randrange
f

PROMPT = 'Please enter a {} time in ISO format: '


def read_time(prompt: str) -> time:
    """Reads a time object from the user."""

    return time.fromisoformat(input(prompt))


def rand_datetime(start: datetime, end: datetime) -> datetime:
    """Returns a random datetime between start and end."""

    return datetime.fromtimestamp(randrange(
        round(start.timestamp()), round(end.timestamp())
    ))


def rand_time(start: time, end: time) -> time:
    """Returns a random time between start and end."""

    return rand_datetime(
        datetime.combine(dt0 := datetime.fromtimestamp(0), start),
        datetime.combine(
            dt0 if start < end else dt0 + timedelta(days=1),
            end
        )
    ).time()


def main(in_s, in_e):
    """Runs the script."""

    start = read_time(in_s)
    end = read_time(in_e)
    rand = rand_time(start, end)
    return rand
