import win32evtlog

server = "localhost"
log_type = "Security"

hand = win32evtlog.OpenEventLog(server, log_type)

flags = (
    win32evtlog.EVENTLOG_BACKWARDS_READ |
    win32evtlog.EVENTLOG_SEQUENTIAL_READ
)

events = win32evtlog.ReadEventLog(hand, flags, 0)

event = events[0]

print(dir(event))