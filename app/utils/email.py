import os
import resend
from dotenv import load_dotenv

load_dotenv()

# Cấu hình API Key
resend.api_key = os.getenv("RESEND_API_KEY")

def send_otp_email(to_email: str, otp_code: str):
    import resend
    import os

    resend.api_key = os.getenv("RESEND_API_KEY")
    print(f"🔐 RESEND_API_KEY: {resend.api_key}")
    print(f"📨 Gửi tới: {to_email} - mã: {otp_code}")

    try:
        response = resend.Emails.send({
            "from": "onboarding@resend.dev",  # ✅ sender được Resend cho phép mặc định
            "to": [to_email],
            "subject": "CMMS - Mã OTP đặt lại mật khẩu",
            "html": f"<p>Mã OTP của bạn là: <strong>{otp_code}</strong></p>"
        })
        print("✅ Đã gửi:", response)
    except Exception as e:
        print("❌ Gửi lỗi:", str(e))

