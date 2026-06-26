def generate_recommendations(results):

    recommendations = []

    if results["failed_logins"] >= 3:

        recommendations.append(
            "Review failed login attempts for suspicious activity."
        )

        recommendations.append(
            "Verify the affected user account."
        )

        recommendations.append(
            "Enable Account Lockout Policy if it is disabled."
        )

        recommendations.append(
            "Change the password if compromise is suspected."
        )

    if results["admin_logins"] > 20:

        recommendations.append(
            "Review privileged logon events."
        )

        recommendations.append(
            "Verify administrator activity."
        )

    if len(recommendations) == 0:

        recommendations.append(
            "No security recommendations at this time."
        )

    return recommendations