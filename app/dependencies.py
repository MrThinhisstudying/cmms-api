from fastapi import Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from app import models, database
import jwt, os
from dotenv import load_dotenv
from app.dependencies import get_current_user
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "secret")
ALGORITHM = "HS256"

# Lấy DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Lấy user từ token
def get_current_user(request: Request, db: Session = Depends(get_db)):
    auth = request.headers.get("Authorization")
    if not auth or not auth.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Thiếu token")

    token = auth.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get("sub"))
    except:
        raise HTTPException(status_code=401, detail="Token không hợp lệ")

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User không tồn tại")

    return user

# Yêu cầu vai trò cụ thể
def require_role(required_role: str):
    def checker(current_user=Depends(get_current_user)):
        if current_user.role != required_role:
            raise HTTPException(status_code=403, detail=f"Yêu cầu vai trò '{required_role}'")
        return current_user
    return checker