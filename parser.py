from core.models import SecurityEvent


def parse_event(event):

    event_id = event["event_id"]
    data = event["data"]
    time = event["time"]

    if not data:
        return None

    if event_id == 4625:

        return SecurityEvent(

            event_id=4625,

            event_name="Failed Login",

            time=time,

            username=data[5],

            ip=data[19],

            logon_type=data[10],

            status=data[7]

        )

    elif event_id == 4624:

        ip = "-"

        if len(data) > 18:
            ip = data[18]

        return SecurityEvent(

            event_id=4624,

            event_name="Successful Login",

            time=time,

            username=data[5],

            ip=ip,

            logon_type=data[8],

            status="SUCCESS"

        )

    elif event_id == 4672:

        return SecurityEvent(

            event_id=4672,

            event_name="Admin Login",

            time=time,

            username=data[5],

            ip="-",

            logon_type="-",

            status="SUCCESS"

        )

    return None