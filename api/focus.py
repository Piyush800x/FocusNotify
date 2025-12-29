import os
from mailer import send_email
from generate_daily_focus import generate_daily_focus


def handler(request):
    GOAL = os.environ["GOAL"]

    focus = generate_daily_focus(GOAL)
    send_email(focus["subject"], focus["body"])

    return {
        "statusCode": 200,
        "body": "Focus email sent"
    }
