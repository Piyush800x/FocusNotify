import os
from mailer import send_email
from generate_daily_focus import generate_daily_focus
import traceback


def handler(request):
    try:
        goal = os.environ.get("GOAL")

        focus = generate_daily_focus(goal)
        send_email(focus["subject"], focus["body"])

        return {
            "statusCode": 200,
            "body": "Focus email sent"
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": traceback.format_exc()
        }
