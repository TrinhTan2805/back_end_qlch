from fastapi import APIRouter
from sqlalchemy.orm import Session
from models import models_danhmuc_nhom  # hoặc đúng tên model nhóm bạn dùng

router = APIRouter(prefix="/danh_muc", tags=["Danh muc nhom"])

def get_all_nhom(db: Session):
    return db.query(models_danhmuc_nhom.Nhom).all()
