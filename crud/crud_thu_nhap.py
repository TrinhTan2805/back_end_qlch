from sqlalchemy.orm import Session

from models import models_thu_nhap
from schemas import schemas_thu_nhap

def create_thu_nhap(db: Session, thu_nhap: schemas_thu_nhap.ThuNhapCreate):
    db_item = models_thu_nhap.ThuNhap(**thu_nhap.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_thu_nhaps(db: Session):
    return db.query(models_thu_nhap.ThuNhap).all()

def get_thu_nhap(db: Session, id: int):
    return db.query(models_thu_nhap.ThuNhap).filter(models_thu_nhap.ThuNhap._id == id).first()

def update_thu_nhap(db: Session, id: int, thu_nhap: schemas_thu_nhap.ThuNhapUpdate):
    db_item = db.query(models_thu_nhap.ThuNhap).filter(models_thu_nhap.ThuNhap._id == id).first()
    if db_item:
        for key, value in thu_nhap.dict(exclude_unset=True).items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_thu_nhap(db: Session, id: int):
    db_item = db.query(models_thu_nhap.ThuNhap).filter(models_thu_nhap.ThuNhap._id == id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
