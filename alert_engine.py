from datetime import datetime

from core.models import Alert


class AlertEngine:

    def __init__(self, detection_result):

        self.result = detection_result

    def generate(self):

        alerts = []

        for user, attempts in self.result.statistics.failed_users.items():

            if attempts >= 3:

                alerts.append(

                    Alert(

                        title="Possible Brute Force Attack",

                        severity="HIGH",

                        username=user,

                        description=(
                            f"Multiple failed login attempts "
                            f"({attempts}) were detected "
                            f"for user '{user}'."
                        ),

                        mitre="T1110 - Brute Force",

                        event_id=4625,

                        detection_time=datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        ),

                        risk="HIGH",

                        recommendation=(
                            "• Verify the user's identity.\n"
                            "• Review recent login history.\n"
                            "• Reset the password if the activity is unauthorized.\n"
                            "• Investigate the source IP address."
                        )

                    )

                )

        return alerts