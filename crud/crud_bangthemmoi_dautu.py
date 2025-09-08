from sqlalchemy.orm import Session
from models.bangthemmoi_dautu import ThemMoiDauTu
from schemas import schemas_themmoidautu

def create_Them_Moi_Dau_Tu(db: Session, Them_Moi_Dau_Tu: schemas_themmoidautu.ThemMoiDauTuCreate):
    db_item = ThemMoiDauTu(**Them_Moi_Dau_Tu.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_Them_Moi_Dau_Tus(db: Session):
    return db.query(ThemMoiDauTu).all()

def get_Them_Moi_Dau_Tu(db: Session, id: int):
    return db.query(ThemMoiDauTu).filter(ThemMoiDauTu.id == id).first()

def update_Them_Moi_Dau_Tu(db: Session, id: int, Them_Moi_Dau_Tu: schemas_themmoidautu.ThemMoiDauTuUpdate):
    db_item = db.query(ThemMoiDauTu).filter(ThemMoiDauTu.id == id).first()
    if db_item:
        for key, value in Them_Moi_Dau_Tu.dict(exclude_unset=True).items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_Them_Moi_Dau_Tu(db: Session, id: int):
    db_item = db.query(ThemMoiDauTu).filter(ThemMoiDauTu.id == id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
