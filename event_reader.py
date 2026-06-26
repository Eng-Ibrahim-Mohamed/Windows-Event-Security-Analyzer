import win32evtlog


def read_security_events(limit=200):

    server = "localhost"
    log_type = "Security"

    events_data = []

    hand = win32evtlog.OpenEventLog(
        server,
        log_type
    )

    flags = (
        win32evtlog.EVENTLOG_BACKWARDS_READ |
        win32evtlog.EVENTLOG_SEQUENTIAL_READ
    )

    count = 0

    while True:

        events = win32evtlog.ReadEventLog(
            hand,
            flags,
            0
        )

        if not events:
            break

        for event in events:

            event_id = event.EventID & 0xFFFF

            events_data.append({
                "event_id": event_id,
                "time": str(event.TimeGenerated),
                "data": event.StringInserts
            })

            count += 1

            if count >= limit:
                return events_data

    return events_data