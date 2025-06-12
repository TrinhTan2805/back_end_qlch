from pydantic import BaseModel
from typing import Optional


class DanhMucBase(BaseModel):
    id: Optional[int] = None
    ten: str

class DanhMucCreate(DanhMucBase):
    pass

class DanhMucUpdate(DanhMucBase):
    pass

class DanhMucResponse(DanhMucBase):
    id: int = 0

    class Config:
        from_attributes = True