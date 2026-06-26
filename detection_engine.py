from core.models import Statistics
from core.models import DetectionResult

from core.rules.authentication import authentication_statistics
from core.rules.privilege import privilege_statistics


class DetectionEngine:

    def __init__(self, events):

        self.events = events

    def analyze(self):

        auth = authentication_statistics(self.events)

        privilege = privilege_statistics(self.events)

        statistics = Statistics(

    	     failed_logins=auth["failed_logins"],

                 successful_logins=auth["successful_logins"],

                  admin_logins=privilege["admin_logins"],

                  failed_users=auth["failed_users"],

                  failed_events=auth["failed_events"],

                  successful_events=auth["successful_events"]

        )

        return DetectionResult(

            statistics=statistics,

            alerts=[],

            events=self.events

        )