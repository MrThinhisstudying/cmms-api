from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:Acv%402022@localhost:5432/cmms_db")
# print(f"✅ DATABASE_URL = '{DATABASE_URL}'")  # Có dấu nháy đơn để kiểm tra khoảng trắng
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
