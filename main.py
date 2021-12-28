import os
import random

import requests
from dotenv import load_dotenv

load_dotenv()
MAIL_GUN_API_KEY = os.getenv("MAIL_GUN_API_KEY")
MAILGUN_ENDPOINT = os.getenv("MAILGUN_ENDPOINT")
RECEIVER = os.getenv("RECEIVER")
SENDER = os.getenv("SENDER")


def send_simple_message(subject, text):
    return requests.post(
        f"{MAILGUN_ENDPOINT}/messages",
        auth=("api", MAIL_GUN_API_KEY),
        data={"from": SENDER,
              "to": [RECEIVER],
              "subject": subject,
              "text": text})


with open("quotes.txt") as f:
    # Randomly choose a motivational quote:
    quotes = f.readlines()
    mail_content = random.choice(quotes)

    send_simple_message(subject="Motivation for new day", text=mail_content)
