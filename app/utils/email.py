import os
from resend import Emails
from dotenv import load_dotenv

load_dotenv()

# Thiết lập API key
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
Emails.api_key = RESEND_API_KEY

def send_otp_email(to_email: str, otp_code: str):
    print(f"📨 Gửi tới: {to_email} - mã: {otp_code}")
    print(f"🔐 RESEND_API_KEY: {RESEND_API_KEY}")
    try:
        response = Emails.send({
            "from": "onboarding@resend.dev",  # bắt buộc là email hợp lệ từ Resend
            "to": [to_email],
            "subject": "CMMS - Mã OTP đặt lại mật khẩu",
            "html": f"<p>Mã OTP của bạn là: <strong>{otp_code}</strong></p>"
        })
        print("✅ Email gửi thành công:", response)
        return response
    except Exception as e:
        print("❌ Gửi lỗi:", e)
        raise
