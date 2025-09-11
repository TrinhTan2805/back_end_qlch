from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from decimal import Decimal  # đồng bộ với Numeric trong SQLAlchemy

class ThemMoiDauTuBase(BaseModel):
    loaiTaiSan: Optional[str] = None
    loaiTien: Optional[str] = None
    soLuong: Optional[Decimal] = None
    donGia: Optional[Decimal] = None
    ghi_chu: Optional[str] = None
    ngay_nhap: Optional[datetime] = None
    soTien: Optional[Decimal] = None
    tinh_trang: Optional[int] = None   # dùng int cho NUMBER(1,0)

class ThemMoiDauTuCreate(ThemMoiDauTuBase):
    pass

class ThemMoiDauTuUpdate(ThemMoiDauTuBase):
    pass

class ThemMoiDauTuResponse(ThemMoiDauTuBase):
    id: int

    class Config:
        from_attributes = True  # cho phép ORM mapping
