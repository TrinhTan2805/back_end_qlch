from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TongHopBase(BaseModel):
    id: int
    thang: int
    nam: int
    tong_giao_dich: Optional[float] = 0.0
    tong_thu_nhap: Optional[float] = 0.0
    tong_tiet_kiem: Optional[float] = 0.0

class TongHopCreate(TongHopBase):
    pass

class TongHopUpdate(TongHopBase):
    pass

class TongHopResponse(TongHopBase):
    class Config:
        from_attributes = True
