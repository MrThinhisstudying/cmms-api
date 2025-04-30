from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models, database
from app.auth_utils import get_current_user, require_role
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# DB Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Chỉ cho admin
def require_admin(user=Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Chỉ admin được phép")
    return user

# Tạo user mới
@router.post("/users", response_model=schemas.UserOut)
def create_user(data: schemas.UserCreate, db: Session = Depends(get_db), admin=Depends(require_admin)):
    if db.query(models.User).filter(models.User.email == data.email).first():
        raise HTTPException(400, detail="Email đã tồn tại")
    user = models.User(
        email=data.email,
        full_name=data.full_name,
        hashed_password=pwd_context.hash(data.password),
        role=data.role,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Lấy tất cả người dùng
@router.get("/users", response_model=list[schemas.UserOut])
def get_users(db: Session = Depends(get_db), admin=Depends(require_admin)):
    return db.query(models.User).all()

# Xóa user
@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), admin=Depends(require_admin)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(404, detail="Không tìm thấy user")
    db.delete(user)
    db.commit()
    return {"message": "Đã xóa user"}
