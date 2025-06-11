from sqlalchemy.orm import Session
from models import models_tiet_kiem
from schemas import schemas_tiet_kiem

def create_tiet_kiem(db: Session, tiet_kiem: schemas_tiet_kiem.TietKiemCreate):
    db_item = models_tiet_kiem.TietKiem(**tiet_kiem.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_tiet_kiems(db: Session):
    return db.query(models_tiet_kiem.TietKiem).all()

def get_tiet_kiem(db: Session, id: int):
    return db.query(models_tiet_kiem.TietKiem).filter(models_tiet_kiem.TietKiem._id == id).first()

def update_tiet_kiem(db: Session, id: int, tiet_kiem: schemas_tiet_kiem.TietKiemUpdate):
    db_item = db.query(models_tiet_kiem.TietKiem).filter(models_tiet_kiem.TietKiem._id == id).first()
    if db_item:
        for key, value in tiet_kiem.dict(exclude_unset=True).items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_tiet_kiem(db: Session, id: int):
    db_item = db.query(models_tiet_kiem.TietKiem).filter(models_tiet_kiem.TietKiem._id == id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
