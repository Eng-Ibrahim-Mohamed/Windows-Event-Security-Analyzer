from core.rules.correlation import detect_account_compromise


class CorrelationEngine:

    def __init__(self, detection_result):

        self.result = detection_result

    def analyze(self):

        alerts = []

        alerts.extend(

            detect_account_compromise(

                self.result

            )

        )

        return alerts