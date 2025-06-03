from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import crud_tiet_kiem

from schemas import schemas_tiet_kiem
from database import database

router = APIRouter(prefix="/tiet_kiem", tags=["Tiet_Kiem"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas_tiet_kiem.TietKiemResponse)
def create(tiet_kiem: schemas_tiet_kiem.TietKiemCreate, db: Session = Depends(get_db)):
    return crud_tiet_kiem.create_tiet_kiem(db, tiet_kiem)

@router.get("/", response_model=list[schemas_tiet_kiem.TietKiemResponse])
def read_all(db: Session = Depends(get_db)):
    return crud_tiet_kiem.get_tiet_kiems(db)

@router.get("/{id}", response_model=schemas_tiet_kiem.TietKiemResponse)
def read_one(id: int, db: Session = Depends(get_db)):
    db_item = crud_tiet_kiem.get_tiet_kiem(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Giao dịch không tồn tại")
    return db_item

@router.put("/{id}", response_model=schemas_tiet_kiem.TietKiemResponse)
def update(id: int, tiet_kiem: schemas_tiet_kiem.TietKiemUpdate, db: Session = Depends(get_db)):
    db_item = crud_tiet_kiem.update_tiet_kiem(db, id, tiet_kiem)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy giao dịch")
    return db_item

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    db_item = crud_tiet_kiem.delete_tiet_kiem(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy giao dịch")
    return {"message": "Xóa thành công"}
