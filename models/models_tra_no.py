from sqlalchemy import Column, Integer, String, Double, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from models.base import Base

class TraNo(Base):
    __tablename__ = "tra_no"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    ghi_chu = Column(String)
    ngay_nhap = Column(TIMESTAMP)
    so_tien_tra_no = Column(Integer)