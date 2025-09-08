from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import crud_bangthemmoi_dautu
from schemas import schemas_themmoidautu
from database import database

router = APIRouter(prefix="/Them_Moi_Dau_Tu", tags=["Them_Moi_Dau_Tu"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas_themmoidautu.ThemMoiDauTuResponse)
def create(Them_Moi_Dau_Tu: schemas_themmoidautu.ThemMoiDauTuCreate, db: Session = Depends(get_db)):
    return crud_bangthemmoi_dautu.create_Them_Moi_Dau_Tu(db, Them_Moi_Dau_Tu)

@router.get("/", response_model=list[schemas_themmoidautu.ThemMoiDauTuResponse])
def read_all(db: Session = Depends(get_db)):
    return crud_bangthemmoi_dautu.get_Them_Moi_Dau_Tus(db)

@router.get("/{id}", response_model=schemas_themmoidautu.ThemMoiDauTuResponse)
def read_one(id: int, db: Session = Depends(get_db)):
    db_item = crud_bangthemmoi_dautu.get_Them_Moi_Dau_Tu(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Giao dịch không tồn tại")
    return db_item

@router.put("/{id}", response_model=schemas_themmoidautu.ThemMoiDauTuResponse)
def update(id: int, Them_Moi_Dau_Tu: schemas_themmoidautu.ThemMoiDauTuUpdate, db: Session = Depends(get_db)):
    db_item = crud_bangthemmoi_dautu.update_Them_Moi_Dau_Tu(db, id, Them_Moi_Dau_Tu)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy giao dịch")
    return db_item

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    db_item = crud_bangthemmoi_dautu.delete_Them_Moi_Dau_Tu(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy giao dịch")
    return {"message": "Xóa thành công"}
