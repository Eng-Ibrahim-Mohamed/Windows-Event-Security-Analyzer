def privilege_statistics(events):

    admin = 0

    for event in events:

        if event.event_id == 4672:

            admin += 1

    return {

        "admin_logins": admin

    }