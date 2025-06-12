from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import SessionLocal
from models.models_tong_hop import TongHopGiaoDichView

router = APIRouter(prefix="/tong_hop", tags=["Tong_hop"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. Get all
@router.get("/all")
def get_all_tong_hop(db: Session = Depends(get_db)):
    return db.query(TongHopGiaoDichView).all()

# 2. Get theo năm
@router.get("/nam/{nam}")
def get_tong_hop_theo_nam(nam: int, db: Session = Depends(get_db)):
    results = db.query(TongHopGiaoDichView).filter(TongHopGiaoDichView.nam == nam).all()
    if not results:
        raise HTTPException(status_code=404, detail="Không có dữ liệu cho năm này")
    return results

# 3. Get theo năm và tháng
@router.get("/nam/{nam}/thang/{thang}")
def get_tong_hop_theo_thang_va_nam(nam: int, thang: int, db: Session = Depends(get_db)):
    result = db.query(TongHopGiaoDichView).filter(
        TongHopGiaoDichView.nam == nam,
        TongHopGiaoDichView.thang == thang
    ).first()
    if not result:
        raise HTTPException(status_code=404, detail="Không có dữ liệu cho năm và tháng này")
    return result
