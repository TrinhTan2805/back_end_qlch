from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from database.database import Base

class DanhMuc(Base):
    __tablename__ = "danh_muc"

    id = Column(Integer, primary_key=True, index=True)
    ten_danh_muc = Column(String, unique=True, index=True)
