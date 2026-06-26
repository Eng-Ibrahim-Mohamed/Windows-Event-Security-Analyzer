from collections import Counter
from collections import defaultdict


def authentication_statistics(events):

    failed = 0
    success = 0

    failed_users = Counter()

    failed_events = defaultdict(list)
    successful_events = defaultdict(list)

    for event in events:

        if event.event_id == 4625:

            failed += 1

            failed_users[event.username] += 1

            failed_events[event.username].append(event)

        elif event.event_id == 4624:

            success += 1

            successful_events[event.username].append(event)

    return {

        "failed_logins": failed,

        "successful_logins": success,

        "failed_users": dict(failed_users),

        "failed_events": dict(failed_events),

        "successful_events": dict(successful_events)

    }