from datetime import datetime


def generate_daily_focus(goal: str) -> dict:
    """
    Generates a strict, single-goal career focus message.
    """

    today = datetime.now().strftime("%A, %d %B %Y")

    message = f"""
        Good morning.

        Date: {today}

        Your ONLY career focus today:

        → {goal}

        Rules for today:
        • Say NO to tasks that do not support this goal
        • Spend at least 90 minutes in deep work
        • Avoid social media before completing progress

        Ask yourself tonight:
        "Did my actions move me closer to this goal?"

        Stay disciplined.
        """

    subject = "Daily Career Focus"

    return {
        "subject": subject,
        "body": message.strip()
    }
