from dataclasses import dataclass, field


# ==================================================
# Security Event
# ==================================================

@dataclass
class SecurityEvent:

    event_id: int
    event_name: str
    timestamp: str
    username: str
    domain: str
    ip_address: str
    logon_type: str
    status: str
    authentication_package: str
    raw_fields: dict = field(default_factory=dict)

    def __str__(self):

        return f"""
==================================================
              WINDOWS SECURITY EVENT
==================================================

Event ID            : {self.event_id}

Event Name          : {self.event_name}

Timestamp           : {self.timestamp}

Username            : {self.username}

Domain              : {self.domain}

IP Address          : {self.ip_address}

Logon Type          : {self.logon_type}

Status              : {self.status}

Authentication      : {self.authentication_package}

==================================================
"""

    def to_dict(self):

        return {
            "event_id": self.event_id,
            "event_name": self.event_name,
            "timestamp": self.timestamp,
            "username": self.username,
            "domain": self.domain,
            "ip_address": self.ip_address,
            "logon_type": self.logon_type,
            "status": self.status,
            "authentication_package": self.authentication_package,
            "raw_fields": self.raw_fields
        }


# ==================================================
# Statistics
# ==================================================

@dataclass
class Statistics:

    failed_logins: int

    successful_logins: int

    admin_logins: int

    failed_users: dict

    failed_events: dict = field(default_factory=dict)

    successful_events: dict = field(default_factory=dict)

# ==================================================
# Alert
# ==================================================

@dataclass
class Alert:

    title: str

    severity: str

    username: str

    description: str

    mitre: str

    event_id: int

    detection_time: str

    risk: str

    recommendation: str

    def __str__(self):

        return f"""
==================================================
                 SECURITY ALERT
==================================================

Title              : {self.title}

Severity           : {self.severity}

Risk Level         : {self.risk}

MITRE ATT&CK       : {self.mitre}

Event ID           : {self.event_id}

Detection Time     : {self.detection_time}

Affected User      : {self.username}

Description
--------------------------------------------------
{self.description}

Recommended Action
--------------------------------------------------
{self.recommendation}

==================================================
"""

# ==================================================
# Detection Result
# ==================================================

@dataclass
class DetectionResult:

    statistics: Statistics

    alerts: list = field(default_factory=list)

    events: list = field(default_factory=list)

    def __str__(self):

        report = f"""
==================================================
              DETECTION RESULTS
==================================================

Failed Logins      : {self.statistics.failed_logins}

Successful Logins  : {self.statistics.successful_logins}

Admin Logins       : {self.statistics.admin_logins}

==================================================

Failed Users
--------------------------------------------------
"""

        if not self.statistics.failed_users:

            report += "\nNo Failed Users Found\n"

        else:

            for user, count in self.statistics.failed_users.items():

                report += f"\n{user} : {count}"

        return report