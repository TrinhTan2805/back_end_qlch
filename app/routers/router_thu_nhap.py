from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import crud_thu_nhap
from schemas import schemas_thu_nhap
from database import database

router = APIRouter(prefix="/thu_nhap", tags=["Thu_nhap"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas_thu_nhap.ThuNhapResponse)
def create(thu_nhap: schemas_thu_nhap.ThuNhapCreate, db: Session = Depends(get_db)):
    return crud_thu_nhap.create_thu_nhap(db, thu_nhap)

@router.get("/", response_model=list[schemas_thu_nhap.ThuNhapResponse])
def read_all(db: Session = Depends(get_db)):
    return crud_thu_nhap.get_thu_nhaps(db)

@router.get("/{id}", response_model=schemas_thu_nhap.ThuNhapResponse)
def read_one(id: int, db: Session = Depends(get_db)):
    db_item = crud_thu_nhap.get_thu_nhap(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Giao dịch không tồn tại")
    return db_item

@router.put("/{id}", response_model=schemas_thu_nhap.ThuNhapResponse)
def update(id: int, thu_nhap: schemas_thu_nhap.ThuNhapUpdate, db: Session = Depends(get_db)):
    db_item = crud_thu_nhap.update_thu_nhap(db, id, thu_nhap)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy giao dịch")
    return db_item

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    db_item = crud_thu_nhap.delete_thu_nhap(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy giao dịch")
    return {"message": "Xóa thành công"}
