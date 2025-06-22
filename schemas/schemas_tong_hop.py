from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TongHopBase(BaseModel):
    id: int
    thang: int
    nam: int
    tong_giao_dich: Optional[int] 
    tong_thu_nhap: Optional[int] 
    tong_tiet_kiem: Optional[int]
    tong_dau_tu: Optional[int] 
    tong_no: Optional[int]
    tong_tra_no: Optional[int]


class TongHopCreate(TongHopBase):
    pass

class TongHopUpdate(TongHopBase):
    pass

class TongHopResponse(TongHopBase):
    class Config:
        from_attributes = True
