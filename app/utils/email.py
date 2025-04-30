import smtplib, ssl, os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_otp_email(to_email: str, otp_code: str):
    msg = EmailMessage()
    msg['Subject'] = "CMMS - Mã OTP đặt lại mật khẩu"
    msg['From'] = EMAIL_USER
    msg['To'] = to_email
    msg.set_content(f"Mã OTP của bạn là: {otp_code}")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASSWORD)
        smtp.send_message(msg)
