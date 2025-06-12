from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class GiaoDichBase(BaseModel):
    id: Optional[int] = None
    nhom: Optional[str] = None
    ghi_chu: Optional[str] = None
    ngay_nhap: Optional[datetime] = None
    so_tien: Optional[float] = None

class GiaoDichCreate(GiaoDichBase):
    pass

class GiaoDichUpdate(GiaoDichBase):
    pass

class GiaoDichResponse(GiaoDichBase):
    _id: int

    class Config:
        from_attributes = True
