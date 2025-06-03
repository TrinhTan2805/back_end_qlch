from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TietKiemBase(BaseModel):
    nhom: Optional[str] = None
    ghi_chu: Optional[str] = None
    ngay_nhap: Optional[datetime] = None
    so_tien: Optional[float] = None

class TietKiemCreate(TietKiemBase):
    pass

class TietKiemUpdate(TietKiemBase):
    pass

class TietKiemResponse(TietKiemBase):
    _id: int

    class Config:
        from_attributes = True
