from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TraNoBase(BaseModel):
    id: Optional[int] = None
    ghi_chu: Optional[str] = None
    ngay_nhap: Optional[datetime] = None
    so_tien_tra_no: Optional[int] = None

class TraNoCreate(TraNoBase):
    pass

class TraNoUpdate(TraNoBase):
    pass

class TraNoResponse(TraNoBase):
    id: int = 0

    class Config:
        from_attributes = True
