import os
import resend
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")

def send_otp_email(to_email: str, otp_code: str):
    return resend.Emails.send({
        "from": "thinhtop869@gmail.com",  # Bạn có thể thay đổi nếu đã xác minh domain riêng
        "to": [to_email],
        "subject": "CMMS - Mã OTP đặt lại mật khẩu",
        "html": f"<p>Mã OTP của bạn là: <strong>{otp_code}</strong></p>"
    })
