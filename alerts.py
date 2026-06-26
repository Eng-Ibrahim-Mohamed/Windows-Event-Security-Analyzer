def generate_alerts(results):

    alerts = []

    for user, attempts in results["failed_users"].items():

        if attempts >= 3:

            details = results["user_details"][user]

            logon_type = details["logon_type"]

            if logon_type == "2":
                logon_type = "Interactive Login"

            elif logon_type == "3":
                logon_type = "Network Login"

            elif logon_type == "10":
                logon_type = "Remote Desktop"

            alerts.append({

                "title": "BRUTE FORCE DETECTED",

                "severity": "HIGH",

                "target_user": user,

                "attempts": attempts,

                "source_ip": details["ip"],

                "logon_type": logon_type

            })

    return alerts