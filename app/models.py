from sqlalchemy import Column, Integer, String
from .database import Base

class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    code = Column(String, unique=True, index=True)
    location = Column(String)
    status = Column(String)
