from pydantic import BaseModel

class NhomSchema(BaseModel):
    id: int
    ten: str

    class Config:
        from_attributes = True
