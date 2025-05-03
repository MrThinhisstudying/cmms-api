import os
import resend
from fastapi import FastAPI
from typing import Dict

resend.api_key = os.environ["RESEND_API_KEY"]

app = FastAPI()

@app.post("/send-email")
def send_email() -> Dict:
    params = {
        "from": "onboarding@resend.dev",
        "to": ["thinhtop869@gmail.com"],
        "subject": "Hello World",
        "html": "<strong>It works!</strong>",
    }
    email = resend.Emails.send(params)
    return email
