from sqlalchemy import Column, Integer, String
from database.database import Base

class Nhom(Base):
    __tablename__ = "nhom"
    id = Column(Integer, primary_key=True, index=True)
    ten_nhom = Column(String, unique=True, index=True)
