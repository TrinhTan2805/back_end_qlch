from sqlalchemy import Column, Integer, String, Float, TIMESTAMP
from models.base import Base  # Bạn đã dùng Base tự định nghĩa trong project

class TraNo(Base):
    __tablename__ = "tra_no"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    ghi_chu = Column(String)
    ngay_nhap = Column(TIMESTAMP)
    so_tien_tra_no = Column(Integer)  # hoặc Float nếu muốn hỗ trợ số lẻ
