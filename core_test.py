from event_reader import read_security_events

events = read_security_events(limit=5)

for event in events:

    print("=" * 50)

    print("Event ID :", event.event_id)

    print("Name     :", event.event_name)

    print("User     :", event.username)

    print("IP       :", event.ip)

    print("Logon    :", event.logon_type)

    print("Status   :", event.status)

    print("Time     :", event.time)