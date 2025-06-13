from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TietKiemBase(BaseModel):
    id: Optional[int] = None
    nhom: Optional[str] = None
    ghi_chu: Optional[str] = None
    ngay_nhap: Optional[datetime] = None
    so_tien: Optional[int] = None

class TietKiemCreate(TietKiemBase):
    pass

class TietKiemUpdate(TietKiemBase):
    pass

class TietKiemResponse(TietKiemBase):
    id: int = 0

    class Config:
        from_attributes = True
