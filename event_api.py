import win32evtlog


class EventAPI:

    def __init__(self):

        self.channel = "Security"

        self.query = """
        *[
            System[
                (
                    EventID=4624
                    or
                    EventID=4625
                    or
                    EventID=4672
                )
            ]
        ]
        """

    def read_events(self, limit=100):

        handle = win32evtlog.EvtQuery(

            self.channel,

            win32evtlog.EvtQueryReverseDirection,

            self.query

        )

        events = []

        while len(events) < limit:

            batch = win32evtlog.EvtNext(

                handle,

                10

            )

            if not batch:

                break

            events.extend(batch)

        return events[:limit]