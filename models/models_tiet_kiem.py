from sqlalchemy import Column, Integer, String, Double, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from models.base import Base



class TietKiem(Base):
    __tablename__ = "tiet_kiem"

    _id = Column(Integer, primary_key=True, index=True)
    nhom = Column(String)
    ghi_chu = Column(String)
    ngay_nhap = Column(TIMESTAMP)
    so_tien = Column(Double)

