from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DauTuBase(BaseModel):
    id: Optional[int] = None
    ghi_chu: Optional[str] = None
    ngay_nhap: Optional[datetime] = None
    tong_so_tien: Optional[int] = None
    tong_so_tien_vay_no: Optional[int] = None

class DauTuCreate(DauTuBase):
    pass

class DauTuUpdate(DauTuBase):
    pass

class DauTuResponse(DauTuBase):
    id: int = 0

    class Config:
        from_attributes = True
