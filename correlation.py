from datetime import datetime

from core.models import Alert
from core.utils.time_utils import minutes_between


WINDOW_MINUTES = 5


def detect_account_compromise(result):

    alerts = []

    failed_events = result.statistics.failed_events
    successful_events = result.statistics.successful_events

    for user in failed_events:

        if user not in successful_events:
            continue

        for success_event in successful_events[user]:

            recent_failed = []

            for failed_event in failed_events[user]:

                minutes = minutes_between(
                    failed_event.timestamp,
                    success_event.timestamp
                )

                if minutes <= WINDOW_MINUTES:
                    recent_failed.append(failed_event)

            if len(recent_failed) >= 3:

                alerts.append(

                    Alert(

                        title="Possible Account Compromise",

                        severity="CRITICAL",

                        username=user,

                        description=(
                            f"{len(recent_failed)} failed login attempts "
                            f"were followed by a successful login "
                            f"within {WINDOW_MINUTES} minutes."
                        ),

                        mitre="T1110 / T1078",

                        event_id=4624,

                        detection_time=success_event.timestamp,

                        risk="CRITICAL",

                        recommendation=(
                            "• Verify the user's identity.\n"
                            "• Review source IP addresses.\n"
                            "• Reset the password if the activity is unauthorized.\n"
                            "• Check for privilege escalation."
                        )

                    )

                )

                break

    return alerts