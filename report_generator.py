from alerts import generate_alerts
from recommendations import generate_recommendations
from datetime import datetime


def generate_report(results):

    alerts = generate_alerts(results)

    recommendations = generate_recommendations(results)

    report_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    total_events = (
        results["failed_logins"] +
        results["successful_logins"] +
        results["admin_logins"]
    )

    if len(alerts) > 0:

        overall_risk = "HIGH"

    elif results["admin_logins"] > 20:

        overall_risk = "MEDIUM"

    else:

        overall_risk = "LOW"

    report = f"""
==================================================
          WINDOWS SECURITY REPORT
                 Version 1.1
==================================================

EXECUTIVE SUMMARY

Overall Risk      : {overall_risk}

Events Analysed   : {total_events}

Alerts Generated  : {len(alerts)}

Report Generated  : {report_time}

==================================================

SECURITY STATISTICS

Failed Logins      : {results['failed_logins']}

Successful Logins  : {results['successful_logins']}

Admin Logins       : {results['admin_logins']}

==================================================

TARGET USERS

"""

    if not results["failed_users"]:

        report += "No Failed Login Attempts Found\n"

    else:

        for user, attempts in results["failed_users"].items():

            report += (
                f"{user} -> "
                f"{attempts} Attempts\n"
            )

    report += "\n"

    report += (
        "==================================================\n\n"
    )

    report += "SECURITY ALERTS\n\n"

    if len(alerts) == 0:

        report += "No Active Alerts\n"

    else:

        for alert in alerts:

            report += (
                f"[{alert['severity']}]\n\n"

                f"{alert['title']}\n\n"

                f"Target User : {alert['target_user']}\n"

                f"Source IP   : {alert['source_ip']}\n"

                f"Logon Type  : {alert['logon_type']}\n"

                f"Attempts    : {alert['attempts']}\n\n"

                "Status      : OPEN\n"

                "\n------------------------------------------\n\n"
            )

    report += (
        "\n==================================================\n\n"
    )

    report += "RECOMMENDATIONS\n\n"

    for recommendation in recommendations:

        report += (
            f"• {recommendation}\n"
        )

    report += (
        "\n==================================================\n"
    )

    return report