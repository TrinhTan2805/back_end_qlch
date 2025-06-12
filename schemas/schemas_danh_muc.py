from pydantic import BaseModel

class DanhMucBase(BaseModel):
    ten: str

class DanhMucCreate(DanhMucBase):
    pass

class DanhMucUpdate(DanhMucBase):
    pass

class DanhMucResponse(DanhMucBase):
    id: int

    class Config:
        from_attributes = True