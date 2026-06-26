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

found = False

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

            found = True

            print("\nFAILED LOGIN FOUND")
            print("=" * 60)

            print("Time:")
            print(event.TimeGenerated)

            print("\nRaw Data:\n")

            if event.StringInserts:

                for item in event.StringInserts:

                    print(item)

            print("\n" + "=" * 60)

            exit()

if not found:

    print("No 4625 Events Found")