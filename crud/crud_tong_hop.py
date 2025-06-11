from sqlalchemy.orm import Session
from models import models_tong_hop



def get_tiet_kiems(db: Session):
    return db.query(models_tong_hop.TongHopGiaoDichView).all()

def get_tiet_kiem(db: Session, id: int):
    return db.query(models_tong_hop.TongHopGiaoDichView).filter(models_tong_hop.TongHopGiaoDichView._id == id).first()


