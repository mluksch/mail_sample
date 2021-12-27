import os
import random
import smtplib
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()
USER = os.getenv("USER")
PASS = os.getenv("PASS")
receiver = os.getenv("RECEIVER")
sender = os.getenv("SENDER")

with smtplib.SMTP(port=587, host="smtp.mail.yahoo.com") as server_con, open("quotes.txt") as f:
    # Randomly choose a motivational quote:
    quotes = f.readlines()
    mail_content = random.choice(quotes)

    # Create a (Mime-Text-Protocol conform) Mail-Message
    msg = MIMEText(mail_content, "plain", "utf-8")
    msg["Subject"] = "Motivation for new day"
    msg["From"] = sender
    msg["To"] = receiver

    # Encrypt mail
    server_con.starttls()

    # Login to Mail-Server
    server_con.login(user=USER, password=PASS)

    # Send mail
    server_con.sendmail(sender, receiver,
                        msg.as_string())
