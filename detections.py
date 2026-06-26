def analyze_events(events):

    failed_logins = 0
    successful_logins = 0
    admin_logins = 0

    failed_users = {}
    user_details = {}

    for event in events:

        event_id = event["event_id"]

        data = event["data"]

        if event_id == 4625:

            failed_logins += 1

            if data:

                username = data[5]
                source_ip = data[19]
                logon_type = data[10]

                if username not in failed_users:
                    failed_users[username] = 0

                failed_users[username] += 1

                user_details[username] = {
                    "ip": source_ip,
                    "logon_type": logon_type
                }

        elif event_id == 4624:

            successful_logins += 1

        elif event_id == 4672:

            admin_logins += 1

    return {
        "failed_logins": failed_logins,
        "successful_logins": successful_logins,
        "admin_logins": admin_logins,
        "failed_users": failed_users,
        "user_details": user_details
    }