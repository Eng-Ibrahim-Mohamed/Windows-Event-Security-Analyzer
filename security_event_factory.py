from core.models import SecurityEvent


LOGON_TYPES = {
    "2": "Interactive",
    "3": "Network",
    "4": "Batch",
    "5": "Service",
    "7": "Unlock",
    "8": "NetworkCleartext",
    "9": "NewCredentials",
    "10": "RemoteInteractive",
    "11": "CachedInteractive"
}


EVENT_NAMES = {
    4624: "Successful Login",
    4625: "Failed Login",
    4672: "Special Privileges Assigned"
}


def create_security_event(parsed_event):

    event_id = parsed_event["event_id"]

    fields = parsed_event["fields"]

    return SecurityEvent(

        event_id=event_id,

        event_name=EVENT_NAMES.get(
            event_id,
            "Unknown Event"
        ),

        timestamp=parsed_event["timestamp"],

        username=fields.get(
            "TargetUserName",
            fields.get(
                "SubjectUserName",
                "Unknown"
            )
        ),

        domain=fields.get(
            "TargetDomainName",
            fields.get(
                "SubjectDomainName",
                "-"
            )
        ),

        ip_address=fields.get(
            "IpAddress",
            "-"
        ),

        logon_type=LOGON_TYPES.get(
            fields.get(
                "LogonType",
                ""
            ),
            fields.get(
                "LogonType",
                "-"
            )
        ),

        status=fields.get(
            "Status",
            "SUCCESS"
        ),

        authentication_package=fields.get(
            "AuthenticationPackageName",
            "-"
        ),

        raw_fields=fields

    )