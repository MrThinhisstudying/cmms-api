from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models, database
from app.utils.email import send_otp_email
from passlib.context import CryptContext
import jwt, os, random
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("SECRET_KEY", "secret")
ALGORITHM = "HS256"

import bcrypt
hashed = b"$2b$12$xL6UyTpJvFdhhXfrcCOD6eRot2OYYa..."  # từ DB
print(bcrypt.checkpw(b"12345678", hashed))
# DB Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Hashing
def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

# Token
def create_token(user_id: int):
    payload = {
        "sub": str(user_id),
        "exp": datetime.utcnow() + timedelta(days=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

# Login
@router.post("/login")
def login(data: schemas.LoginSchema, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Sai email hoặc mật khẩu")
    token = create_token(user.id)
    return {"access_token": token}

# Quên mật khẩu
@router.post("/forgot-password")
def forgot_password(data: schemas.ForgotPassword, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Email không tồn tại")
    otp = str(random.randint(100000, 999999))
    user.otp_code = otp
    db.commit()
    send_otp_email(user.email, otp)
    return {"message": "OTP đã được gửi qua email"}

# Đặt lại mật khẩu
@router.post("/reset-password")
def reset_password(data: schemas.ResetPassword, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user or user.otp_code != data.otp_code:
        raise HTTPException(status_code=400, detail="OTP không hợp lệ")
    user.hashed_password = hash_password(data.new_password)
    user.otp_code = None
    db.commit()
    return {"message": "Mật khẩu đã được cập nhật"}
