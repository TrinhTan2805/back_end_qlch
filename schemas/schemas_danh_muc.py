from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DanhMucBase(BaseModel):
    id: Optional[int] = None
    ten_danh_muc: Optional[str] = None


class DanhMucCreate(DanhMucBase):
    pass

class DanhMucUpdate(DanhMucBase):
    pass

class DanhMucResponse(DanhMucBase):
    id: int = 0

    class Config:
        from_attributes = True
