from app.database import SessionLocal
from app.models import User
from passlib.context import CryptContext
from dotenv import load_dotenv
load_dotenv()
db = SessionLocal()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
from app.database import engine
print("✅ Connected to:", engine.url)
# Dữ liệu admin
email = "kythuatvcs@gmail.com   "
password = "12345678"
full_name = "Kỹ Thuật VCS"

# Kiểm tra user tồn tại
existing_user = db.query(User).filter(User.email == email).first()

if existing_user:
    print("⚠️ Admin đã tồn tại.")
else:
    hashed_pw = pwd_context.hash(password)
    user = User(
        email=email,
        full_name=full_name,
        hashed_password=hashed_pw,
        role="admin"
    )
    db.add(user)
    db.commit()
    print("✅ Tạo admin thành công.")
