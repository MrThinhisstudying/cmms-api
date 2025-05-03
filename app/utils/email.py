import os
import resend
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")
EMAIL_FROM = os.getenv("RESEND_EMAIL_FROM", "onboarding@resend.dev")

def send_otp_email(to_email: str, otp_code: str):
    subject = "CMMS - Mã OTP đặt lại mật khẩu"
    html_content = f"<p>Mã OTP của bạn là: <strong>{otp_code}</strong></p>"

    try:
        response = resend.Emails.send({
            "from": EMAIL_FROM,
            "to": [to_email],
            "subject": subject,
            "html": html_content
        })
        print(f"✅ Đã gửi OTP đến {to_email}: {otp_code}")
        return response
    except Exception as e:
        print(f"❌ Lỗi khi gửi email: {e}")
        raise
