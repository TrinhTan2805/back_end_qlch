from sqlalchemy.orm import Session
from models import models_danhmuc_nhom

def get_all_nhom(db: Session):
    return db.query(models_danhmuc_nhom.Nhom).all()