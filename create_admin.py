from app.database import SessionLocal
from app.models import User
from passlib.context import CryptContext

db = SessionLocal()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Cấu hình tài khoản admin
email = "kythuatvcs@cmms.com"
password = "acvvcs2025"
full_name = "Kỹ Thuật VCS"

# Kiểm tra tồn tại
existing = db.query(User).filter(User.email == email).first()
if existing:
    print("⚠️ Admin đã tồn tại.")
else:
    user = User(
        email=email,
        full_name=full_name,
        hashed_password=pwd_context.hash(password),
        role="admin"
    )
    db.add(user)
    db.commit()
    print("✅ Đã tạo tài khoản admin thành công.")
