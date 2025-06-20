from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TienNoBase(BaseModel):
    id: Optional[int] = None
    ghi_chu: Optional[str] = None
    ngay_nhap: Optional[datetime] = None
    tong_so_tien_vay_no: Optional[int] = None

class TienNoCreate(TienNoBase):
    pass

class TienNoUpdate(TienNoBase):
    pass

class TienNoResponse(TienNoBase):
    id: int = 0

    class Config:
        from_attributes = True
