from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import crud_giao_dich

from schemas import schemas_giao_dich
from database import database

router = APIRouter(prefix="/giao_dich", tags=["Giao_dich"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas_giao_dich.GiaoDichResponse)
def create(giao_dich: schemas_giao_dich.GiaoDichCreate, db: Session = Depends(get_db)):
    return crud_giao_dich.create_giao_dich(db, giao_dich)

@router.get("/", response_model=list[schemas_giao_dich.GiaoDichResponse])
def read_all(db: Session = Depends(get_db)):
    return crud_giao_dich.get_giao_dichs(db)

@router.get("/{id}", response_model=schemas_giao_dich.GiaoDichResponse)
def read_one(id: int, db: Session = Depends(get_db)):
    db_item = crud_giao_dich.get_giao_dich(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Giao dịch không tồn tại")
    return db_item

@router.put("/{id}", response_model=schemas_giao_dich.GiaoDichResponse)
def update(id: int, giao_dich: schemas_giao_dich.GiaoDichUpdate, db: Session = Depends(get_db)):
    db_item = crud_giao_dich.update_giao_dich(db, id, giao_dich)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy giao dịch")
    return db_item

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    db_item = crud_giao_dich.delete_giao_dich(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy giao dịch")
    return {"message": "Xóa thành công"}
