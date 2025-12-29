import os
from mailer import send_email
from generate_daily_focus import generate_daily_focus


def handler(request):
    goal = os.environ.get("GOAL")

    if not goal:
        return {
            "statusCode": 500,
            "body": "GOAL environment variable is not set"
        }

    focus = generate_daily_focus(goal)
    send_email(focus["subject"], focus["body"])

    return {
        "statusCode": 200,
        "body": "Focus email sent"
    }
