import os
from http.server import BaseHTTPRequestHandler
from api.mailer import send_email
from api.generate_daily_focus import generate_daily_focus


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            goal = os.environ.get("GOAL")

            if not goal:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b"GOAL environment variable is not set")
                return

            focus = generate_daily_focus(goal)
            send_email(focus["subject"], focus["body"])

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Focus email sent")

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())
