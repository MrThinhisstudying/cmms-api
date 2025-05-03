import os
import resend
from dotenv import load_dotenv

load_dotenv()

# Cấu hình API Key
resend.api_key = os.getenv("RESEND_API_KEY")

def send_otp_email(to_email: str, otp_code: str):
    try:
        print(f"📨 Đang gửi OTP tới: {to_email} - mã: {otp_code}")
        print("🔐 RESEND_API_KEY:", os.getenv("RESEND_API_KEY"))

        # Gửi email sử dụng Resend API
         # Nên dùng default hoặc domain đã xác minh
         # https://resend.com/docs/api-reference/emails/send-email  
         
        response = resend.Emails.send({
            "from": "onboarding@resend.dev",  # Nên dùng default hoặc domain đã xác minh
            "to": [to_email],
            "subject": "CMMS - Mã OTP đặt lại mật khẩu",
            "html": f"<p>Mã OTP của bạn là: <strong>{otp_code}</strong></p>"
        })

        print("✅ Gửi email thành công:", response)
        return response
    except Exception as e:
        print("❌ Lỗi khi gửi email:", str(e))
        raise
