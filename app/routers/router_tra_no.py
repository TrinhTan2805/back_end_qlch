from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import crud_tra_no
from schemas import schemas_tra_no
from database import database

router = APIRouter(prefix="/tra_no", tags=["tra_no"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas_tra_no.TraNoResponse)
def create(tra_no: schemas_tra_no.TraNoCreate, db: Session = Depends(get_db)):
    return crud_tra_no.create_tra_no(db, tra_no)

@router.get("/", response_model=list[schemas_tra_no.TraNoResponse])
def read_all(db: Session = Depends(get_db)):
    return crud_tra_no.get_tra_nos(db)

@router.get("/{id}", response_model=schemas_tra_no.TraNoResponse)
def read_one(id: int, db: Session = Depends(get_db)):
    db_item = crud_tra_no.get_tra_no(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="trả nợ không tồn tại")
    return db_item

@router.put("/{id}", response_model=schemas_tra_no.TraNoResponse)
def update(id: int, tra_no: schemas_tra_no.TraNoUpdate, db: Session = Depends(get_db)):
    db_item = crud_tra_no.update_tra_no(db, id, tra_no)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy trả nợ")
    return db_item

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    try:
        db_item = crud_tra_no.delete_tra_no(db, id)
        if db_item is None:
            raise HTTPException(status_code=404, detail="Không tìm thấy trả nợ")
        return {"message": "Xóa thành công"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi server khi xóa: {str(e)}")

