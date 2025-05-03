import os
import resend
from dotenv import load_dotenv

load_dotenv()
resend.api_key = os.getenv("RESEND_API_KEY")

def send_otp_email(to_email: str, otp_code: str):
    from resend import Emails
    import os
    resend.api_key = os.getenv("RESEND_API_KEY")
    
    try:
        response = Emails.send({
            "from": "onboarding@resend.dev",
            "to": [to_email],
            "subject": "CMMS - Mã OTP đặt lại mật khẩu",
            "html": f"<p>Mã OTP của bạn là: <strong>{otp_code}</strong></p>"
        })
        print("✅ Đã gửi:", response)
        return response  # <- để log thấy rõ
    except Exception as e:
        print("❌ Gửi lỗi:", str(e))
        raise e

    print(f"🔐 RESEND_API_KEY: {resend.api_key}")
    print(f"📨 Gửi tới: {to_email} - mã: {otp_code}")

    try:
        response = resend.Emails.send({
            "from": "onboarding@resend.dev",  # ✅ sender mặc định được phép
            "to": [to_email],
            "subject": "CMMS - Mã OTP đặt lại mật khẩu",
            "html": f"<p>Mã OTP của bạn là: <strong>{otp_code}</strong></p>"
        })
        print("✅ Đã gửi:", response)
    except Exception as e:
        print("❌ Gửi lỗi:", str(e))
