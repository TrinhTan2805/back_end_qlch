from sqlalchemy import Column, Integer, String, DateTime, Numeric, Sequence
from database.database import Base

class ThemMoiDauTu(Base):
    __tablename__ = "mua"

    id = Column(
        Integer,
        Sequence("mua_id_seq", start=1, increment=1),
        primary_key=True
    )
    loaiTaiSan = Column("loaiTaiSan", String(255))
    loaiTien = Column("loaiTien", String(50))
    soLuong = Column("soLuong", Numeric(12, 2))        # ✅ fix
    donGia = Column("donGia", Numeric(12, 2))          # ✅ fix
    ghi_chu = Column("GHI_CHU", String(500))           # DB đang uppercase
    ngay_nhap = Column("NGAY_NHAP", DateTime)          # DB đang uppercase
    soTien = Column("soTien", Numeric(12, 2))          # ✅ fix
    tinhTrang = Column("TINHTRANG", Numeric(1, 0))     # DB đang uppercase
