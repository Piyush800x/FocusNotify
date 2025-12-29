import smtplib
from email.message import EmailMessage
import os


def send_email(subject: str, body: str):
    msg = EmailMessage()
    msg["From"] = os.environ["EMAIL_FROM"]
    msg["To"] = os.environ["EMAIL_TO"]
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL(os.environ["SMTP_HOST"], 465) as server:
        server.login(
            os.environ["SMTP_USER"],
            os.environ["SMTP_PASS"]
        )
        server.send_message(msg)
