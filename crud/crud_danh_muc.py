from sqlalchemy.orm import Session
from models import models_danh_muc
from schemas import schemas_danh_muc

def create_danh_muc(db: Session, danh_muc: schemas_danh_muc.DanhMucCreate):
    db_item = models_danh_muc.DanhMuc(**danh_muc.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_danh_mucs(db: Session):
    return db.query(models_danh_muc.DanhMuc).all()

def get_danh_muc(db: Session, id: int):
    return db.query(models_danh_muc.DanhMuc).filter(models_danh_muc.DanhMuc.id == id).first()

def update_danh_muc(db: Session, id: int, danh_muc: schemas_danh_muc.DanhMucUpdate):
    db_item = db.query(models_danh_muc.DanhMuc).filter(models_danh_muc.DanhMuc.id == id).first()
    if db_item:
        for key, value in danh_muc.dict(exclude_unset=True).items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_danh_muc(db: Session, id: int):
    db_item = db.query(models_danh_muc.DanhMuc).filter(models_danh_muc.DanhMuc.id == id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
