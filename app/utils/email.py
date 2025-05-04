import os
import resend
from dotenv import load_dotenv

load_dotenv()

# Thiết lập API key
resend.api_key = os.getenv("RESEND_API_KEY")

def send_otp_email(to_email: str, otp_code: str):
    print(f"📨 Gửi tới: {to_email} - mã: {otp_code}")
    print(f"🔐 RESEND_API_KEY: {resend.api_key}")

    try:
        response = resend.Emails.send({
            "from": "onboarding@resend.dev",  # default sender
            "to": [to_email],
            "subject": "CMMS - Mã OTP đặt lại mật khẩu",
            "html": f"<p>Mã OTP của bạn là: <strong>{otp_code}</strong></p>"
        })
        print("✅ Đã gửi:", response)
    except Exception as e:
        print("❌ Lỗi khi gửi email:", type(e).__name__, "-", str(e))
        raise