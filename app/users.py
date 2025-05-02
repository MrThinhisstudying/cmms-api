from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, models, database
from app.utils.auth_utils import get_current_user
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

# Role check
def require_admin(current_user: models.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Chỉ admin mới có quyền thực hiện thao tác này"
        )
    return current_user

# Tạo người dùng mới (chỉ admin)
@router.post("/users", response_model=schemas.UserOut)
def create_user(
    data: schemas.UserCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_admin)
):
    if db.query(models.User).filter(models.User.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email đã tồn tại")
    hashed_password = pwd_context.hash(data.password)
    user = models.User(
        email=data.email,
        full_name=data.full_name,
        hashed_password=hashed_password,
        role=data.role,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Lấy danh sách tất cả người dùng
@router.get("/users", response_model=list[schemas.UserOut])
def get_users(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_admin)
):
    return db.query(models.User).all()

# Xóa người dùng theo ID
@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_admin)
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Không tìm thấy user")
    db.delete(user)
    db.commit()
    return {"message": "Đã xóa user"}
