from pydantic import BaseModel, EmailStr
from enum import Enum
class EquipmentBase(BaseModel):
    name: str
    code: str
    location: str
    status: str

class EquipmentCreate(EquipmentBase):
    pass

class Equipment(EquipmentBase):
    id: int

    class Config:
        from_attributes = True

class RoleEnum(str, Enum):
    nhan_vien = "nhân viên"
    quan_ly = "quản lý"
    ky_thuat = "kỹ thuật"
    admin = "admin"

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    role: RoleEnum = RoleEnum.nhan_vien  # mặc định là "nhân viên"

class UserCreate(UserBase):
    password: str
    role: RoleEnum = RoleEnum.nhan_vien  # mặc định là "nhân viên"
class UserOut(UserBase):
    id: int
    role: RoleEnum
    class Config:
        from_attributes = True

class LoginSchema(BaseModel):
    email: EmailStr
    password: str

class ForgotPassword(BaseModel):
    email: EmailStr

class ResetPassword(BaseModel):
    email: EmailStr
    otp_code: str
    new_password: str