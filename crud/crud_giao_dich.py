from sqlalchemy import desc
from sqlalchemy.orm import Session

from models import models_giao_dich
from schemas import schemas_giao_dich

def create_giao_dich(db: Session, giao_dich: schemas_giao_dich.GiaoDichCreate):
    db_item = models_giao_dich.GiaoDich(**giao_dich.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_giao_dichs(db: Session):
    return db.query(models_giao_dich.GiaoDich).order_by(desc(models_giao_dich.GiaoDich.ngay_nhap)).all()

def get_giao_dich(db: Session, id: int):
    return db.query(models_giao_dich.GiaoDich).filter(models_giao_dich.GiaoDich._id == id).first()

def update_giao_dich(db: Session, id: int, giao_dich: schemas_giao_dich.GiaoDichUpdate):
    db_item = db.query(models_giao_dich.GiaoDich).filter(models_giao_dich.GiaoDich._id == id).first()
    if db_item:
        for key, value in giao_dich.dict(exclude_unset=True).items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_giao_dich(db: Session, id: int):
    db_item = db.query(models_giao_dich.GiaoDich).filter(models_giao_dich.GiaoDich._id == id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
