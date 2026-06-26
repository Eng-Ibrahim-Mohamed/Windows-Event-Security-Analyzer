import win32evtlog

server = "localhost"
log_type = "Security"

hand = win32evtlog.OpenEventLog(
    server,
    log_type
)

flags = (
    win32evtlog.EVENTLOG_BACKWARDS_READ |
    win32evtlog.EVENTLOG_SEQUENTIAL_READ
)

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

        if event_id == 4625:

            print("\nFAILED LOGIN")

            if event.StringInserts:

                for index, item in enumerate(
                    event.StringInserts
                ):

                    print(
                        f"{index}: {item}"
                    )

            exit()