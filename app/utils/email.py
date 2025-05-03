import os
from resend import Resend
from dotenv import load_dotenv

load_dotenv()

resend = Resend(api_key=os.getenv("RESEND_API_KEY"))

def send_otp_email(to_email: str, otp_code: str):
    subject = "CMMS - Mã OTP đặt lại mật khẩu"
    body = f"Mã OTP của bạn là: {otp_code}"
    resend.emails.send({
        "from": "onboarding@resend.dev",  # Bạn có thể thay bằng domain riêng sau
        "to": [to_email],
        "subject": subject,
        "text": body,
    })
