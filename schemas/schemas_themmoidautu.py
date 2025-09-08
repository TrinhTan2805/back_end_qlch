from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from decimal import Decimal  # để đồng bộ với Numeric trong SQLAlchemy

class ThemMoiDauTuBase(BaseModel):
    loaiTaiSan: Optional[str] = None
    loaiTien: Optional[str] = None
    soLuong: Optional[Decimal] = None
    donGia: Optional[Decimal] = None
    thue: Optional[Decimal] = None
    phi: Optional[Decimal] = None
    ghi_chu: Optional[str] = None
    ngay_nhap: Optional[datetime] = None
    soTien: Optional[Decimal] = None

class ThemMoiDauTuCreate(ThemMoiDauTuBase):
    pass

class ThemMoiDauTuUpdate(ThemMoiDauTuBase):
    pass

class ThemMoiDauTuResponse(ThemMoiDauTuBase):
    id: int

    class Config:
        from_attributes = True
