from sqlalchemy import Column, Integer, String, DateTime, Numeric, Sequence
from database.database import Base

class ThemMoiDauTu(Base):
    __tablename__ = "mua"

    id = Column(
        Integer,
        Sequence("mua_id_seq", start=1, increment=1),  # Tạo sequence trong Oracle
        primary_key=True
    )
    loaiTaiSan = Column(String(255))
    loaiTien = Column(String(50))
    soLuong = Column(Numeric(12, 2))
    donGia = Column(Numeric(12, 2))
    thue = Column(Numeric(12, 2))
    phi = Column(Numeric(12, 2))
    ghi_chu = Column(String(500))
    ngay_nhap = Column(DateTime)
    soTien = Column(Numeric(12, 2))
