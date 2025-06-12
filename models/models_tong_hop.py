from sqlalchemy import Column, BigInteger, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TongHopGiaoDichView(Base):
    __tablename__ = "tong_hop_giao_dich_thu_nhap_tiet_kiem_2025"
    __table_args__ = {"extend_existing": True}

    id = Column(BigInteger, primary_key=True)
    thang = Column(Integer)
    nam = Column(Integer)
    tong_giao_dich = Column(Integer)
    tong_thu_nhap = Column(Integer)
    tong_tiet_kiem = Column(Integer)
