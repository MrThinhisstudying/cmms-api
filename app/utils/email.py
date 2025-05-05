import smtplib
import ssl
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")  # Gmail của bạn
EMAIL_PASSWORD = os.getenv("EMAIL_PASS")  # App Password (16 ký tự)

def send_otp_email(to_email: str, otp_code: str):
    msg = EmailMessage()
    msg['Subject'] = "CMMS - Mã OTP đặt lại mật khẩu"
    msg['From'] = EMAIL_USER
    msg['To'] = to_email
    msg.set_content(f"Mã OTP của bạn là: {otp_code}")

    print(f"📨 Gửi OTP tới: {to_email} - mã: {otp_code}")
    print(f"📤 Gửi từ: {EMAIL_USER}")

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("✅ Email đã được gửi thành công")
    except Exception as e:
        print("❌ Lỗi gửi email:", str(e))