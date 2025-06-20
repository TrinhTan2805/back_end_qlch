from sqlalchemy import Column, Integer, String, Double, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from models.base import Base

class TienNo(Base):
    __tablename__ = "tien_no"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    ghi_chu = Column(String)
    ngay_nhap = Column(TIMESTAMP)
    tong_so_tien_vay_no = Column(Integer)