from datetime import datetime


def parse_timestamp(timestamp: str):

    # Remove trailing Z
    timestamp = timestamp.rstrip("Z")

    # Split date/time and fractional seconds
    if "." in timestamp:

        base, fraction = timestamp.split(".")

        # Python supports only 6 digits
        fraction = fraction[:6]

        timestamp = f"{base}.{fraction}"

        return datetime.strptime(
            timestamp,
            "%Y-%m-%dT%H:%M:%S.%f"
        )

    return datetime.strptime(
        timestamp,
        "%Y-%m-%dT%H:%M:%S"
    )


def minutes_between(start: str, end: str):

    start_time = parse_timestamp(start)

    end_time = parse_timestamp(end)

    return abs(
        (end_time - start_time).total_seconds()
    ) / 60