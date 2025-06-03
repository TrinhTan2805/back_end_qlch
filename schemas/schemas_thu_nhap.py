from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ThuNhapBase(BaseModel):
    nhom: Optional[str] = None
    ghi_chu: Optional[str] = None
    ngay_nhap: Optional[datetime] = None
    so_tien: Optional[float] = None

class ThuNhapCreate(ThuNhapBase):
    pass

class ThuNhapUpdate(ThuNhapBase):
    pass

class ThuNhapResponse(ThuNhapBase):
    _id: int

    class Config:
        from_attributes = True
